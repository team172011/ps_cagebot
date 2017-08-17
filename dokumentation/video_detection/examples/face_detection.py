# Phyton Example File

import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
from time import sleep
import picamera

print "Version: " + cv2.__version__+" Beispieldatei"


face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_eye.xml')


# Example 1 simple face detection
def test_picture_face_detection(img,nr):
    print "Gesichtserkennung Versuch: "+str(nr)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Bild in Graustufen umwandeln
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) #Bild, scaleFactor, minNeighbor
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        smile = smile_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        eye = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    filename = 'face detection'+str(nr)+'.jpg'
    cv2.imwrite(filename, img) #speichere Bild mit recs


# Example 2 simple face detection via video input stream
def test_video_face_detection():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),(ex+ew,ey+eh),(0,255,0), 2)
            smile = smile_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in smile:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255),1)

        cv2.imshow('Face Detection Video',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# take 5 snapshots and save face detection results as jpg
camera = picamera.PiCamera()
for i in xrange(1,5):

    camera.capture('temp.jpg')
    test_picture_face_detection(img = cv2.imread('temp.jpg'),nr=i)
    sleep(3)



