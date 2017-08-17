#!/usr/bin/env python
# coding: utf8
"""
Python Module for face, qr-code and object detection with obencv 3.2 and zbar module
@author: wimmer, simon-justus
"""


import numpy as np
import cv2
import zbar

import logging
import threading
import random

import general

from speech_output import Speaker
from PIL import Image
from speech_detection import Dialog


"""
Search for available cameras on this operating system
@return: id of last available camera or None if there is no available cam
"""


def get_available_cam_id():
    cam_id = None
    i = 0
    while i < 50:
        if cv2.VideoCapture(i).isOpened():
            cam_id = i
        i = i + 1
    return cam_id


""""
Class(threading.Thread) that searches for faces in frames of the camera input stream
if face is detected, the *** function tries to find an QR-code
if QR-code ist detected, the *** function tries to get an corresponding DB Result
if no face is detected, the *** function will search for other objects 
Results will be printed on console and on frames of video output
"""


class FaceQrSearch(threading.Thread):

    def __init__(self, thread_id, p_db_handler, logger=logging.getLogger('defaultLogger'), thread_name='FaceQrSearch'+str(random.randint(0, 10))):
        threading.Thread.__init__(self)

        self.thread_id = thread_id

        self.face_frontal = cv2.CascadeClassifier(general.params.cascade_face_frontal)
        self.face_profile = cv2.CascadeClassifier(general.params.cascade_face_profile)
        self.eyes = cv2.CascadeClassifier(general.params.cascade_eye_glasses)
        self.banana = cv2.CascadeClassifier(general.params.cascade_banana)
        self.pflaster = cv2.CascadeClassifier(general.params.cascade_pflaster)
        self.lower_body = cv2.CascadeClassifier(general.params.cascade_lower_body)
        self.stop = False
        self.name = thread_name
        self.db_handler = p_db_handler
        self.logger = logger
        self.speaker = Speaker()
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')

    def __del__(self):
        self.stop_searching()
        cv2.destroyWindow("PS_Cagebot")

    def run(self):
        cap = cv2.VideoCapture(general.params.upper_cam)
        cap.set(3, general.params.upper_cam_resolution_h)
        cap.set(4, general.params.upper_cam_resolution_w)
        self.logger.info('Nutze Kamera Nummer: ' + str(general.params.upper_cam))
        lock = threading.RLock()
        lock.acquire()
        self.start_searching(cap)
        lock.release()

    def stop_searching(self):
        self.stop = True

    # get information if qr code detected else None
    def search_and_get_qr(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        pil = Image.fromarray(gray)
        w, h = pil.size
        raw = pil.tobytes()
        zbar_im = zbar.Image(w, h, 'Y800', raw)
        self.scanner.scan(zbar_im)

        for code in zbar_im:
            data = code.data.split(' ')
            id = int(data[1])
            self.logger.info('Id erkannt: '+str(id))
            if id is None:
                return None

            results = None
            if id in general.params.patient_id:
                results = self.db_handler.get_patient_by_qr(id)
            elif id in general.params.employee_id:
                results = self.db_handler.get_employee_by_qr(id)
            person_info = []
            for rows in results:
                id = rows['id']
                current_dialog = Dialog(user_id=id, thread_id=10, logger=self.logger,
                                        thread_name="current_dialog", db_handler=self.db_handler)

                current_dialog.daemon = True
                current_dialog.start()

                return rows, current_dialog  # just first result and corresponding instance of dialog
        return None, None

    """
    start searching for a face, and (if there is one) search for an qr-code
    show location of face/object and information on outputframe
    @:param cap opencv-frame from video input
    """
    def start_searching(self, cap):

            tracker = None  # tracker on a detected face
            person_info = None  # information (row of sql database) for a detected person
            current_dialog = None # instance of a dialog that is acive at the moment
            _, image = cap.read()
            x_max = len(image[0])
            y_max = len(image[1])
            print x_max, y_max
            while not self.stop:
                a = cv2.waitKey(1) & 0xFF
                if a == ord("q"):
                    self.stop_searching()
                    
                _, image = cap.read()

                if person_info is None:
                    person_info, current_dialog = self.search_and_get_qr(image)
                """
                if there is a tracker, a person was identified and its face will be tracked
                """
                if tracker is not None:
                    ok, bbox = tracker.update(image)
                    x, y, xi, yi = bbox
                    # disable tracker if we are to close to the border
                    if ok and x > 15 and y > 15 and int(x+xi) < (x_max-15) and int(y+yi) < (y_max-15):
                        x, y, xi, yi = bbox
                        cv2.rectangle(image, (int(x), int(y)), (int(x + xi), int(y + yi)),
                                          (166, 255, 77))  # draw tracker
                        if person_info is None:
                                # draw person_info
                                cv2.putText(image, 'Unbekannte Person', (int(x + xi), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                                            0.5, (166, 255, 77))
                        else:
                            y_var = int(y)
                            for value, key in person_info.iteritems():
                                text = str(value) + ': ' + str(key)
                                # draw person_info
                                cv2.putText(image, text, (int(x + xi), y_var), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                            (166, 255, 77))
                                y_var += 20
                    else:
                        tracker = None
                        person_info = None
                        if current_dialog is not None:
                            if current_dialog.isAlive():
                                current_dialog.stop_dialog()
                                current_dialog = None
                        self.logger.info('Starte Gesichtserkennung')

                """
                if there is no tracker and the tracker was not set, we will search for a face (and eyes to be sure) 
                and set a tracker on the detected area
                """
                if tracker is None:
                    # search for face and set tracker if found
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    face = self.face_frontal.detectMultiScale(gray, 1.1, 5, 5, (100, 100))  # image, scale, minNeighbor

                    if len(face) > 0: # frontal face detected
                        for (x, y, w, h) in face:
                            center = x + w/2, y+h/2
                            cv2.circle(image, center, w / 2, (255, 255, 0), 2)
                            break
                    """
                    profile = self.face_profile.detectMultiScale(gray, 1.1, 5, 5, (100, 100))
                    elif len(profile) > 0: # face in profile detected
                        for (x, y, w, h) in profile:
                            center = x + w / 2, y + h / 2
                            cv2.circle(image, center, w / 2, (255, 255, 0), 2) 
                    """

                    # if face was found, search for eyes to be sure and set tracker if found:
                    if len(face) > 0:
                        eyes = self.eyes.detectMultiScale(gray)
                        for (xe, ye, we, he) in eyes: # search for eyes to be sure that there is a face in the frame
                            cv2.circle(image, center, w / 2, (255, 255, 0), 1)
                            center_e = xe + we / 2, ye + he / 2
                            cv2.circle(image, center_e, we / 2, (255, 255, 0), 1)
                            tracker = cv2.Tracker_create("BOOSTING")
                            tracker.init(image, (x, y, w, h))  # init tracker
                            self.logger.info('Gesicht erkannt')
                            self.speaker.say_in_thread("Hallo, bitte identifizieren Sie sich mithilfe ihres QR-Codes")
                            break
                
                cv2.imshow("PS_Cagebot", image)
                cv2.waitKey(1)
            cap.release()