"""
Class(threading.Thread) for detecting and tracking objects
@author: wimmer, simon-justus
based on    http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
            http://einsteiniumstudios.com/beaglebone-opencv-line-following-robot.html

"""
import logging
import random
import threading
import numpy as np
import cv2
import wingamepad

import general
import ball

from PIL import Image
import zbar
from collections import deque


class ObjectTracker(threading.Thread):
    def __init__(self, thread_id, logger=logging.getLogger('defaultLogger'),
                 thread_name='Tracker' + str(random.randint(0, 10)), mod=0):
        threading.Thread.__init__(self)

        self.thread_id = thread_id
        self.logger = logger
        self.name = thread_name

        self.stop = False

        self.buffer = 10

        self.middle = 40
        self.near_min, self.near_max = (65, 100)

        self.mod = mod

        self.last_position = 0

        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')

    def run(self):
        cap = cv2.VideoCapture(general.params.lower_cam)
        self.logger.info('Nutze Kamera Nummer: ' + str(general.params.lower_cam))

        lock = threading.RLock()
        lock.acquire()
        if self.mod == 0:
            self.start_creme_tracking(cap)
        elif self.mod == 1:
            cap.set(4, general.params.lower_cam_resolution_h)
            cap.set(3, general.params.lower_cam_resolution_w)
            _, frame = cap.read()
            self.y_max = len(frame[0])
            self.x_max = len(frame[1])
            print "Video size: {0} {1}".format(self.x_max, self.y_max)
            self.init_cam(cap)
            self.start_ball_tracking(cap)
        elif self.mod == 2:
            cap.set(4, 1000)
            cap.set(3, 1000)
            _, frame = cap.read()
            self.y_max = len(frame[0])
            self.x_max = len(frame[1])
            print "Video size: {0} {1}".format(self.x_max, self.y_max)
            self.init_cam(cap)
            self.start_line_tracking(cap)
        elif self.mod == 3:
            general.Gamepad = True
            self.start_gamepad()

        lock.release()

    """
    read the first 100 frame to initialize the camera
    """

    def init_cam(self, cap):
        num = 0
        while num < 25:
            cap.read()
            num = num + 1

    def start_gamepad(self):
        wingamepad.run_gamepad()

    """
    modus = 0
    detect and track a lower body. Currently not in use
    """

    def start_body_tracking(self, cap):
        creme = cv2.CascadeClassifier(general.params.cascade_creme3)

        while not self.stop:
            _, image = cap.read()

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # make image gray
            b = creme.detectMultiScale(gray, 1.1, 5, 5, (100, 100))
            for (x, y, w, h) in b:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.imshow("body", image)
            key = cv2.waitKey(1) & 0xFF

    def stop_tracking(self):
        self.logger.info("Tracking stopped!")
        general.leftspeedvalue = 0
        general.rightspeedvalue = 0
        self.stop = True

    """
    modus = 1
    track a colored ball and print its parameters (position, radius)
    """

    def start_ball_tracking(self, cap):
        _, image = cap.read()

        self.lower = general.params.greenLower
        self.upper = general.params.greenUpper

        pts = deque(maxlen=self.buffer)
        while not self.stop and general.Running:
            grabbed, frame = cap.read()

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower, self.upper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if radius > 10:
                    cv2.circle(frame, (int(x), int(y)), int(radius),
                               (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                self.write_ball_command(center, radius)
            else:
                pass
            pts.appendleft(center)

            # loop over the set of tracked points
            for i in xrange(1, len(pts)):
                if pts[i - 1] is None or pts[i] is None:
                    continue

                thickness = int(np.sqrt(self.buffer / float(i + 1)) * 2.5)
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

    """
    Prints the position in a controller friendly transformation 
    left, right = range(-1000,1000)
    radius = radius or 100000 if not given
    """

    def write_ball_command(self, center, radius):

        if radius < 5 or center is None:
            radius = 99
            position = self.last_position

        x, y = center
        entity = float(1000 / (self.x_max / 2))
        if x >= self.x_max / 2:
            position = entity * (x - self.x_max / 2)
        else:
            position = entity * (self.x_max / 2 - x)
            position = -position

        # self.last_position = position
        if not general.Gamepad:
            self.logger.info("ball.calculatemotorspeedball horact={}, actradius={}".format(position, radius))
            ball.calculatemotorspeedsball(horact=position, actradius=radius)

    """
    modus == 2
    track a line and follow ist parameters
    """

    def start_line_tracking(self, cap):
        _, frame = cap.read()
        while not self.stop and general.Running:
            _, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            ret, thresh1 = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

            # Erode and dilate to remove accidental line detections
            mask = cv2.erode(thresh1, None, iterations=8)
            mask = cv2.dilate(mask, None, iterations=8)

            # Find the contours of the frame

            im2, contours, hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)

            # Find the biggest contour (if detected)
            # circle = self.detect_circle(frame)
            if len(contours) > 0 and len(contours) < 18:
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.line(frame, (cx, 0), (cx, 720), (255, 0, 0), 1)
                cv2.line(frame, (0, cy), (1280, cy), (255, 0, 0), 1)
                cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)
                self.write_line_command(center=(cx, cy))
            else:
                self.write_line_command((None,None), speed=20) # slowly straigt on
                pass

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    """
	get information if qr code detected else None
    currently not in use
	"""
	def search_qr(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        pil = Image.fromarray(gray)
        w, h = pil.size
        raw = pil.tobytes()
        zbar_im = zbar.Image(w, h, 'Y800', raw)
        self.scanner.scan(zbar_im)
        for code in zbar_im:
            data = code.data.split(' ')
            try:
                id = int(data[1])
            except IndexError:
                return None
            if id is None:
                return None
            else:
                self.logger.info('Id erkannt: ' + str(id))
                return int(id)

     """
    Prints the position in a controller friendly transformation 
    left, right = range(-1000,1000)
    speed=100 if not given (=30 in ball.py )
    """

    def write_line_command(self, center, speed=100):
        x, y = center
        print "x: " + str(x) + " x_max: " + str(self.x_max)
        entity = float(1000 / (self.x_max / 2))
        if x is None:
            x = position = 0
        elif x >= self.x_max / 2:
            position = entity * (x - self.x_max / 2)
        else:
            position = entity * (self.x_max / 2 - x)
            position = -position

        # self.last_position = position
        if not general.Gamepad:
            self.logger.info("ball.calculatemotorspeedsline horact={}, speed={}".format(position, speed))
            ball.calculatemotorspeedsline(horact=position, actradius=speed)

	"""
	try to detect circles in a frame
	currently not in use
	"""
    def detect_circle(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect circles in the image
        circles = cv2.HoughCircles(gray, 3, 1.2, 100)  # 3 = cv2.CV_HOUGH_GRADIENT

        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(image, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                return True  # True if circle detected
        return False  # else false
