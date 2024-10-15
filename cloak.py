import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
time.sleep(3)

background = 0
for i in range(30):
    ret, background = video.read()

background = np.flip(background, axis=1)

while True:
    ret, img = video.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.medianBlur(hsv, 51)  # Try median blur with a larger kernel size

    lower = np.array([0, 120, 70])
    upper = np.array([10, 255, 255])
    mask01 = cv2.inRange(hsv, lower, upper)

    lower_red = np.array([0, 100, 100])  # Lower range for red color
    upper_red = np.array([10, 255, 255])  

    mask02 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask01 + mask02
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))  # Increase kernel size
    _, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)  # Apply threshold to mask
    img[np.where(thresh == 255)] = background[np.where(thresh == 255)]

    cv2.imshow("Display", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()