import numpy
from PIL import Image,ImageDraw
from datetime import *
from time import time, sleep
import random


# import cv2
# import numpy as np
# import os
 
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = np.array(randomByteArray)
 
# grayImage = flatNumpyArray.reshape(300,400)
# cv2.imwrite('RandomGray.png',grayImage)
 
# bgrImage = flatNumpyArray.reshape(100,400,3)
# cv2.imwrite('RandomColor.png',bgrImage)



def creatNewName(arg):
    return str(arg) + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".png"


def drawImage(newName):
    out = Image.new("RGB", (150, 100), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    d = ImageDraw.Draw(out)
    d.multiline_text((20,40),datetime.now().strftime("%Y-%m-%d %H:%M:%S") , fill=(0, 0, 0))
    out.save("photo/"+newName+"", "PNG")
    print("New image created: ",newName)
    return


def main():
    while True:
        newName = creatNewName('camera')
        drawImage(newName)
        print("New image created: ",newName)
        #sleep(1 - time() % 1) #every second
        sleep(60 - time() % 60) #every minutes

if __name__ == "__main__":
    main()

