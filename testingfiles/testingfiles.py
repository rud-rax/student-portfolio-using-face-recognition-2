import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh


print("ok")
print("DTYPE of mp_face_mesh --> ", type(mp_face_mesh))
print("DTYPE of mp_drawing --> ", type(mp_drawing))
print("DTYPE of mp_drawing_styles --> ", type(mp_drawing_styles))
