import Tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk
import tkMessageBox
import numpy






fileName = "/home/xia/working_tools" + "/WebcamCap.txt"
cancel = False
num = 0
standard = 128
idx_bright = 1.0
def get_avg_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    avg = cv2.mean(img)
    return avg

def prompt_ok(event = 0):
    global cancel, button, button1, button2
    cancel = True

    button.place_forget()
    button1 = tk.Button(mainWindow, text="Good Image!", command=saveAndExit)
    button2 = tk.Button(mainWindow, text="Try Again", command=resume)
    button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
    button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
    button1.focus()

def saveAndExit(event = 0):
    global prevImg
    global num
    num += 1
    if (len(sys.argv) < 2):
        filepath = str(num) + ".jpg"
    else:
        filepath = sys.argv[1]

    print ("Output file to: " + filepath)
    prevImg.save(filepath)
    mainWindow.quit()


def resume(event = 0):
    global button1, button2, button, lmain, cancel

    cancel = False

    button1.place_forget()
    button2.place_forget()

    mainWindow.bind('<Return>', prompt_ok)
    button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    lmain.after(10, show_frame)

def changeCam(event=0, nextCam=-1):
    global camIndex, cap, fileName

    if nextCam == -1:
        camIndex += 1
    else:
        camIndex = nextCam
    del(cap)
    cap = cv2.VideoCapture(camIndex)

    #try to get a frame, if it returns nothing
    success, frame = cap.read()
    if not success:
        camIndex = 0
        del(cap)
        cap = cv2.VideoCapture(camIndex)

    f = open(fileName, 'w')
    f.write(str(camIndex))
    f.close()

try:
    f = open(fileName, 'r')
    camIndex = int(f.readline())
except:
    camIndex = 0

camIndex = 0
cap = cv2.VideoCapture(camIndex)
# capWidth = cap.get(3)
# capHeight = cap.get(4)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

success, frame = cap.read()
if not success:
    if camIndex == 0:
        print("Error, No webcam found!")
        sys.exit(1)
    else:
        changeCam(nextCam=0)
        success, frame = cap.read()
        if not success:
            print("Error, No webcam found!")
            sys.exit(1)


def setContrast(var):
    global contrast
    # print contrast.get()
    var = float(contrast.get())
    var = var / 50.0
    cap.set(cv2.CAP_PROP_CONTRAST, var)

def setBrightness(var):
    global brightness, idx_bright
    print "idx_bright:", idx_bright
    # print contrast.get()
    var = float(brightness.get())
    var = var / 50.0
    var = var * idx_bright
    print "var:", var
    cap.set(cv2.CAP_PROP_BRIGHTNESS, var)


mainWindow = tk.Tk()
mainWindow.resizable(width=True, height=True)
mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
lmain = tk.Label(mainWindow, compound=tk.CENTER, anchor=tk.CENTER, relief=tk.RAISED)
button = tk.Button(mainWindow, text="Capture", command=prompt_ok)
button_changeCam = tk.Button(mainWindow, text="Switch Camera", command=changeCam)

lmain.pack()
var = tk.DoubleVar()
contrast = tk.Scale(mainWindow, orient=tk.HORIZONTAL,
                                 label='Contrast', variable=var, resolution=0.5, from_=0.0, to=100.0,
                                 command=setContrast)
contrast.set(50)
contrast.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)


brightness = tk.Scale(mainWindow, orient=tk.HORIZONTAL,
                                 label='Brightness', resolution=0.5, from_=0.0, to=100.0,
                                 command=setBrightness)
brightness.set(50)
brightness.pack(side=tk.LEFT,anchor=tk.NW, padx=5, pady=5)



button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
button.focus()
button_changeCam.place(bordermode=tk.INSIDE, relx=0.85, rely=0.1, anchor=tk.CENTER, width=150, height=50)



def show_frame():
    global cancel, prevImg, button, standard, idx_bright

    _, frame = cap.read()
    avg = get_avg_gray(frame)
    idx_bright = standard / avg[0]
    # print idx_bright
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if not cancel:
        lmain.after(10, show_frame)

while(1):

    show_frame()
    mainWindow.mainloop()


