import cv2
import time
import numpy as np
import matplotlib.pyplot as plot


standard = 128
def get_avg_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    avg = cv2.mean(img)
    return avg


img = cv2.imread("1.jpg")
cv2.imshow("img", img)
avg = get_avg_gray(img)
bright = standard / avg[0]

print avg
cv2.waitKey(0)