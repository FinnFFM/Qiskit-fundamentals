# Worked exercises

[exercises.ipynb](exercises.ipynb) contains self-contained solutions with saved
outputs. The course material belongs to the upstream authors; these additional
solutions were prepared with AI assistance. Existing worked homework examples
are acknowledged in the notebook.

## Run locally

Tested on Ubuntu with Python **3.13.3** and Qiskit **2.3.0**. From the repository root:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r solutions/requirements.txt
.venv/bin/python solutions/check.py
```

If `python3` is your Python 3.13 interpreter, use it in the first command.
All installed dependencies are pinned in `requirements.txt`. This smaller
environment is for the solution notebook; the full course has separate
dependencies in the root `pyproject.toml` and `uv.lock`.

The checker starts a fresh kernel using the selected interpreter, executes all
15 code cells, and fails on any execution error or failed assertion. Run with
`--write` to refresh saved notebook outputs. To experiment interactively, open
the notebook in a Jupyter-compatible editor and select `.venv/bin/python`.

## Coverage

| Source | Answers in the solution notebook |
| --- | --- |
| Week 2: single-qubit gates | Six input states, ten gates, phase relationships, H identities, measurement and shots |
| Week 3: multiple qubits | All four Bell states and concurrence |
| Week 4: exercises 1–5 | Gate order, phase kickback, three-CNOT SWAP, global/relative phase, inverse Bell preparation |
| Week 4: homework 1–3 | Product-state probabilities, generalized GHZ preparation, partial entanglement |
| Week 5: transpilation exercises | RZZ at four optimization levels and five angles; gate decomposition and linear-connectivity routing |
| Week 6: exercises 1–2 | A 20-angle RX sweep in one Sampler V2 PUB; Bell correlations with Estimator V2 |
| Week 7: embedded questions | State preparation by rotations and hopping-Hamiltonian evolution |

The original exercise cells are kept intact; use this notebook alongside them.
External IBM learning-module homework and certificate material are not included
in this coverage. Weeks 1 and 8 contain demonstrations rather than additional
explicit exercise cells; their examples have not been re-executed here.

All added examples use ideal local simulation. Transpilation uses an explicit
Manila-like gate basis and a simple line coupling map, rather than a historical
device calibration. It checks the resulting operators including qubit layout.
Gate counts are compiler-dependent, and simulation does not demonstrate physical
hardware fidelity. Sampling and transpilation use fixed seeds.

Two details in the task wording deserve care: Qiskit displays the most significant
qubit first, and an inclusive 20-point grid from 0 to 2π does not contain π.
Both are explained in the answers.

API reference: [Qiskit 2.3 V2 primitives](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.3/primitives).
