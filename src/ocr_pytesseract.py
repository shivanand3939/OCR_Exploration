import cv2
import sys
import pytesseract
impath='/content/ocr2.png'
config = ('-l eng --oem 1 --psm 3')
# Read image from disk
im = cv2.imread(impath, cv2.IMREAD_COLOR)
text = pytesseract.image_to_string(im, config=config)
print(text)
