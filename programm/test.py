
# programm/..

import numpy as np
import cv2
import general

face_frontal = cv2.CascadeClassifier(general.params.cascade_face_frontal)
cap = cv2.VideoCapture(0)

while True:
	_,image = cap.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	face = face_frontal.detectMultiScale(gray, 1.1, 5, 5, (100, 100))
		
	for (x, y, w, h) in face:
		center = x + w/2, y+h/2
		cv2.circle(image, center, w / 2, (255, 255, 0), 2)
		
	cv2.imshow("PS_Cagebot", image)
	cv2.waitKey(1)