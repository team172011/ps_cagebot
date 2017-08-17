"""
Pyhton script for resizing existing images
@author: wimmer simon-justus
@param dir: 1 directory that contains the raw data
@param w: width of file
@param h: height of file
"""


import sys
import os
import cv2
import numpy as np
from time import sleep

# function for resizing existing images
def resize_images(dir,w,h):
    c = 0
    path = str(dir)+"/" # / on linux
    path_results = path+"results"
    if not os.path.exists(path_results):
        os.makedirs(path_results)
    for i in os.listdir(dir):
        try:
            c += 1
            print("resizing: "+path+str(i))
            img = cv2.imread(path+str(i), cv2.IMREAD_GRAYSCALE)
            img_res = cv2.resize(img,(w,h))

            # rotate the image if needed ....
            # rows, cols = img_res.shape

            # M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
            # img_res = cv2.warpAffine(img_res,M,(cols,rows))

            # ....comment in if not necessary
            cv2.imwrite(path_results+"/"+"5050_"+str(c)+".bmp",img_res) # / on linux
        except Exception as e:
            print("Fehler, Image wird uebersprungen:\n"+str(e))

try:
    dir = sys.argv[1]
    w = sys.argv[2]
    h = sys.argv[3]
    resize_images(dir,int(w),int(h))
except Exception as i:
    print("Fehler beim ausfeuren der Scripts. Bitte dir, w und h angeben:\n"+str(i))

