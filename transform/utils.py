# transform/utils.py
import numpy as np

def convert_numpy_to_python(obj):
    """
    Recursively convert NumPy numeric types to Python native types
    so MongoDB can store them without errors.
    """
    if isinstance(obj, dict):
        return {k: convert_numpy_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_to_python(v) for v in obj]
    elif isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    else:
        return obj
