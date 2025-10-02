import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import os

# Load recognizer and Haar Cascade
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Define font
font = cv2.FONT_HERSHEY_SIMPLEX

# Define names by ID — edit as needed
names = ["None", "Sanjay"]

# Start video capture
cap = cv2.VideoCapture(0)

# Attendance file setup
file_name = 'attendance.csv'

# Create file if not exists
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(file_name, index=False)

def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    df = pd.read_csv(file_name)

    # Avoid duplicate entry for same person on same day
    if not ((df['Name'] == name) & (df['Date'] == date)).any():
        new_entry = pd.DataFrame([[name, date, time]], columns=["Name", "Date", "Time"])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(file_name, index=False)
        print(f"[INFO] Attendance marked for {name} at {time}")

print("[INFO] Starting face recognition with attendance. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        confidence_percent = round(100 - confidence)

        if confidence_percent >= 50:
            name = names[id]
            mark_attendance(name)
        else:
            name = "Unknown"

        # Draw results
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"{confidence_percent}%", (x+5, y+h-5), font, 1, (255, 255, 0), 1)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
