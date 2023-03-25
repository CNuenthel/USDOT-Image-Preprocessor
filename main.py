import cv2
import pytesseract
from PIL import Image
import random

# Install Tesseract OCR from here:
# https://github.com/UB-Mannheim/tesseract/wiki#windows

# Load the image and preprocess it
image = cv2.imread('truck_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Save the preprocessed image
# cv2.imwrite(f"processed/saved_image.jpg", thresh)

usdot_number = pytesseract.image_to_string(Image.open(f"processed/saved_image.jpg"))

print(usdot_number)



