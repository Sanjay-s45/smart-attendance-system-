import cv2
import os
import sys

name = sys.argv[1] if len(sys.argv) > 1 else input("Enter your name: ")

path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Capturing Faces", frame)

    if count % 5 == 0:
        filename = os.path.join(path, f"{name}_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
