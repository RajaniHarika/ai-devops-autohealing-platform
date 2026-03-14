import numpy as np

def detect_anomaly(cpu_values):

    if len(cpu_values) == 0:
        return False

    avg_cpu = np.mean(cpu_values)

    print("Average CPU:", avg_cpu)

    if avg_cpu > 0.8:
        return True

    return False