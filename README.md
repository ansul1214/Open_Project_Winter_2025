# Machine Learning Assisted Quantum State Tomography and Hybrid HHL Verification
Open Project – Winter 2025

---

## 1. Project Overview

This project investigates the intersection of:

- Quantum State Tomography (QST)
- Machine Learning-assisted reconstruction
- Quantum channel classification
- Hybrid verification of HHL-style linear solvers

Assignments 1–5 build progressively toward a structured research-style workflow.

No new experiments were introduced in the final consolidation phase.

---

## 2. Assignment Contributions

### Assignment 1 – Foundational Quantum Simulation & Metrics

Assignment 1 established:

- Quantum state preparation using Qiskit
- Measurement simulation
- Density matrix construction
- Fidelity computation framework
- Baseline reconstruction evaluation

This assignment created the simulation backbone used in all subsequent experiments.

Key learning:
Understanding how quantum states are represented and evaluated numerically.

---

### Assignment 2 – ML-Based Quantum State Reconstruction

- Generated synthetic states.
- Encoded measurement data as features.
- Trained regression model to predict density matrix elements.

Results:
- Mean Fidelity: 0.7586
- Mean Trace Distance: 0.3993
- Inference Latency: 0.0049 s

Insight:
ML reconstruction is fast but fidelity decreases with system complexity.

---

### Assignment 3 – Pauli Tomography & Scalability

- Implemented Pauli-basis expectation value computation.
- Trained Ridge regression surrogate (`models/qst.pkl`).
- Studied scalability from 1 to 5 qubits.
- Performed ablation study on circuit depth.

Observation:
Fidelity decreases with increasing qubit count, while runtime remains nearly constant.

---

### Assignment 4 – Quantum Channel Classification

- Represented quantum channels via Choi matrices.
- Engineered 32-dimensional feature vectors.
- Trained Random Forest classifier.

Result:
Accuracy = 1.00

Insight:
Choi representations strongly separate channel families.

---

### Assignment 5 – HHL Workflow & Tomography Verification

- Solved Hermitian linear system.
- Generated HHL-style normalized solution.
- Applied phase alignment and amplitude scaling.
- Used ML-based QST surrogate to reconstruct state.
- Compared fidelities and residual norms.

Result:
Strong agreement between classical, HHL, and QST outputs.

---

## 3. Methodology

The project progresses through five structured stages, each increasing in algorithmic complexity and verification depth.

---

### 3.1 Assignment 1 – Quantum State Simulation Framework

This stage established the numerical simulation backbone for the project.

Methodology:

- Prepared quantum states using Qiskit statevector formalism.
- Converted statevectors into density matrices via outer product.
- Simulated measurement processes to obtain expectation values.
- Computed fidelity as a similarity metric.
- Implemented numerical validation routines.

This stage ensured familiarity with:

- State representation (|ψ⟩ and ρ)
- Measurement statistics
- Basic reconstruction validation

It formed the computational foundation for all later ML-based reconstruction.

---

### 3.2 Assignment 2 – ML-Based Quantum State Reconstruction

Objective: Learn a mapping from measurement statistics to density matrix elements.

Methodology:

1. Generated synthetic pure states.
2. Simulated measurement outcomes.
3. Encoded measurement data into feature vectors.
4. Flattened density matrices into regression targets.
5. Trained supervised regression models.
6. Evaluated reconstruction quality using:
   - Fidelity
   - Trace distance
   - Inference latency

This stage demonstrated how classical ML can approximate tomography mappings.

---

### 3.3 Assignment 3 – Pauli-Basis Tomography & Surrogate Training

Objective: Use Pauli operator expansion for structured state reconstruction.

Methodology:

- Computed full Pauli-basis expectation values:
  
  ρ = (1 / 2^n) Σ ⟨P_i⟩ P_i

- Constructed feature vectors from expectation values.
- Trained Ridge regression surrogate to predict density matrix elements.
- Saved surrogate model as `qst.pkl`.
- Conducted scalability study across 1–5 qubits.
- Performed ablation study on circuit depth.

This stage introduced structured tomography and studied how reconstruction degrades with system size.

---

### 3.4 Assignment 4 – Quantum Channel Classification

Objective: Classify noise channels via Choi matrix features.

Methodology:

- Defined depolarizing and amplitude damping channels using Kraus operators.
- Converted channels to Choi matrices.
- Flattened real and imaginary components into 32-dimensional feature vectors.
- Trained Random Forest classifier.
- Evaluated precision, recall, and F1-score.

This stage demonstrated supervised classification in quantum process space.

---

### 3.5 Assignment 5 – HHL Workflow & Hybrid Verification

Objective: Verify a linear-system solution using ML-based tomography.

Methodology:

1. Defined well-conditioned Hermitian matrix A.
2. Solved Ax = b classically (baseline).
3. Generated normalized quantum-style solution (HHL surrogate).
4. Applied global phase alignment:

   ψ_aligned = ψ exp(-i arg(⟨ψ | x_classical⟩))

5. Applied amplitude rescaling.
6. Generated Pauli expectation values from HHL state.
7. Loaded QST surrogate (`qst.pkl`).
8. Reconstructed density matrix and extracted dominant eigenstate.
9. Computed:
   - L2 error
   - Relative error
   - Residual norm
   - Fidelity comparisons

This stage integrates quantum linear solving with ML-assisted verification.

---


## 4. Key Insights

- Fidelity degrades as qubit count increases.
- Runtime remains low for small systems.
- Channel classification is highly separable in Choi space.
- Phase alignment is critical for quantum-classical comparisons.
- Tomography overhead may erode theoretical HHL speedups.

---

## 5. Conclusion

This project demonstrates that ML-assisted tomography can support hybrid quantum-classical workflows. However, scalability is limited by:

- Exponential state growth
- Reconstruction overhead
- Conditioning sensitivity in linear solvers

Future work may explore compressed sensing tomography and observable-based verification instead of full state reconstruction.
