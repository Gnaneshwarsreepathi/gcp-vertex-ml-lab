# GCP Vertex AI MLOps Project

## Project Overview

This project demonstrates an end-to-end MLOps workflow using Google Cloud Vertex AI.

A Random Forest machine learning model is trained on the Iris dataset, registered in Vertex AI Model Registry, deployed to a Vertex AI Endpoint, and used for real-time online predictions.

The project showcases key MLOps concepts including:

- Cloud-based model training
- Model artifact management
- Model Registry
- Model Deployment
- Online Inference
- Infrastructure automation using Python

---

## Architecture

Iris Dataset
↓
train.py
↓
Vertex AI Custom Training Job
↓
Cloud Storage Bucket
↓
Vertex AI Model Registry
↓
Vertex AI Endpoint
↓
Online Prediction API
↓
Prediction Response

---

## Technologies Used

- Google Cloud Platform (GCP)
- Vertex AI
- Cloud Storage
- Python 3.10
- Scikit-Learn
- Random Forest Classifier
- Git
- GitHub

---

## Project Structure

```text
gcp-vertex-ml-lab/
│
├── train.py
├── run_vertex_lab.py
├── predict.py
└── README.md
