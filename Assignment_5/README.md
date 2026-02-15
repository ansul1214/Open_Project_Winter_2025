# Assignment 5 – HHL Workflow and Tomography Verification

## Overview

This assignment revisits the HHL algorithm for solving a 4×4 linear system and integrates an ML-based tomography surrogate for verification.

The workflow compares:

- Classical solution
- HHL-style normalized quantum solution
- ML-based tomography reconstruction

---

## Problem Statement

Solve a Hermitian linear system Ax = b and verify the solution using tomography reconstruction.

---

## Methodology

1. Define a well-conditioned 4×4 Hermitian matrix.
2. Solve classically to obtain the baseline solution.
3. Generate HHL-style normalized quantum solution.
4. Align global phase and rescale amplitudes.
5. Compute L2 error, relative error, and residual norm.
6. Generate Pauli expectation values from HHL output.
7. Load ML-based surrogate (`Assignment_3/qst.pkl`).
8. Reconstruct density matrix and extract dominant eigenstate.
9. Compare fidelities and residuals.

---

## Metrics

- L2 vector error
- Relative error
- Residual norm
- Fidelity (QST vs HHL)
- Fidelity (QST vs Classical)

---

## Why Efficient QST Matters

HHL outputs amplitude-encoded solutions, but hardware provides only measurement samples. Tomography is required to recover amplitude-level observables.

Efficient QST:

- Reduces measurement overhead
- Preserves potential speed-up
- Enables calibration and debugging workflows

---

## Key Insights

- Phase alignment is essential for fair comparison.
- ML-based tomography accurately reconstructs solution amplitudes.
- Scalability depends on sparsity, conditioning, and measurement cost.
- Hybrid validation pipelines are critical for practical deployment.

---

## Artefacts Used

- Assignment_3/qst.pkl → ML-based tomography surrogate
- HHL workflow notebook
- Comparison tables and metrics
