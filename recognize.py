import cv2
import numpy as np
import os
from PIL import Image

# Load recognizer and trained data
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Load the Haar cascade for face detection
cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# ID and name mapping (change this as needed)
names = ['None', 'Sanjay']  # ID 0 is 'None', ID 1 is 'Sanjay'

# Open webcam
cam = cv2.VideoCapture(0)

print("[INFO] Starting face recognition. Press 'ESC' to exit.")

while True:
    ret, img = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 60:
            name = names[1]  # 'Sanjay'
            confidence_text = f"{round(100 - confidence)}%"
        else:
            name = "Unknown"
            confidence_text = f"{round(100 - confidence)}%"

        # Draw rectangle and name
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, str(name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence_text), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

    cv2.imshow('Face Recognition', img)

    # Press ESC to exit
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Cleanup
print("[INFO] Exiting...")
cam.release()
cv2.destroyAllWindows()
