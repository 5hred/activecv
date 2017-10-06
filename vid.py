#Robert Lambert lambert.r@gmail.com
#2017
from scipy  import  fftpack
import cv2
import numpy as np
import pylab as plb

#Cap is an instance of open cv VideoCapture
cap = cv2.VideoCapture(0)

"""

parms = dict(hsv,
             lower_blue,
             upper_blue,
             lower_red,
             upper_red)

"""

#loop the action to keep the app open
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([359,100,100])
    upper_red = np.array([359,100,65])
    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #display panes
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF

    def sciencefft():
        #Convert the image to a array
        fa = fftpack.fft2(frame)
        #fft on the array
        fb = fftpack.fftshift( fa )
        #plot the fft
        psf2D = np.abs( fb )**2
        #plot the power spectrum
        plb.figure(1)
        plb.clf()
        plb.imshow( psf2D )
        plb.show()

    #fig, ax = plt.subplots()
    #ax.plot(xf,)

    sciencefft()

    if k == 27:
        break

cv2.destroyAllWindows()
