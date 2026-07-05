# Non-Invasive Bilirubin Estimation using Facial Image Processing

## Overview
This project estimates bilirubin levels from facial images using computer vision and machine learning techniques. It is a non-invasive approach that extracts color space features from the facial region and predicts bilirubin concentration.

---

## Methodology

1. Image Acquisition via smartphone or dataset
2. Face Detection using Haar Cascade (OpenCV)
3. Region of Interest (ROI) extraction
4. Color Space Conversion (RGB → YCbCr)
5. Feature Extraction (Y, Cr, Cb values)
6. Machine Learning-based regression model for bilirubin prediction
7. Clinical range comparison (WHO & CMRR standards)

---

## Features Used
- Y (Luminance)
- Cr (Chrominance Red)
- Cb (Chrominance Blue)

---

## Tech Stack
- Python
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn (for ML model)

---

## Limitations
- Sensitive to lighting conditions
- Requires controlled image capture
- Needs clinically labeled dataset for real-world accuracy

---

## Future Improvements
- Deep learning-based prediction model
- Real-time mobile application integration
- Dataset expansion with clinical validation

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
