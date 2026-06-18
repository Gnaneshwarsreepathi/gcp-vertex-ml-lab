# GCP Vertex AI MLOps Project

## Overview

This project demonstrates an end-to-end Machine Learning Operations (MLOps) workflow using Google Cloud Vertex AI.

A Random Forest machine learning model is trained using the Iris dataset, registered in Vertex AI Model Registry, deployed to a Vertex AI Endpoint, and tested through real-time online predictions.

The objective of this project is to understand the complete lifecycle of a machine learning model in a cloud-native environment using managed Google Cloud services.

---

## Architecture

![GCP Vertex AI MLOps Architecture](03-architecture-diagram.png)

Figure: End-to-End Vertex AI MLOps Workflow

## Project Architecture

```text
Iris Dataset
      |
      v
train.py
      |
      v
Vertex AI Custom Training Job
      |
      v
Cloud Storage Bucket
(model.joblib)
      |
      v
Vertex AI Model Registry
      |
      v
Vertex AI Endpoint
      |
      v
Online Prediction API
      |
      v
Prediction Response
```

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Google Cloud Platform (GCP) | Cloud Infrastructure |
| Vertex AI | Model Training and Deployment |
| Cloud Storage | Model Artifact Storage |
| Python 3.10 | Development Language |
| Scikit-Learn | Machine Learning Framework |
| Random Forest Classifier | Classification Algorithm |
| Joblib | Model Serialization |
| Git | Version Control |
| GitHub | Source Code Repository |

---

## Dataset

The project uses the Iris dataset provided by Scikit-Learn.

### Dataset Characteristics

- Total Records: 150
- Features: 4
- Classes: 3

### Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

- Setosa (0)
- Versicolor (1)
- Virginica (2)

---

## Project Structure

```text
gcp-vertex-ml-lab/
│
├── train.py
├── run_vertex_lab.py
├── predict.py
├── README.md
└── architecture.png
```

---

## Workflow

### Step 1: Configure GCP Environment

The project begins by configuring the Google Cloud environment.

```bash
PROJECT_ID=$(gcloud config get-value project)

REGION=us-central1

BUCKET=${PROJECT_ID}-vertex-ml-lab-$RANDOM

export PROJECT_ID
export REGION
export BUCKET
```

---

### Step 2: Enable Required APIs

The following services are enabled:

```bash
gcloud services enable \
aiplatform.googleapis.com \
storage.googleapis.com \
artifactregistry.googleapis.com
```

Services enabled:

- Vertex AI API
- Cloud Storage API
- Artifact Registry API

---

### Step 3: Create Cloud Storage Bucket

A Cloud Storage bucket is created to store model artifacts.

```bash
gsutil mb -l $REGION gs://$BUCKET
```

Example:

```text
gs://project-xxxxx-vertex-ml-lab-17840
```

---

### Step 4: Train Machine Learning Model

The training logic is implemented in:

```text
train.py
```

The script performs:

- Load Iris Dataset
- Split Dataset
- Train Random Forest Model
- Evaluate Model Accuracy
- Save Model as model.joblib
- Upload Model to Cloud Storage

Model Configuration:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

---

### Step 5: Submit Vertex AI Custom Training Job

The orchestration script:

```text
run_vertex_lab.py
```

creates a Vertex AI Custom Training Job.

Training Container:

```text
us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-6:latest
```

Machine Type:

```text
n1-standard-4
```

Output Location:

```text
gs://<bucket-name>/vertex-output
```

---

### Step 6: Store Model Artifact

After successful training, the model is saved as:

```text
model.joblib
```

and stored in:

```text
Google Cloud Storage
```

Example:

```text
gs://<bucket>/vertex-output/model/model.joblib
```

---

### Step 7: Register Model in Vertex AI

The trained model is automatically registered in Vertex AI Model Registry.

Model Name:

```text
iris-random-forest-model
```

Benefits:

- Model Versioning
- Model Governance
- Deployment Management
- Lifecycle Tracking

---

### Step 8: Deploy Model to Endpoint

The model is deployed to a Vertex AI Endpoint for online inference.

Endpoint Name:

```text
iris-random-forest-model_endpoint
```

Deployment Configuration:

```text
Machine Type : n1-standard-2
Min Replicas : 1
Max Replicas : 1
Traffic Split : 100%
```

---

### Step 9: Real-Time Prediction

Prediction requests are sent to the deployed endpoint.

Example Input:

```python
[
 [5.1, 3.5, 1.4, 0.2],
 [6.7, 3.1, 4.7, 1.5],
 [7.2, 3.6, 6.1, 2.5]
]
```

Example Output:

```text
[0, 1, 2]
```

Class Mapping:

| Prediction | Flower |
|------------|---------|
| 0 | Setosa |
| 1 | Versicolor |
| 2 | Virginica |

---

## Verification Commands

### List Training Jobs

```bash
gcloud ai custom-jobs list --region=us-central1
```

### List Registered Models

```bash
gcloud ai models list --region=us-central1
```

### List Endpoints

```bash
gcloud ai endpoints list --region=us-central1
```

### View Storage Bucket Contents

```bash
gsutil ls -r gs://<bucket-name>
```

---

## Results

### Training Job

Status:

```text
JOB_STATE_SUCCEEDED
```

### Model Registry

Model successfully registered in Vertex AI.

### Endpoint Deployment

Status:

```text
READY
```

### Prediction

Successful online inference performed through Vertex AI Endpoint.

---

## Screenshots

The project documentation contains screenshots for:

- GCP Project Configuration
- API Enablement
- Cloud Storage Bucket Creation
- Training Script
- Vertex AI Training Job
- Model Registry
- Endpoint Deployment
- Online Prediction
- GitHub Repository
- Project Backup

---

## Learning Outcomes

Through this project, the following MLOps concepts were implemented:

- Cloud-Based Model Training
- Managed Infrastructure
- Model Artifact Management
- Model Versioning
- Model Registry
- Endpoint Deployment
- Real-Time Inference
- Cloud Storage Integration
- Git Version Control
- End-to-End MLOps Lifecycle

---

## Future Enhancements

Possible improvements include:

- CI/CD using GitHub Actions
- Automated Model Retraining
- Model Monitoring
- Feature Store Integration
- ML Pipelines
- Infrastructure as Code (Terraform)
- Multi-Environment Deployment

---

## Author

**Sreepathi Gnaneshwar**

Data Engineer | MLOps Engineer | Cloud & AI Enthusiast

GitHub Repository:

```text
https://github.com/Gnaneshwarsreepathi/gcp-vertex-ml-lab
```

---

## License

This project is intended for educational and learning purposes.
