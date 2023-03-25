import cv2
import pytesseract
from PIL import Image


image = cv2.imread('/home/pi/Desktop/truck_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


image = cv2.imread()



