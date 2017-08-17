"""
Pyhton-Module for general informations like number ranges and global data
@author: wimmer, simon-justus
"""

import os


#global variables

Running = True
Gamepad = False
leftspeedvalue = 0
rightspeedvalue = 0

# TODO: wrap data to get some kind of final static pattern
class params:
    patient_id = range(0, 9999)
    employee_id = range(10000, 19999)
    material_id = range(20000, 29999)
    command_id = range(30000, 39999)
    permission = range(0, 3)

    # camera ids
    upper_cam = 2 #face/object detection
    lower_cam = 1 #ball/line tracking


    upper_cam_resolution_w = int(1280)
    upper_cam_resolution_h = int(800)

    lower_cam_resolution_w = int(1920)
    lower_cam_resolution_h = int(1920)

    # detection / opencv
    cascade_face_frontal = './data/haarcascades/haarcascade_frontalface_default.xml'
    cascade_face_profile = './data/haarcascades/haarcascade_profileface.xml'
    cascade_eye_glasses = './data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'
    cascade_lower_body = './data/haarcascades/body.xml'

    cascade_creme = './data/haarcascades/creme.xml'
    cascade_creme2 = './data/haarcascades/creme2.xml'
    cascade_creme3 = './data/haarcascades/creme3.xml'
    cascade_banana = './data/haarcascades/banana.xml'
    cascade_pen = './data/haarcascades/pen.xml'
    cascade_pflaster = './data/haarcascades/pflaster.xml'

    # ball detection
    yellowLower = (17, 63, 122)
    yellowUpper = (35, 173, 255)

    lightLower = (30, 0, 140)
    lightUpper = (77, 103, 255)

    redLower = (0, 124, 128)
    redUpper = (3, 255, 255)

    greenLower = (23, 86, 0)
    greenUpper = (94, 255, 182)

    blackLower = (0,114,14)
    blackUpper=(255,255,68)

    # speech
    API_ENDPOINT = os.getenv('WIT_URL', 'https://api.wit.ai')
    WIT_AI_KEY = 'WLZRABEEHQRAQCOQYIM5SJ2UYRKX7TJG'
    WIT_API_VERSION = os.getenv('WIT_API_VERSION', '20160516')