import cv2
import mediapipe as mp
from utils.eye_landmark import get_EAR

mp_face_mesh = mp.solutions.face_mesh
LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]  # 좌안
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]  # 우안

def process_image(image_path):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            left_ear = get_EAR(landmarks, LEFT_EYE_IDX, w, h)
            right_ear = get_EAR(landmarks, RIGHT_EYE_IDX, w, h)
            return (left_ear + right_ear) / 2
    return None