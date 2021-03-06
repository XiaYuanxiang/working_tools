# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np
import matplotlib.pyplot as plot


frame0 = np.zeros((1200, 900, 3), np.uint8)
num0 = 0
bright0 = 60.0
contrast0 = 50.0
saturation0 = 70.0
cap0 = cv2.VideoCapture(0)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)
cap0.set(cv2.CAP_PROP_CONTRAST, 1)
cap0.set(cv2.CAP_PROP_BRIGHTNESS, 1)
cap0.set(cv2.CAP_PROP_SATURATION, 1)

frame1 = np.zeros((1200, 900, 3), np.uint8)
num1 = 0
bright1 = 60.0
contrast1 = 50.0
saturation1 = 70.0
cap1 = cv2.VideoCapture(1)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)
cap1.set(cv2.CAP_PROP_CONTRAST, 1)
cap1.set(cv2.CAP_PROP_BRIGHTNESS, 1)
cap1.set(cv2.CAP_PROP_SATURATION, 1)



def nothing(x):
    pass

cv2.namedWindow("imshow0")
cv2.createTrackbar('BRIGHTNESS0', 'imshow0', 60, 100, nothing)
cv2.createTrackbar('CONTRAST0', 'imshow0', 50, 100, nothing)
cv2.createTrackbar('SATURATION0', 'imshow0', 70, 100, nothing)

cv2.namedWindow("imshow1")
cv2.createTrackbar('BRIGHTNESS1', 'imshow1', 60, 100, nothing)
cv2.createTrackbar('CONTRAST1', 'imshow1', 50, 100, nothing)
cv2.createTrackbar('SATURATION1', 'imshow1', 70, 100, nothing)

# def save_img(event, x, y, flags, param):
def save_img0(event, x, y, flags, param):

    global frame0
    global num0
    global cap0


    if event == cv2.EVENT_LBUTTONDBLCLK:
        num0 += 1
        cv2.imwrite("num_detect_" + str(num0) + ".jpg", frame0)



def save_img1(event, x, y, flags, param):

    global frame1
    global num1
    global cap1

    if event == cv2.EVENT_LBUTTONDBLCLK:
        num1 += 1
        cv2.imwrite("huogui_" + str(num1) + ".jpg", frame1)

while(1):

    bright0 = bright0 / 80.0
    contrast0 = contrast0 / 80.0
    saturation0 = saturation0 / 80.0

    cap0.set(cv2.CAP_PROP_BRIGHTNESS, bright0)
    cap0.set(cv2.CAP_PROP_CONTRAST, contrast0)
    cap0.set(cv2.CAP_PROP_SATURATION, saturation0)

    ret0, frame0 = cap0.read()
    id = 0
    cv2.setMouseCallback('imshow0', save_img0)
    cv2.imshow("imshow0", frame0)

    bright0 = cv2.getTrackbarPos('BRIGHTNESS0', 'imshow0')
    contrast0 = cv2.getTrackbarPos('CONTRAST0', 'imshow0')
    saturation0 = cv2.getTrackbarPos('SATURATION0', 'imshow0')

    bright1 = bright1 / 80.0
    contrast1 = contrast1 / 80.0
    saturation1 = saturation1 / 80.0

    cap1.set(cv2.CAP_PROP_BRIGHTNESS, bright1)
    cap1.set(cv2.CAP_PROP_CONTRAST, contrast1)
    cap1.set(cv2.CAP_PROP_SATURATION, saturation1)

    ret1, frame1 = cap1.read()
    cv2.setMouseCallback('imshow1', save_img1)
    cv2.imshow("imshow1", frame1)

    bright1 = cv2.getTrackbarPos('BRIGHTNESS1', 'imshow1')
    contrast1 = cv2.getTrackbarPos('CONTRAST1', 'imshow1')
    saturation1 = cv2.getTrackbarPos('SATURATION1', 'imshow1')


    # print bright, contrast, saturation

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap0.release()
cap1.release()
cv2.destroyAllWindows()
