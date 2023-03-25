import cv2
import pytesseract


# PREPROCESS IMAGE FOR READABILITY

# Load Image
img = cv2.imread('base_images/truck_image4.jpg')

# Grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save Grayscale Image
cv2.imwrite("processed/gray_scale.jpeg", gray)

# Noise reduction
bfilter = cv2.bilateralFilter(gray, 5, 5, 5)

# ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# ______________________________________________________________________________________________________________________


# Edge detection
edged = cv2.Canny(bfilter, 30, 200)

# Save edged image with noise reduction
cv2.imwrite("processed/edged.jpeg", cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

# Detecting words
hImg, wImg = gray.shape

boxes = pytesseract.image_to_data(img)

data = boxes.splitlines()

for item in data:
    print(item)

found_data = [item.split() for item in data[1:] if len(item.split()) == 12]

for idx, data in enumerate(found_data):
    if data[11].upper() == "DOT" or data[11].upper() == "USDOT" :
        print(f"USDOT Number is: {found_data[idx+1][11]}")
        break

for idx, data in enumerate(boxes.splitlines()):
    if idx != 0:
        d = data.split()
        if len(d) == 12:
            x,y,w,h = int(d[6]), int(d[7]), int(d[8]), int(d[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
            # cv2.putText(img, d[0], (x, hImg-y+45), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2) # shows characters on image

cv2.imwrite("processed/boxed.jpeg", img)











# # Find rectangular contour
# keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(keypoints)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#
# # Check contours
# location = None
# count = 0
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 10, True) # approximate polygon from contour, (type, the higher-the rougher)
#     if len(approx) == 4:
#         location = approx
#
#         # Mask image
#         mask = np.zeros(gray.shape, np.uint8)
#         new_image = cv2.drawContours(mask, [location], 0, 255, -1)
#         new_image = cv2.bitwise_and(img, img, mask=mask)
#
#         # Save masked image
#         cv2.imwrite(f"processed/masked{count}.jpeg", cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
#         count += 1
