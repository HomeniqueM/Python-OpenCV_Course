import cv2 as cv 

path_image = '../../resources/images/Ghibli_Park.jpg'

img = cv.imread(path_image)

## Show image in a windows
cv.imshow('Image window', img)


def rescaleFrame(frame,scale =0.75):
    height = int(frame.shape[0]* scale)
    width  = int(frame.shape[1]* scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


# By default
cv.imshow('Image Rescale default', rescaleFrame(img))

# Rescales the image to 20% of the original size
cv.imshow('Image Rescale 20%', rescaleFrame(img,scale=0.20))





## Waits a certain amount of time to be able to press a key
# 0 = infinite 
#cv.destroyAllWindows()
cv.waitKey(0)

