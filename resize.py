import cv2 as cv

def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/untitled.png')
newImage = rescaleFrame(img, 2)
cv.imshow('Resize', newImage)

cv.waitKey(0)