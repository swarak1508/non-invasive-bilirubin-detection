import cv2
import numpy as np
import sys

# =========================
# Load image
# =========================
if len(sys.argv) < 2:
    raise Exception("Usage: python main.py <image_path>")

image_path = sys.argv[1]

img = cv2.imread(image_path)
if img is None:
    raise Exception("Image not found or invalid path")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# =========================
# Face Detection
# =========================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

if len(faces) == 0:
    raise Exception("No face detected")

x, y, w, h = faces[0]
face = img[y:y+h, x:x+w]

# =========================
# Feature Extraction (YCbCr)
# =========================
ycbcr = cv2.cvtColor(face, cv2.COLOR_RGB2YCrCb)
y, cr, cb = cv2.split(ycbcr)

features = np.array([[np.mean(y), np.mean(cr), np.mean(cb)]])

# =========================
# Prediction (ML or fallback)
# =========================
try:
    import joblib
    model = joblib.load("model/bilirubin_model.pkl")
    bilirubin = model.predict(features)[0]
except:
    bilirubin = (np.mean(cr) - np.mean(cb)) / 10

# Safety clamp
bilirubin = max(0, min(bilirubin, 25))

# =========================
# Output
# =========================
print("\n==============================")
print("NON-INVASIVE BILIRUBIN SYSTEM")
print("==============================")
print(f"Estimated Bilirubin: {bilirubin:.2f} mg/dL")
