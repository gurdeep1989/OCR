# convert pdf to images

import pdf2image

from pdf2image import convert_from_path
pages = convert_from_path('C:/Users/gurdd/Desktop/ml/opencv/CertificateOfCompletion_Excel.pdf', 500)

for page in pages:
    page.save('C:/Users/gurdd/Desktop/ml/opencv/out.jpg', 'JPEG')
 
###############################################################################
    
# crop the image to the area where there is signature       
import cv2

img = cv2.imread('C:/Users/gurdd/Desktop/ml/opencv/out.jpg',0)
y= 2000
x=1500
h=350
w=1000
crop = img[y:y+h, x:x+w]

cv2.imshow('Image', crop)
cv2.waitKey(0)

###############################################################################

# see if there is any dots in the image
th, threshed = cv2.threshold(crop, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2] 

s1 = 3
s2 = 20
xcnts = [] 
  
for cnt in cnts: 
    if s1<cv2.contourArea(cnt) <s2: 
        xcnts.append(cnt) 
 
# printing output 
print("\nDots number: {}".format(len(xcnts)))

###############################################################################

# Convert the image into text

import pytesseract
    
from PIL import Image
import PIL.Image

#download below from : https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows 
# Windows Installer made with MinGW-w64 (4.0.0-alpha for Windows)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('C:/Users/gurdd/Desktop/ml/opencv/out.jpg').convert("RGB"), lang='eng')
print(output)

