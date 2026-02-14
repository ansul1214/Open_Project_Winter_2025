# Replication Guide

## 1. Environment Setup

Python version: 3.9+

Create virtual environment:

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Install dependencies:

pip install torch numpy scipy

---

## 2. Project Structure

ML-Tomography/
├── src/
├── outputs/
├── docs/
├── AI_USAGE.md
└── README.md

---

## 3. Running Training

From project root:

cd src
python train.py

---

## 4. Outputs Generated

After training:

- outputs/model.pt
- outputs/metrics.txt

---

## 5. Reproducing Metrics

Metrics printed in terminal:

- Mean Fidelity
- Mean Trace Distance
- Inference Latency

They are also saved inside outputs/metrics.txt
