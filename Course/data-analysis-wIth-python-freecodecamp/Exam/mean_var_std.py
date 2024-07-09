import numpy as np

def calculate(list):
    if len(list) < 9 :
        raise ValueError("List must contain nine numbers.")

    data = np.array(list).reshape(3, 3)

    calculations = {
        "mean": [
            np.mean(data, axis=0).tolist(),
            np.mean(data, axis=1).tolist(),
            np.mean(data).tolist(),
        ],
        "variance": [
            np.var(data, axis=0).tolist(),
            np.var(data, axis=1).tolist(),
            np.var(data).tolist(),
        ],
        "standard deviation": [
            np.std(data, axis=0).tolist(),
            np.std(data, axis=1).tolist(),
            np.std(data).tolist(),
        ],
        "max": [
            np.max(data, axis=0).tolist(),
            np.max(data, axis=1).tolist(),
            np.max(data).tolist(),
        ],
        "min": [
            np.min(data, axis=0).tolist(),
            np.min(data, axis=1).tolist(),
            np.min(data).tolist(),
        ],
        "sum": [
            np.sum(data, axis=0).tolist(),
            np.sum(data, axis=1).tolist(),
            np.sum(data).tolist(),
        ],
    }
    return calculations