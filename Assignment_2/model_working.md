# Model Working – Classical Shadows with GNN (Track 1)

## 1. Problem Statement

The objective is to reconstruct a quantum density matrix ρ from classical shadow measurement data.

The reconstructed matrix must satisfy:

- Hermitian
- Positive Semi-Definite (PSD)
- Unit Trace

These constraints are enforced using Cholesky parameterization.

---

## 2. Classical Shadows (2-Qubit System)

For a 2-qubit system, the density matrix dimension is:

dim = 2² = 4

Each sample consists of:

- Random Pauli measurement bases (XX, XY, ..., ZZ)
- Corresponding measurement outcomes

Each measurement shot is encoded as:

[one-hot basis encoding (6 values), measurement outcome]

Thus each node has 7 features.

Multiple shots form a graph of measurement nodes.

---

## 3. Graph Neural Network Architecture

Each measurement shot is treated as a node in a fully connected graph.

Architecture:

1. Node embedding layer
2. Two rounds of message passing
3. GRU-based update function
4. Global readout layer

Message passing allows the model to learn correlations between different measurement bases.

---

## 4. Physical Constraint Enforcement

The network outputs a matrix L (4×4).

We enforce:

ρ = (L L†) / Tr(L L†)

Where:

- L is lower triangular
- L† is conjugate transpose
- Tr ensures unit trace

This guarantees:

- Hermitian matrix
- Positive Semi-Definite
- Trace = 1

No penalty terms are used; constraints are enforced structurally.

---

## 5. Training Objective

Loss function:

Mean Squared Error (MSE) between predicted ρ and ground-truth ρ (real components).

Optimizer: Adam  
Scheduler: StepLR

---

## 6. Evaluation Metrics

As required:

1. Mean Fidelity:
   Measures similarity between quantum states.

2. Trace Distance:
   Measures distinguishability between quantum states.

3. Inference Latency:
   Time required for single reconstruction.

---

## 7. Observations

The model successfully reconstructs valid density matrices under physical constraints.

Performance metrics are reported in outputs/metrics.txt.
