import cv2 as cv 

img = cv.imread('../../resources/images/calibration.jpg')

## Show image in a windows
cv.imshow('Image window', img)

## Waits a certain amount of time to be able to press a key
# 0 = infinite 
cv.waitKey(0)



# Reading Videos 

#capture = cv.VideoCapture('path/')

#while True:
#    isTrue, frame = capture.read()
#    cv,imshow ('Video',frame)

    # 
#    if cv.waitKey(20) & 0xFF ==ord('d'):
#        break

#apture.release()
#cv.destroyAllWindows()
#cv.waitKey(0)