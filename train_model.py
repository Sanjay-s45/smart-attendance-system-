import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = 'dataset/sanjay_s'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')  # grayscale
        imageNp = np.array(pilImage, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[0]) 
        faces = detector.detectMultiScale(imageNp)

        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("\n[INFO] Training faces. It will take a few seconds. Wait ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the trained model
if not os.path.exists('trainer'):
    os.makedirs('trainer')
recognizer.write('trainer/trainer.yml')

print(f"\n[INFO] {len(np.unique(ids))} faces trained. Exiting Program.")
