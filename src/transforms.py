"""Basic 4x4 transformation matrices for graphics experiments."""
from __future__ import annotations
import math
import numpy as np

def translation(x: float, y: float, z: float) -> np.ndarray:
    matrix = np.eye(4)
    matrix[:3, 3] = [x, y, z]
    return matrix

def scale(x: float, y: float, z: float) -> np.ndarray:
    return np.diag([x, y, z, 1.0])

def rotation_z(degrees: float) -> np.ndarray:
    angle = math.radians(degrees)
    c, s = math.cos(angle), math.sin(angle)
    return np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float)

def transform_point(matrix: np.ndarray, point) -> np.ndarray:
    homogeneous = np.append(np.asarray(point, dtype=float), 1.0)
    return (matrix @ homogeneous)[:3]

if __name__ == "__main__":
    model = translation(1, 2, 3) @ rotation_z(30) @ scale(2, 2, 2)
    print(transform_point(model, [1, 0, 0]))
