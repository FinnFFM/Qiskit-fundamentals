# Qiskit-fundamentals-course
A course to teach the basics of IBM's Qiskit SDK

## Worked exercises in this fork

This fork tracks [JoeyRogers-svg/Qiskit-fundamentals](https://github.com/JoeyRogers-svg/Qiskit-fundamentals).
The original course notebooks remain unchanged. The latest upstream revision
included here is `27ec6cc` (29 July 2026).

**[Open the worked solutions](solutions/exercises.ipynb)** for the exercises in
weeks 2–7, with explanations, plots, and executable checks. These additions were
prepared with AI assistance. See [setup and coverage](solutions/README.md) for
the small, pinned local environment. No IBM account is required for the solutions.

The installation instructions below are for the **full upstream course**;
some original notebooks include cloud/hardware examples.


## Installation

This project uses **uv** for dependency management. The repository includes:

- `pyproject.toml` — project dependencies  
- `uv.lock` — locked dependency versions for reproducible environments  

Using **uv** is recommended because it is fast and ensures everyone installs the same dependency versions.

---

## Option 1 (Recommended): Install with uv

### Install uv

See the official installation instructions:  
https://docs.astral.sh/uv/getting-started/installation/

Or install directly from the terminal.

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatively, install with pip:

```bash
pip install uv
```

---

### Install project dependencies

Clone the repository and run:

```bash
uv sync
```

This will:

- create a virtual environment (`.venv`)
- install all dependencies from `pyproject.toml`
- reproduce the exact environment defined in `uv.lock`

Activate the environment:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

---

## Option 2: Install with pip

If you prefer using pip, you can install the project directly from `pyproject.toml`.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

Install the project:

```bash
pip install .
```

---

## Option 3: Install with Conda

If you prefer Conda, create an environment and install the project using pip.

Create the environment:

```bash
conda create -n qiskit-fundamentals python=3.12
```

Activate it:

```bash
conda activate qiskit-fundamentals
```

Install the project:

```bash
pip install .
```
