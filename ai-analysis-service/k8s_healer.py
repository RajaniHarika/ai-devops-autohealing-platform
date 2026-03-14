from kubernetes import client, config

def restart_pod():

    config.load_incluster_config()

    v1 = client.CoreV1Api()

    pods = v1.list_namespaced_pod(namespace="default")

    for pod in pods.items:

        if "application-service" in pod.metadata.name:

            print("Restarting pod:", pod.metadata.name)

            v1.delete_namespaced_pod(
                name=pod.metadata.name,
                namespace="default"
            )