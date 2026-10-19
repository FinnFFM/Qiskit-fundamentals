"""Execute the solution notebook in a fresh kernel; optionally save its outputs."""
import argparse
from pathlib import Path
import tempfile
import sys

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='save executed outputs')
    args = parser.parse_args()
    path = Path(__file__).with_name('exercises.ipynb')
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    # Bind the kernel to this interpreter instead of an unrelated global Python.
    with tempfile.TemporaryDirectory() as directory:
        import json
        kernel = Path(directory) / 'solutions'
        kernel.mkdir()
        (kernel / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'Solutions', 'language': 'python',
            'env': {'MPLBACKEND': 'module://matplotlib_inline.backend_inline'},
        }))
        manager = KernelManager(kernel_name='solutions',
                                kernel_spec_manager=KernelSpecManager(kernel_dirs=[directory]))
        NotebookClient(notebook, km=manager, timeout=180,
                       resources={'metadata': {'path': str(path.parent)}}).execute()
    if args.write:
        nbformat.write(notebook, path)
    code_cells = sum(cell.cell_type == 'code' for cell in notebook.cells)
    print(f'PASS: {code_cells} code cells executed; all assertions passed.')


if __name__ == '__main__':
    main()
