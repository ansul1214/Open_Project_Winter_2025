# Assignment 4 – Quantum Channel Classification

## Overview

This assignment builds a machine learning classifier to distinguish between noisy quantum channels using Choi matrix representations.

The classifier supports rapid calibration checks in production-style workflows.

---

## Problem Statement

Classify quantum noise channels (e.g., depolarizing vs amplitude damping) using features derived from Choi matrices.

---

## Methodology

1. Define Kraus operators for channel families.
2. Convert channels to Choi matrices.
3. Flatten real and imaginary parts into feature vectors.
4. Train classifiers (Logistic Regression and Random Forest).
5. Evaluate accuracy and confusion matrices.
6. Reuse the saved classifier for inference.

---

## Results

- High classification accuracy on synthetic datasets.
- Random Forest captures nonlinear structure effectively.

---

## Production Workflow

1. Load saved classifier.
2. Rebuild feature mapping.
3. Predict channel labels for calibration runs.

---

## Learning Outcomes

- Understanding Choi representations of quantum channels
- Feature engineering for quantum processes
- Model reuse in deployment scenarios
- Calibration-oriented inference pipelines
