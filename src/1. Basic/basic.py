import cv2 as cv 

img = cv.imread('../../resources/images/paris-Test.jpg')

## Show image in a windows
cv.imshow('paris-Test.jpg', img)

# Converting to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur 3x3', blur)
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur 7x7', blur)

# Edge Cascade 
canny = cv.Canny(img, 125, 175)

cv.imshow('Canny Edges ', canny)

cannyblur = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges with blur', cannyblur)
cv.waitKey(0)
