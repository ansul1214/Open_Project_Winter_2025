# Assignment 3 – Pauli Tomography and ML Surrogate

## Overview

This assignment implements Pauli-basis quantum state tomography and trains a regression-based surrogate model to reconstruct density matrices from Pauli expectation values.

The trained surrogate is saved and reused in Assignment 5.

---

## Problem Statement

Reconstruct quantum states using Pauli expectation values and build a machine learning model that maps expectation vectors to density matrix coefficients.

---

## Methodology

1. Generate random pure quantum states.
2. Compute full Pauli-basis expectation values.
3. Construct feature vectors from expectation values.
4. Train a Ridge regression model to predict density matrix elements.
5. Save the surrogate model as `Assignment_3/qst.pkl`.

---

## Artefacts

- qst.pkl → ML-based Pauli tomography surrogate
- Channel classifier models
- Evaluation plots

---

## Why This Matters

The ML surrogate:

- Reduces tomography post-processing cost
- Allows reuse across experiments
- Enables fast reconstruction in hybrid workflows

---

## Learning Outcomes

- Understanding Pauli operator expansion
- Implementing regression-based tomography
- Saving and reusing trained ML artefacts
- Preparing models for cross-assignment deployment
