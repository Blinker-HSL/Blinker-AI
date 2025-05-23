import numpy as np

def get_EAR(landmarks, eye_idx, image_w, image_h):
    p = [landmarks[i] for i in eye_idx]
    p = [(int(p.x * image_w), int(p.y * image_h)) for p in p]

    A = np.linalg.norm(np.array(p[1]) - np.array(p[5]))
    B = np.linalg.norm(np.array(p[2]) - np.array(p[4]))
    C = np.linalg.norm(np.array(p[0]) - np.array(p[3]))
    ear = (A + B) / (2.0 * C)
    return ear