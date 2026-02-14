# Assignment 3 – Scalable Quantum Tomography Framework

## Overview

This assignment implements a scalable n-qubit surrogate model for quantum state tomography.

The framework supports:
- Arbitrary qubit scaling
- Model checkpointing using pickle
- Scalability benchmarking
- Ablation analysis over circuit depth
- Reproducible experiment logging

---

## State Representation

For an n-qubit system:

Dimension:
d = 2^n

Model parameters represent the real and imaginary parts of a complex statevector.

Normalized state:

|ψ⟩ = (r + i c) / ||r + i c||

where r, c ∈ ℝ^d.

---

## Fidelity Metric

Reconstruction quality is measured using:

F = |⟨ψ | φ⟩|²

Expected fidelity between random states:

E[F] = 1 / 2^n

Experimental results confirm this exponential scaling.

---

## Saved Checkpoints

Located in:

models/

Files included:
- model_1qubits.pkl
- model_3qubits.pkl
- model_5qubits.pkl

Each file contains:

{
    "n_qubits": int,
    "n_layers": int,
    "params": numpy.ndarray
}

---

## How to Load a Model

```python
import pickle

def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)

data = load_pickle("models/model_3qubits.pkl")

model = QuantumModel(
    n_qubits=data["n_qubits"],
    n_layers=data["n_layers"],
    params=data["params"]
)
