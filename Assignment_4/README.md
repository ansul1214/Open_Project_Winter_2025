# Assignment 4 – Channel Classification Workflow

## Overview

This assignment demonstrates how a trained machine learning classifier can be reused to rapidly label noisy quantum channels during calibration checks.

Two workflows are implemented:

1. Reuse of the trained classifier from Assignment 3 (production-style deployment).
2. A lightweight calibration-time classifier trained directly inside the notebook.

The goal is to validate an end-to-end inference pipeline using Choi-based feature representations of quantum channels.

---

## Model Artifact Used

The trained classifier from Assignment 3 is stored at:

Assignment_3/channel_classifier.pkl

Project structure:

Open_Project_Winter_2025/
│
├── Assignment_3/
│   ├── channel_classifier.pkl
│   ├── model_1qubits.pkl
│   ├── model_3qubits.pkl
│   ├── model_5qubits.pkl
│   └── ...
│
└── Assignment_4_notebook.ipynb

The model is loaded using:

model_path = "Assignment_3/channel_classifier.pkl"
model = joblib.load(model_path)

The load was verified using:

- model.n_features_in_
- model.classes_

The classifier successfully loads as a RandomForestClassifier.

---

## Environment Validation (Task 1)

The following libraries were confirmed to import without errors:

- qiskit
- numpy
- pandas
- joblib
- scikit-learn

If any dependency is missing, it can be installed using:

pip install qiskit numpy pandas joblib scikit-learn

---

## Feature Encoding Strategy

To ensure compatibility between Assignment 3 and Assignment 4, the feature mapping was kept identical.

Feature pipeline:

Kraus Operators → Choi Matrix → Flatten → Real + Imag Concatenation

Feature vector structure:

- 16 real entries
- 16 imaginary entries
- Total dimension = 32

Feature mapping function:

def channel_to_feature(channel):
    choi = Choi(channel).data
    real_part = np.real(choi).flatten()
    imag_part = np.imag(choi).flatten()
    return np.concatenate([real_part, imag_part])

No normalization or structural modifications were introduced.  
This prevents feature drift and ensures production compatibility.

---

## Model Details

- Model Type: RandomForestClassifier
- Feature Dimension: 32
- Classes:
  - depolarizing
  - amplitude_damping

The model correctly predicts channel families using Choi features.

---

## Task 3 – Lightweight Calibration-Time Classifier

A standalone classifier was implemented inside the function:

build_channel_classifier()

This function:

1. Generates synthetic depolarizing and amplitude damping channels.
2. Converts channels to Choi feature vectors.
3. Splits data into train/validation sets.
4. Trains a RandomForest baseline.
5. Reports validation accuracy.
6. Returns the trained estimator.

Validation accuracy achieved: 1.0

This is expected because the two channel families have structurally distinct Choi matrices.

---

## Task 4 & Task 5 – Sample Channel Classification

A small batch of synthetic channels was evaluated:

- depolarizing_p0.1
- depolarizing_p0.5
- amp_damp_0.1
- amp_damp_0.5

Channels were converted using channel_to_feature(), stacked into a feature matrix, and passed to the classifier.

All channels were correctly classified with high confidence.

---

## End-to-End Workflow

Complete pipeline:

1. Validate environment.
2. Load trained classifier from Assignment 3.
3. Rebuild feature mapper.
4. Generate synthetic channels.
5. Convert to Choi features.
6. Predict channel labels.
7. Review predictions in a DataFrame.

This confirms successful deployment-style reuse of a trained ML artifact.

---

## Reflection

This assignment demonstrates how a trained machine learning model can be reused in a production-style quantum calibration workflow without retraining.

By maintaining identical feature encoding between assignments, compatibility was preserved and inference errors were avoided.

The classifier provides near-instant channel labeling, illustrating how ML can support rapid noise diagnostics in quantum systems.

---

## Submission Confirmation

- Model path updated and verified.
- Trained artifact successfully loaded.
- Feature mapping kept identical to training configuration.
- Tasks 1–5 executed with visible outputs.
- Reflection included.
