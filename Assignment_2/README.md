# Assignment 2 – ML-Based Quantum State Reconstruction

## Overview

This assignment introduces supervised machine learning for reconstructing quantum states from measurement data. The objective is to map measurement statistics to density matrices using classical regression models.

The workflow demonstrates how ML can approximate quantum state tomography (QST) in a data-driven manner.

---

## Problem Statement

Given measurement statistics from quantum experiments, reconstruct the underlying quantum state (density matrix).

This involves:

- Preparing labelled datasets of measurement outcomes
- Encoding features appropriately
- Training a regression model
- Evaluating reconstruction accuracy

---

## Methodology

1. Generate synthetic quantum states.
2. Simulate measurement statistics.
3. Encode measurement data into feature vectors.
4. Train a regression model to predict density matrix elements.
5. Evaluate reconstruction fidelity and error metrics.

---

## Metrics Used

- Fidelity
- L2 reconstruction error
- Trace distance
- Training loss

---

## Key Takeaways

- ML can approximate tomography mappings efficiently.
- Reconstruction accuracy depends on dataset quality and feature encoding.
- This lays the foundation for scalable QST surrogates used in later assignments.

---

## Files

- Trained model checkpoints (.pkl)
- Reconstruction plots
- Dataset files (.npy/.npz)





