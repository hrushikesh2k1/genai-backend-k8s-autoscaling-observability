# GenAI Backend on Kubernetes with Autoscaling & Observability

A **production-style GenAI backend** built using **FastAPI**, containerized with **Docker**, deployed on **Kubernetes**, horizontally autoscaled using **CPU-based HPA**, and monitored using **Prometheus and Grafana**.

This project demonstrates **end-to-end backend engineering**, **Kubernetes-native autoscaling**, **metrics-driven scaling decisions**, and **cluster observability** — following real-world DevOps and SRE practices.

---

## 🧱 Architecture Overview

**Flow:**
FastAPI Application → Docker Container → Kubernetes Deployment → HPA (CPU Metrics) → Prometheus → Grafana Dashboards

**Key Capabilities:**

* RESTful backend mimicking GenAI behavior
* Containerized and portable application
* Kubernetes deployment with Service & HPA
* Automatic scale-up and scale-down based on CPU usage
* Full observability using Prometheus metrics and Grafana dashboards

---

## 🧪 Step 1: Backend Development (FastAPI)

The backend is implemented using **FastAPI** and simulates GenAI-like behavior using mock responses.

### Run the application locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Access the Swagger UI:

```
http://localhost:8000/docs
```

### Available Endpoints

* `/health` → Health check endpoint (returns `ok`)
* `/generate` → Simulated GenAI response endpoint

The successful response from `/health` confirms the backend is running correctly.

---

## 🐳 Step 2: Containerization with Docker

The application is containerized using a **Dockerfile** provided in the repository.

### Build Docker Image

```bash
docker build -t hrushikesh2k1/genai-service:v1 .
```

### Run Docker Container

```bash
docker run -d -p 8000:8000 -e USE_MOCK_AI=true hrushikesh2k1/genai-service:v1
```

The application will now be accessible at:

```
http://localhost:8000
```

---

## ☸️ Step 3: Kubernetes Deployment & Autoscaling

The application is deployed on a **local Kubernetes cluster (Docker Desktop)**.

### Kubernetes Manifests

The `k8s/` directory contains:

* `deployment.yaml` → Application Deployment
* `service.yaml` → NodePort Service
* `hpa.yaml` → Horizontal Pod Autoscaler (CPU-based)

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### Horizontal Pod Autoscaler (HPA)

* Autoscaling is based on **CPU utilization**
* Metrics are provided by **metrics-server**
* HPA dynamically adjusts replicas based on load

### Load Testing HPA

Generate continuous load to trigger scaling:

Use the load-test.sh script and observe the CPU usage metrics.

### Observations

* Pods scale **up automatically** as CPU usage increases
* Pods scale **down gradually** after CPU stabilizes (cooldown period)
* Demonstrates real-world HPA stabilization behavior

---

## 📊 Step 4: Monitoring with Prometheus & Grafana

Monitoring is implemented using the **kube-prometheus-stack** via **Helm**.

### Install Prometheus & Grafana

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```

### Access Grafana

Port-forward Grafana service:

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

Grafana will be available at:

```
http://localhost:3000
```

---

## 📈 Grafana Dashboards

### Pod Metrics Dashboard

* **Dashboard ID:** `15757`
* Visualizes CPU, memory, and pod-level metrics

### HPA Metrics Dashboard

* **Dashboard ID:** `22128`
* Visualizes desired vs current replicas
* Shows scaling behavior and CPU targets

These dashboards provide clear visibility into:

* Resource usage
* Autoscaling decisions
* Kubernetes workload behavior

---

## Step 5: 🚀 CI/CD with Docker, GitHub Actions & Helm

This project implements a realistic CI/CD workflow for a Kubernetes-based application using Docker, GitHub Actions, and Helm.

🔁 CI: Continuous Integration (Build & Publish)
Objective
Automate the process of:

  Building the application image
  Versioning it immutably
  Publishing it to a container registry

Implementation

A GitHub Actions workflow is triggered on every push to the main branch. The CI pipeline performs the following steps:
  Checkout source code
  Build Docker image using Docker Buildx
  Tag the image with the Git commit SHA
  Push the image to Docker Hub

📦 Helm for Application Packaging

The Kubernetes manifests (Deployment, Service, HPA) are packaged into a Helm chart, which provides:

  Parameterization via values.yaml
  Clean separation of configuration and templates
  Release versioning and rollback support

Key configurable values:

Docker image repository and tag
Resource requests and limits
HPA configuration (min/max replicas, CPU target)
Service type and ports

🔄 Release Management & Rollbacks

Helm enables full release lifecycle management:

Install / Upgrade
```bash
helm upgrade --install genai helm
```
View release history
```bash
helm history genai
```
Rollback to a previous version
```bash
helm rollback genai <REVISION>
```

This provides production-grade safety during deployments.

## Key-Take aways!

* Built a production-style backend using FastAPI
* Containerized applications for portability
* Deployed and exposed workloads on Kubernetes
* Implemented CPU-based HPA using metrics-server
* Observed real-time autoscaling behavior
* Implemented full observability using Prometheus & Grafana

---

## 🚀 Future Enhancements

* Custom metrics-based HPA using Prometheus Adapter
* Ingress setup with NGINX
* Load testing using k6 or Locust
* Real GenAI model integration
* CI/CD pipeline using GitHub Actions

---

## 👤 Author

**Hrushikesh**
DevOps Engineer | Kubernetes | Cloud | Observability

---

⭐ If you find this project useful, consider giving it a star!

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3c58715c-b7a9-4146-9c42-e9f892c7d308" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4bd7ea63-fe6c-4706-bedb-ea66c43f57d5" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/66551076-584a-4a61-9d94-2a267e3341e5" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f03df922-fcb8-4d06-ac13-86494892d19f" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/83ac0c16-70d6-40c6-92cb-a7a6f2b53773" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5dfaca69-b9e5-43ab-aa4d-70b857250a4e" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/29c71489-1f82-4d78-b3ba-8468e726aa3e" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d2dc9ac7-eff2-48e4-8444-1b8385805632" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3e8d883f-806a-4c69-8a32-b717f3376d73" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/57d93314-9c6a-41a1-aab5-8528e2282140" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7927d241-8fd1-43fc-b811-ae78735cc3c4" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/928d5fc6-3f7b-452b-880e-2b0fc2221be2" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c7aeeb9b-b6f5-4e50-908d-b9a8b424f640" />

