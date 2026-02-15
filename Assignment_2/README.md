# Assignment 2 – ML-Based Quantum State Reconstruction

## Overview

This assignment implements a machine learning approach to quantum state tomography (QST).  
The objective is to reconstruct quantum density matrices from measurement statistics using supervised regression.

The workflow demonstrates how classical ML models can approximate quantum state reconstruction efficiently.

---

## Problem Statement

Given measurement data from quantum experiments, reconstruct the underlying quantum state (density matrix).

This involves:

- Generating labelled quantum states
- Encoding measurement statistics as features
- Training a regression model
- Evaluating reconstruction accuracy using physically meaningful metrics

---

## Methodology

1. Generate synthetic quantum states.
2. Simulate measurement statistics.
3. Encode measurement outcomes into feature vectors.
4. Train a regression model to predict density matrix elements.
5. Evaluate reconstruction performance using fidelity and trace distance.

---

## Results

The trained model achieved the following performance metrics:

- **Mean Fidelity:** 0.7586179971694946  
- **Mean Trace Distance:** 0.39925656353433925  
- **Inference Latency:** 0.004904270172119141 seconds  

### Interpretation

- A mean fidelity of ~0.76 indicates that the reconstructed states preserve a substantial portion of the original quantum information.
- A mean trace distance of ~0.40 reflects moderate deviation between predicted and true density matrices.
- Inference latency (~4.9 ms) demonstrates that ML-based reconstruction is computationally efficient and suitable for repeated evaluations.

---

## Metrics Explained

**Fidelity**

\[
F(\rho, \sigma) = \left( \mathrm{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}} \right)^2
\]

Measures similarity between two quantum states.

**Trace Distance**

\[
T(\rho, \sigma) = \frac{1}{2} \|\rho - \sigma\|_1
\]

Measures distinguishability between two density matrices.

---

## Key Takeaways

- ML-based tomography can approximate density matrices with reasonable accuracy.
- Reconstruction accuracy depends on feature representation and training data quality.
- Inference is fast, making ML-based QST suitable for repeated calibration workflows.
- There is a trade-off between fidelity and computational efficiency.

---

## Files Included

- Trained model checkpoints (.pkl)
- Reconstruction plots
- Dataset files (.npy/.npz)
- Performance metrics summary
