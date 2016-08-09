from opencv.cv import *
from opencv.highgui import *

import time

initialized=False

cvNamedWindow("Image", 0)
cvResizeWindow("Image", 1024, 768)
cvStartWindowThread()
initialized=True

def ui_update_image(filename):
    print "Showing", filename
    if initialized:
        image=cvLoadImage(filename)
        cvShowImage("Image", image)
        print "cvShowImage called"
        

def terminate_ui():
    if initialized:
        cvDestroyWindow("Image")

if __name__=='__main__':
    ui_update_image("/home/pmitros/stefie_on_bed.jpg")
    while True:
        time.sleep(1000)
    terminate_ui()

