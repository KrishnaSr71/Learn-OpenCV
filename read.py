# Import OpenCV
import cv2 as cv

# Reading Images: Create a reference to an image, and convert it into a matrix of pixels
img = cv.imread('Photos/Untitled.png')
cv.imshow('Give me your soul', img)

# Reading Videos: Create a reference to a specific video, and convert it into a readable format
capture = cv.VideoCapture('Videos/1.mp4')
while True:                                     # Keep looping through every frame in the video and convert into a matrix of pixels
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):        # Only breakout when a key is pressed after 20 seconds or if d is pressed
        break

# Reading Webcam: Create a reference to your webcam (0 is your first webcam, 1 is your second, etc.), and convert it into a readable format
webCam = cv.VideoCapture(1)
while True:
    isTrue, f = webCam.read()
    cv.imshow('Video', f)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

webCam.release()
cv.destroyAllWindows()

# commit to test branch





