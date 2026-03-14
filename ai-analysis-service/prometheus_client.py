import requests

PROMETHEUS_URL = "http://monitoring-kube-prometheus-prometheus:9090"

def get_cpu_usage():

    query = 'rate(container_cpu_usage_seconds_total{pod=~"application-service.*"}[1m])'

    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )

    data = response.json()

    results = data["data"]["result"]

    cpu_values = []

    for r in results:
        cpu_values.append(float(r["value"][1]))

    return cpu_values