# 🧪 Non-Invasive Bilirubin Detection using Image Processing

## 📌 Overview
This project presents a simple, non-invasive method to estimate bilirubin levels using image processing techniques. By analyzing the RGB values of a facial image, the system provides a rough estimation of bilirubin concentration.

⚠️ **Disclaimer:** This is an educational prototype and NOT a clinically approved diagnostic tool.

---

## 🎯 Objective
To develop a low-cost, non-invasive approach for bilirubin estimation using digital image analysis, eliminating the need for blood sampling.

---

## ⚙️ Methodology

1. Image is loaded and converted to RGB format  
2. Pixel values are extracted from the image  
3. Average RGB values are calculated  
4. A heuristic formula is applied to estimate bilirubin levels  
5. The result is compared with standard reference ranges (WHO & CMRR)

---

## 🧠 Working Principle

- Higher bilirubin levels often give a yellowish tint to the skin  
- Yellow color = High Red + Green, Low Blue  
- The model uses this relationship to estimate bilirubin  
## 📊 Bilirubin Estimation Formula


Bilirubin ≈ ((R + G) / 2 - B) / 255 × 20


- Output range: **0 – 20 mg/dL**
- This is a **heuristic model**, not medically validated

---

## 📁 Project Structure


non-invasive-bilirubin-detection/
│
├── main.py # Main Python script
├── requirements.txt # Required libraries
├── README.md # Project documentation
├── sample_images/ # Input images
│ └── sample.jpg
└── outputs/ # Output screenshots
└── output.png


---

## 💻 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
▶️ How to Run
Place your image inside sample_images/
Update the image path in main.py if needed
Run:
python main.py
📷 Sample Output
Displays input image
Prints average RGB values
Outputs estimated bilirubin level
Classifies as Normal/Abnormal

(Add your screenshot in the outputs folder and link here if needed)

📚 Reference Ranges Used
Standard	Normal Range (mg/dL)
WHO	0.3 – 1.2
CMRR	0.2 – 1.0
🚀 Future Improvements
Face detection for accurate ROI extraction
Machine Learning model for better prediction
Mobile app integration
Real-time camera-based analysis
Clinical dataset validation
🧑‍💻 Author

Swara K
Biomedical Electronics Engineering Student

⭐ Acknowledgment

This project was developed as part of a biomedical engineering learning initiative focused on non-invasive diagnostic techniques.

⚠️ Disclaimer

This project is intended strictly for educational and research purposes.
It should not be used for medical diagnosis or treatment decisions.
---

## 📊 Bilirubin Estimation Formula
