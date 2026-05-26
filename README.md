# AI DevOps Auto-Healing Platform 🚀

## Project Overview

This project is an AI-powered DevOps Auto-Healing Platform built using modern DevOps and Cloud Native tools.

The platform demonstrates:

* CI/CD automation
* Kubernetes self-healing
* Monitoring & observability
* Auto-scaling
* Containerized deployment

---

## Tech Stack

* Java
* Spring Boot
* Docker
* Kubernetes
* Jenkins
* Prometheus
* Grafana
* Minikube
* Git & GitHub

---

## Features

### ✅ CI/CD Pipeline

Implemented Jenkins pipeline for:

* automated build stages
* deployment workflow simulation
* DevOps automation

### ✅ Kubernetes Self-Healing

Kubernetes automatically restarts failed containers and maintains desired pod replicas.

### ✅ Monitoring & Observability

Integrated:

* Prometheus for metrics collection
* Grafana for dashboards and visualization

### ✅ Horizontal Pod Autoscaling (HPA)

Configured Kubernetes HPA for dynamic scaling based on CPU utilization.

### ✅ Docker Containerization

Application containerized using Docker for portability and deployment consistency.

---

## Project Architecture

GitHub → Jenkins → Docker → Kubernetes → Prometheus → Grafana

---

## Kubernetes Components Used

* Deployments
* Services
* Pods
* HPA
* Metrics Server

---

## Jenkins Pipeline Stages

1. Check Jenkins
2. Simulate Docker Build
3. Simulate Kubernetes Deployment
4. Final Pipeline Status

---

## Commands Used

### Build Docker Image

```bash
docker build -t ai-devops-app .
```

### Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Enable HPA

```bash
kubectl autoscale deployment application-service --cpu=50% --min=1 --max=5
```

---

## Monitoring Stack

### Prometheus

Used for:

* metrics scraping
* monitoring Kubernetes workloads

### Grafana

Used for:

* dashboard visualization
* real-time monitoring

---

## Future Enhancements

* AWS EKS Deployment
* Terraform Infrastructure as Code
* GitHub Webhooks
* AI-based anomaly detection
* Alertmanager integration
* Helm Charts
* GitOps with ArgoCD

---

## Author

Harika Rajani

GitHub:
https://github.com/RajaniHarika
