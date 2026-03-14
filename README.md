# ai-devops-autohealing-platform

AI DevOps Auto-Healing Platform (AIOps System) using Kubernetes, Docker, Jenkins, Prometheus, Grafana and AI log analysis

🚀 AI DevOps Auto-Healing Platform



An AI-driven DevOps platform that monitors a Kubernetes-based application using Prometheus and Grafana, detects anomalies in system metrics, and automatically performs recovery actions using Kubernetes APIs.



This project demonstrates real-world DevOps practices including containerization, monitoring, observability, and self-healing infrastructure.



📌 Project Overview



Modern cloud systems require automated monitoring and recovery mechanisms. This project implements an AI-powered monitoring and auto-healing system that detects abnormal behavior in application metrics and automatically restores system health.



The platform integrates:



Spring Boot microservice



Docker containerization



Kubernetes orchestration



Prometheus monitoring



Grafana dashboards



AI-based anomaly detection using Python



Automated self-healing using Kubernetes API



🏗 System Architecture



User Request

↓

Spring Boot Application

↓

Docker Container

↓

Kubernetes Deployment (Multiple Pods)

↓

Prometheus Metrics Collection

↓

Grafana Monitoring Dashboard

↓

AI Analysis Service (FastAPI)

↓

Anomaly Detection

↓

Kubernetes API

↓

Auto-Healing (Restart/Recover Pods)



🛠 Tech Stack



Backend

• Spring Boot (Java)



Containerization

• Docker



Container Orchestration

• Kubernetes



Monitoring

• Prometheus



Visualization

• Grafana



AI \& Automation

• Python

• FastAPI

• NumPy / Scikit-learn



Infrastructure

• Kubernetes Services

• Kubernetes Deployments



⚙️ Key Features

1️⃣ Containerized Microservice



The application is packaged using Docker to ensure consistent runtime environments across development and deployment.



2️⃣ Kubernetes Deployment



The system uses Kubernetes deployments to run multiple replicas of the application for high availability.



3️⃣ Monitoring with Prometheus



Prometheus collects real-time metrics such as CPU usage, memory usage, and container health.



4️⃣ Visualization with Grafana



Grafana dashboards provide real-time visualization of cluster and application performance.



5️⃣ AI-Based Anomaly Detection



A Python FastAPI service reads metrics from Prometheus and analyzes CPU usage patterns to detect anomalies.



6️⃣ Self-Healing Infrastructure



When an anomaly is detected, the AI service triggers Kubernetes API calls to restart unhealthy pods automatically.



📊 Monitoring Dashboard



Grafana provides real-time dashboards for:



• CPU Usage

• Memory Usage

• Node Performance

• Pod Health



Example dashboard:



Add screenshot here



🧠 AI Anomaly Detection Logic



The AI service periodically queries Prometheus metrics and applies anomaly detection.



Example logic:



If CPU usage > 80%

→ Anomaly detected

→ Restart affected pods



🚀 How to Run the Project

Step 1: Build Application Container



docker build -t application-service .



Step 2: Deploy Application to Kubernetes



kubectl apply -f kubernetes/deployment.yaml

kubectl apply -f kubernetes/service.yaml



Step 3: Deploy Monitoring Stack



helm install monitoring prometheus-community/kube-prometheus-stack



Step 4: Deploy AI Analysis Service



kubectl apply -f kubernetes/ai-analysis-deployment.yaml

kubectl apply -f kubernetes/ai-analysis-service.yaml



Step 5: Access Grafana



kubectl port-forward service/monitoring-grafana 3000:80



Open:



http://localhost:3000



Step 6: Run AI Health Analysis



kubectl port-forward service/ai-analysis-service 8001:8000



Open:



http://localhost:8001/analyze



Example response:



{"status":"system healthy"}



📂 Project Structure



ai-devops-autohealing-platform

│

├── application-service

│ ├── Spring Boot application

│

├── ai-analysis-service

│ ├── AI anomaly detection service

│

├── kubernetes

│ ├── Kubernetes deployment files

│

├── monitoring

│ ├── Prometheus and Grafana setup

│

├── infrastructure

│ ├── Infrastructure configurations

│

├── cicd

│ ├── CI/CD configurations

│

└── README.md



📈 Future Improvements



• AI-driven auto-scaling using Kubernetes HPA

• ML-based failure prediction

• Slack / Email alert integration

• Advanced anomaly detection models



🎯 Learning Outcomes



Through this project I gained hands-on experience with:



• Kubernetes orchestration

• Docker containerization

• DevOps monitoring tools

• AI-driven infrastructure automation

• Cloud-native application architecture



👨‍💻 Author



Harika Rajani

AI | Cloud | DevOps Enthusiast

