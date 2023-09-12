# USDOT-Image-Preprocessor
Preprocesses images to output text for USDOT numbers

Simple script that will take an image input and utilize pytesseract and cv2 libraries to preprocess the image and sequentially scan image data for textual markers. If a textual marker matches the phrase "DOT", the textual marker will be read and returned using computer vision recognition of alphanumeric characters. Test part of my USDOT computer vision reader. 
