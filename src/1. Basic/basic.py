import cv2 as cv 

img = cv.imread('../../resources/images/calibration.jpg')

## Show image in a windows
cv.imshow('calibration.jpg', img)

# Converting to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

cv.waitKey(0)
