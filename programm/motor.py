#!/usr/bin/env python
 
import serial
import math
import time
import general
# debug log to console 
# >10: log everything
debug=15
 
 # leftspeedvalue = general.leftspeedvalue
 # rightspeedvalue = general.rightspeedvalue

# for while loops in threads, if aborted -> False
# running = general.Running
 
def motors():
  ser = serial.Serial()
  ser.port = 'com4'
  ser.baudrate = 115200
  ser.parity = serial.PARITY_NONE
  ser.stopbits = serial.STOPBITS_ONE
  ser.bytesize = serial.EIGHTBITS
  ser.timeout = None
  CMD_MOTOR_DRIVE=[1, 249, 3, 6, 42, 0]
  ser.open()
  time.sleep(2)
  print('motor ready')
   
  while general.Running:
    if debug > 10:
      print(' leftspeed: ' + str(general.leftspeedvalue) + ' rightspeed: ' + str(general.rightspeedvalue))
    if general.leftspeedvalue > 0:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 11, int(general.leftspeedvalue)]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 31, int(general.leftspeedvalue)]
    elif general.leftspeedvalue < 0:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 12, abs(int(general.leftspeedvalue))]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 32, abs(int(general.leftspeedvalue))]
    else:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 11, 0]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 31, 0]
    if general.rightspeedvalue > 0:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 22, int(general.rightspeedvalue)]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 42, int(general.rightspeedvalue)]
    elif general.rightspeedvalue < 0:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 21, abs(int(general.rightspeedvalue))]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 41, abs(int(general.rightspeedvalue))]
    else:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 22, 0]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 42, 0]
       
    ser.write(CMD_MOTOR_DRIVE_1)
    ser.write(CMD_MOTOR_DRIVE_2)
    ser.write(CMD_MOTOR_DRIVE_3)
    ser.write(CMD_MOTOR_DRIVE_4)
    #print "M1: {} M2: {} M3: {} M4: {}".format(CMD_MOTOR_DRIVE_1, CMD_MOTOR_DRIVE_2, CMD_MOTOR_DRIVE_3, CMD_MOTOR_DRIVE_4)
    time.sleep(0.1)
 
  ser.close()