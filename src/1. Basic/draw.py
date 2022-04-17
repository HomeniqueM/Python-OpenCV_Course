import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank Image', blank)
    
# 1. Paint the image a certain colour
    # 1.1 All image

blank[:] = 0,0,255
cv.imshow('Full Red', blank)

blank[:] = 0,0,0
    # 1.2 certain part
blank[200:300, 300:400] = 0,255,0
cv.imshow('Partial Green', blank)

blank[:] = 0,0,0
#2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness =2 )
cv.imshow('Rectangle', blank)
blank[:] = 0,0,0
    #or -1 = Filled
cv.rectangle(blank, (0,250), (blank.shape[1]//2,blank.shape[0]), (0,255,0), thickness =cv.FILLED )
cv.imshow('Filled rectangle ', blank)

#3. Draw a circle

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness =3)
cv.imshow('Circle ', blank)
blank[:] = 0,0,0

#or -1 = Filled
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness =-1)
cv.imshow('Filled circle ', blank)


# 4. Draw Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness=3)
cv.imshow('Line ', blank)
blank[:] = 0,0,0
# 5. Write Text
cv.putText(blank, 'Hello', (225,255), (cv.FONT_HERSHEY_TRIPLEX), 1.0, (0,255,0), thickness=2)

cv.imshow('Text in blank image ', blank)

cv.waitKey(0)