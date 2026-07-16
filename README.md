# Non-Invasive Bilirubin Detection using Facial Image Processing

## Overview

This project presents a prototype for the non-invasive estimation of bilirubin levels using facial image processing techniques. The system detects the facial region, extracts color-based features in the YCbCr color space, and estimates bilirubin levels using image processing and color analysis.

This project was developed for academic purposes as part of the Medical Electronics Engineering curriculum and demonstrates the application of computer vision in biomedical engineering.

---

## Features

- Facial image acquisition
- Automatic face detection using OpenCV Haar Cascade
- Region of Interest (ROI) extraction
- RGB to YCbCr color space conversion
- Extraction of Y, Cr and Cb color features
- Bilirubin level estimation using color analysis
- Simple command-line execution

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Pillow
- Matplotlib

---

## Project Workflow

1. Load the input facial image.
2. Detect the face using OpenCV Haar Cascade.
3. Extract the facial Region of Interest (ROI).
4. Convert the ROI from RGB to YCbCr color space.
5. Extract the mean Y, Cr and Cb values.
6. Estimate the bilirubin level using the extracted color features.
7. Display the estimated bilirubin level.

---

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## How to Run

Place the input image in the project folder and run:

```bash
python main.py test.jpg
```

Replace `test.jpg` with the name of your input image.

---

## Sample Output

Example console output:

```text
==============================
NON-INVASIVE BILIRUBIN SYSTEM
==============================
Estimated Bilirubin: 2.45 mg/dL
```

*The value shown above is only a sample output for demonstration purposes.*

---

## Privacy Notice

To protect participant privacy and identity, no identifiable facial images used during testing have been included in this repository. Only the project code and documentation are shared.

---

## Limitations

- The estimation is based on image processing and color analysis and is intended for academic demonstration purposes.
- Performance may vary depending on lighting conditions, camera quality and image resolution.
- The system is not intended for clinical diagnosis or medical decision-making.
- Clinical validation with real patient data is beyond the scope of this project.

---

## Future Scope

- Improve robustness under different lighting conditions.
- Enhance face and skin region extraction techniques.
- Validate the approach using a larger clinical dataset.
- Develop a mobile application for non-invasive bilirubin estimation.

---

## Repository Contents

```text
README.md
main.py
requirements.txt
non-invasive-bilirubin-detection.ipynb
```

---

## Author

**Swara K**  
Medical Electronics Engineering  
Dayananda Sagar College of Engineering
