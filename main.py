from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload Image
uploaded = files.upload()

# Step 2: Load Image
image_path = next(iter(uploaded))
img = Image.open(image_path).convert('RGB')
plt.imshow(img)
plt.title("Uploaded Image")
plt.axis('off')
plt.show()

# Step 3: Calculate Average RGB
rgb_array = np.array(img)
avg_rgb = rgb_array.mean(axis=(0, 1))
avg_r, avg_g, avg_b = avg_rgb
print(f"\nAverage RGB values:\nR: {avg_r:.2f}, G: {avg_g:.2f}, B: {avg_b:.2f}")

# Step 4: Simple Estimation of Bilirubin from RGB
# Example mapping: higher bilirubin often correlates with yellow tint (high R+G, low B)
# This is a naive heuristic and **NOT** clinically accurate
bilirubin_level = ((avg_r + avg_g) / 2 - avg_b) / 255 * 20  # scaled to max ~20 mg/dL
bilirubin_level = max(0, min(bilirubin_level, 20))  # clamp to realistic range

print(f"\nEstimated Bilirubin Level: {bilirubin_level:.2f} mg/dL")

# Step 5: WHO and CMRR reference comparison
who_normal = (0.3, 1.2)
cmrr_normal = (0.2, 1.0)

def check_range(level, normal_range):
    return normal_range[0] <= level <= normal_range[1]

print("\nBilirubin Level Classification:")
print(f"WHO Normal Range: {who_normal[0]}–{who_normal[1]} mg/dL => {'Normal' if check_range(bilirubin_level, who_normal) else 'Abnormal'}")
print(f"CMRR Normal Range: {cmrr_normal[0]}–{cmrr_normal[1]} mg/dL => {'Normal' if check_range(bilirubin_level, cmrr_normal) else 'Abnormal'}")
