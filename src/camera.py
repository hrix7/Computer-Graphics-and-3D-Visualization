"""Camera matrices that reproduce the view setup used in my graphics exercises."""
from __future__ import annotations
import math
import numpy as np

def look_at(eye, target, up=(0.0, 1.0, 0.0)) -> np.ndarray:
    eye = np.asarray(eye, dtype=float)
    target = np.asarray(target, dtype=float)
    up = np.asarray(up, dtype=float)
    forward = target - eye
    if np.linalg.norm(forward) == 0:
        raise ValueError("eye and target cannot be identical")
    forward /= np.linalg.norm(forward)
    right = np.cross(forward, up)
    if np.linalg.norm(right) == 0:
        raise ValueError("up cannot be parallel to the view direction")
    right /= np.linalg.norm(right)
    corrected_up = np.cross(right, forward)
    view = np.eye(4)
    view[:3, :3] = np.vstack([right, corrected_up, -forward])
    view[:3, 3] = -view[:3, :3] @ eye
    return view

def perspective(vertical_fov_degrees: float, aspect: float,
                near: float, far: float) -> np.ndarray:
    if not (0 < vertical_fov_degrees < 180 and aspect > 0 and 0 < near < far):
        raise ValueError("Invalid projection parameters")
    f = 1.0 / math.tan(math.radians(vertical_fov_degrees) / 2.0)
    return np.array([[f / aspect, 0, 0, 0], [0, f, 0, 0],
                     [0, 0, (far + near) / (near - far), 2 * far * near / (near - far)],
                     [0, 0, -1, 0]], dtype=float)

if __name__ == "__main__":
    print("View matrix:\n", look_at([3, 2, 5], [0, 0, 0]))
    print("Projection matrix:\n", perspective(45, 16 / 9, 0.1, 100))
