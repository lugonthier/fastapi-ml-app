# FastAPI ML Model Deployment on GCP (in less than 5 minutes)

This repository contains the necessary resources and instructions for deploying a Scikit-Learn model as a dynamic web service, utilizing FastAPI, Docker, and Google Cloud Run. This tutorial is designed for data scientists and ML engineers seeking to efficiently operationalize their ML models.

## Prerequisites
Before starting, ensure you have:

- A Google Cloud Platform (GCP) account
- The Google Cloud SDK installed and initialized on your machine


## Repository Contents
- FastAPI application ([main.py](main.py))
- Sample model generation script ([train.py](train.py))
- Docker configuration ([Dockerfile](Dockerfile))
- Requirements file ([requirements.txt](requirements.txt))
- Instructions for deploying the application on Google Cloud Run

Note : The [train.py](train.py) script is provided to generate a sample ML model for testing purposes. Run this script to create a model before deploying the application.

## Setup and Usage
### 1 - Create a FastAPI App
FastAPI is a modern web framework for building APIs with Python type hints. It's fast and allows for high performance.

### 1.1 - Initialize Your Project
```bash
mkdir fastapi-ml-app && cd fastapi-ml-app
```

### 1.2 - Create Your FastAPI Application ([main.py](main.py))
The FastAPI application serves as the server handling requests to your model. It exposes endpoints for health checks and model predictions.

### 1.3 - Specify Your Dependencies ([requirements.txt](requirements.txt))
List the necessary dependencies for your application. Change as needed to match your project requirements.


## 2 - Containerize with Docker

Docker packages your app and its environment, ensuring consistent behavior across different deployment environments.

### 2.1 - The [Dockerfile](Dockerfile)
The Dockerfile creates a lightweight Python environment, installs dependencies, and sets the command to run the FastAPI app.

### 2.2 - Build and Run Your Container Locally (Optional)
Test your app locally with Docker before deploying:
```bash
docker build -t fastapi-ml-app .
docker run -p 8080:8080 fastapi-ml-app
```

Then go to http://0.0.0.0:8080/docs/ to interact with your app.


## 4 - Build and Deploy
Utilize Google Cloud SDK for deploying the application to Google Cloud Run. Replace placeholders  (e.g., `[REPOSITORY]`, `[REGION]`, `[PROJECT-ID]`)  with your specific details.

### 4.1 - Create an Artifact Registry Repository
Use Google Artifact Registry for storing and managing your Docker images.

```bash
gcloud artifacts repositories create [REPOSITORY] --repository-format=docker --location=[REGION] --description="Docker repository"

```

### 4.2 - Build Your App with Google Cloud Build
Automatically build your container image in the cloud and push it to your Artifact Registry.
 ```bash
 gcloud builds submit --tag [REGION]-docker.pkg.dev/[PROJECT-ID]/[REPOSITORY]/fastapi-ml-app
 ```

 ### 4.3 - Deploy Your App to Google Cloud Run
```bash
gcloud run deploy fastapi-ml-app --image [REGION]-docker.pkg.dev/[PROJECT-ID]/[REPOSITORY]/fastapi-ml-app --platform managed
```

## 5 - Clean Up Resources
Instructions to delete any services or resources that are no longer needed.

### 5.1 - Delete The Cloud Run Service
```bash
gcloud run services delete fastapi-ml-app --platform managed --project [PROJECT-ID]
```
### 5.2 - Delete The Artifact Registry Repository
```bash
gcloud artifacts repositories delete [REPOSITORY] --location=[REGION]
```
