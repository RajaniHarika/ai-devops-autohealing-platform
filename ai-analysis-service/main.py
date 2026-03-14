from fastapi import FastAPI
from prometheus_client import get_cpu_usage
from anomaly_detector import detect_anomaly
from k8s_healer import restart_pod

app = FastAPI()

@app.get("/analyze")

def analyze_system():

    cpu_values = get_cpu_usage()

    if detect_anomaly(cpu_values):

        restart_pod()

        return {"status": "auto-healing triggered"}

    return {"status": "system healthy"}