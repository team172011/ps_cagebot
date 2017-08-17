#!/usr/bin/env python
 
import serial
import math
import time
import threading
from evdev import InputDevice, categorize, ecodes, KeyEvent
import pantilthat
 
# hardcoeded first input
event0 = InputDevice('/dev/input/event0')
 
# vars
# center ~34000 should be 32768 31000&37000 nullzone
# debug log to console 
# >10: log everything
debug=330
 
# nullzone analogsticks
minval = 0
nullmin = 31000
nullmax = 37000
maxval = 65535
 
# left analog stick values (horizontal/vertical: min, actual, max)
a1hormin = 65535
a1hormax = 0
a1horact = 32768
a1vermin = 65535
a1vermax = 0
a1veract = 32768
 
# right analog stick values (horizontal/vertical: min, actual, max)
a2hormin = 65535
a2hormax = 0
a2horact = 32768
a2vermin = 65535
a2vermax = 0
a2veract = 32768
 
# lt values (min, actual, max)
ltmin = 1023
ltact = 0
ltmax = 0
 
# rt values (min, actual, max)
rtmin = 1023
rtact = 0
rtmax = 0
 
# pantilt servohat values
panact = -10
tiltact = 10
pantemp = -10
tilttemp = 10
panrange = 60
pannull = -10
tiltrange = 50
tiltnull = 10
 
# actual rgb helper value
rgbvalue = 0
 
# speed values (max: 0-100 and actual)
maxspeed = 100
speedvalue = 0
leftspeedvalue = 0
rightspeedvalue = 0
 
# for while loops in threads, if aborted -> False
running = True
 
# helpers
def smooth(val1, val2):
  tresshold = 500
  if abs(val1 - val2) > tresshold:
    return True
  else:
    return False
 
# get scaled int
#def scale(scavalue, orimin, orimax, scamin, scamax):
 
# get scaled int
def scalestick(scastivalue):
  scamin = 0
  scamax = 100
  scamid = abs(scamax - scamin)/2
  if scastivalue < nullmin:
    return int(scamid/nullmin*scastivalue)
  elif scastivalue > nullmax:
    return int(scamid+(scamid/(maxval-nullmax)*(scastivalue-nullmax)))
  else:
    return int(scamid)
 
# pan an tilt servos in steps
# pan: - = right & + = left
# tilt: - = up & + = down
 
def calculatepantilt():
  global panact
  global tiltact
   
  if a2horact < nullmin:
    panact = int(pannull+panrange-(panrange/nullmin*a2horact))
  elif a2horact > nullmax:
    panact = int(pannull-(panrange/(maxval-nullmax)*(a2horact-nullmax)))
  else:
    panact = pannull
  if a2veract < nullmin:
    tiltact = int(tiltnull+tiltrange-(tiltrange/nullmin*a2veract))
  elif a2veract > nullmax:
    tiltact = int(tiltnull-(tiltrange/(maxval-nullmax)*(a2veract-nullmax)))
  else:
    tiltact = tiltnull
 
def calculateanalogspeed(analogvalue):
  minanalogval = 0
  nullanalogmin = 31000
  nullanalogmax = 37000
  maxanalogval = 65535
  nullanalogmaxrange = 65535 - 37000
  speedrange = 100
  tempspeed = 0
   
  if analogvalue < nullanalogmin:
    tempspeed = (speedrange/nullanalogmin*analogvalue)-speedrange
    if debug > 10:
      print('speed: ' + str(tempspeed))
  elif analogvalue > nullanalogmax:
    tempspeed = speedrange/nullanalogmaxrange*(analogvalue-nullanalogmax)*-1
    if debug > 10:
      print('speed: ' + str(tempspeed))
  else:
    tempspeed = 0
    if debug > 10:
      print('speed: 0')
  return int(tempspeed)
 
def calculateltrtspeed():
  minltrtval = 0
  maxltrtval = 1023
  ltrttempspeed = 0
  ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
  if debug > 10:
    print('speed: ' + str(ltrttempspeed))
  return int(ltrttempspeed)
 
def calculatemotorspeeds():
  global leftspeedvalue
  global rightspeedvalue
  global speedvalue
  minltrtval = 0
  maxltrtval = 1023
  ltrttempspeed = 0
  speedvalue = ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
 
  steernull = 1000
  steernullmin = nullmin - steernull
  steernullmax = nullmax + steernull
 
  #minval = 0
  #maxval = 65535
   
  if a1horact < steernullmin:
    steermultiplier = 1-a1horact/steernullmin
    if speedvalue > 0:
      leftspeedvalue = -1 * steermultiplier * maxspeed + ltrttempspeed
      rightspeedvalue = ltrttempspeed
    elif speedvalue < 0:
      leftspeedvalue = ltrttempspeed
      rightspeedvalue = steermultiplier * maxspeed + ltrttempspeed
    else:
      leftspeedvalue = -1 * steermultiplier * maxspeed
      rightspeedvalue = steermultiplier * maxspeed
  elif a1horact > steernullmax:
    steermultiplier = (a1horact-steernullmax)/(maxval-steernullmax)
    if speedvalue > 0:
      leftspeedvalue = ltrttempspeed
      rightspeedvalue = -1 * steermultiplier * maxspeed + ltrttempspeed
    elif speedvalue < 0:
      leftspeedvalue = steermultiplier * maxspeed + ltrttempspeed
      rightspeedvalue = ltrttempspeed
    else:
      leftspeedvalue = steermultiplier * maxspeed
      rightspeedvalue = -1 * steermultiplier * maxspeed
  else:
    leftspeedvalue = rightspeedvalue = ltrttempspeed
 
# threaded functions
def pantilt():
  global pantemp
  global tilttemp
  angletresshold = 2
  stepsize = 10
 
  pantilthat.servo_enable(1, True)
  pantilthat.servo_enable(2, True)
 
  while running:
    if pantemp < panact and pantemp + angletresshold < panact:
      if pantemp + stepsize < pannull + panrange:
        pantemp += stepsize
      else:
        pantemp = pannull + panrange
      pantilthat.pan(pantemp)
      #time.sleep(0.005)
    elif pantemp > panact and pantemp - angletresshold > panact:
      if pantemp - stepsize > pannull - panrange:
        pantemp -= stepsize
      else:
        pantemp = pannull - panrange
      pantilthat.pan(pantemp)
      #time.sleep(0.005)
     
    if tilttemp < tiltact and tilttemp + angletresshold < tiltact:
      if tilttemp + stepsize < tiltnull + tiltrange:
        tilttemp += stepsize
      else:
        tilttemp = tiltnull + tiltrange
      pantilthat.tilt(tilttemp)
      #time.sleep(0.005)
    elif tilttemp > tiltact and tilttemp - angletresshold > tiltact:
      if tilttemp - stepsize > tiltnull - tiltrange:
        tilttemp -= stepsize
      else:
        tilttemp = tiltnull - tiltrange
      pantilthat.tilt(tilttemp)
      #time.sleep(0.005)
     
    time.sleep(0.005)
 
def rgbled():
  rgbtemp = 0
  pantilthat.light_mode(pantilthat.WS2812)
  pantilthat.light_type(pantilthat.GRBW)
 
  while running:
    if (rgbtemp != rgbvalue):
      if rgbvalue == 0:
        rgbtemp = rgbvalue
        pantilthat.set_all(0, 0, 0)
      elif rgbvalue == 1:
        rgbtemp = rgbvalue
        pantilthat.set_all(255, 0, 0)
      elif rgbvalue == 2:
        rgbtemp = rgbvalue
        pantilthat.set_all(0, 255, 0)
      elif rgbvalue == 3:
        rgbtemp = rgbvalue
        pantilthat.set_all(0, 0, 255)
      elif rgbvalue == 4:
        rgbtemp = rgbvalue
        pantilthat.set_all(127, 127, 127)
      elif rgbvalue == 5:
        rgbtemp = rgbvalue
        pantilthat.set_all(255, 255, 255)
      else:
        rgbtemp = rgbvalue
        pantilthat.set_all(255, 255, 0)
 
      pantilthat.show()
 
  #pantilthat.servo_enable(1, False)
  #pantilthat.servo_enable(2, False)
 
def motor():
  ser = serial.Serial()
  ser.port = '/dev/ttyUSB0'
  ser.baudrate = 115200
  ser.parity = serial.PARITY_NONE
  ser.stopbits = serial.STOPBITS_ONE
  ser.bytesize = serial.EIGHTBITS
  ser.timeout = None
  CMD_MOTOR_DRIVE=[1, 249, 3, 6, 42, 0]
  ser.open()
  time.sleep(2)
  print('motor ready')
   
  while running:
    speedvalue = calculateltrtspeed()
    if speedvalue > 0:
      CMD_MOTOR_DRIVE=[1, 249, 3, 6, 42, int(speedvalue)]
    elif speedvalue < 0:
      CMD_MOTOR_DRIVE=[1, 249, 3, 6, 41, abs(int(speedvalue))]
    else:
      CMD_MOTOR_DRIVE=[1, 249, 3, 6, 41, 0]
    ser.write(CMD_MOTOR_DRIVE)
    time.sleep(0.1)
 
  ser.close()
 
def motors():
  ser = serial.Serial()
  ser.port = '/dev/ttyUSB0'
  ser.baudrate = 115200
  ser.parity = serial.PARITY_NONE
  ser.stopbits = serial.STOPBITS_ONE
  ser.bytesize = serial.EIGHTBITS
  ser.timeout = None
  CMD_MOTOR_DRIVE=[1, 249, 3, 6, 42, 0]
  ser.open()
  time.sleep(2)
  print('motor ready')
   
  while running:
    if debug > 10:
      print('speed: ' + str(speedvalue) + ' leftspeed: ' + str(leftspeedvalue) + ' rightspeed: ' + str(rightspeedvalue))
    if leftspeedvalue > 0:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 11, int(leftspeedvalue)]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 31, int(leftspeedvalue)]
    elif leftspeedvalue < 0:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 12, abs(int(leftspeedvalue))]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 32, abs(int(leftspeedvalue))]
    else:
      CMD_MOTOR_DRIVE_1=[1, 249, 3, 6, 11, 0]
      CMD_MOTOR_DRIVE_3=[1, 249, 3, 6, 31, 0]
    if rightspeedvalue > 0:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 22, int(rightspeedvalue)]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 42, int(rightspeedvalue)]
    elif rightspeedvalue < 0:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 21, abs(int(rightspeedvalue))]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 41, abs(int(rightspeedvalue))]
    else:
      CMD_MOTOR_DRIVE_2=[1, 249, 3, 6, 22, 0]
      CMD_MOTOR_DRIVE_4=[1, 249, 3, 6, 42, 0]
       
    ser.write(CMD_MOTOR_DRIVE_1)
    ser.write(CMD_MOTOR_DRIVE_2)
    ser.write(CMD_MOTOR_DRIVE_3)
    ser.write(CMD_MOTOR_DRIVE_4)
     
    time.sleep(0.1)
 
  ser.close()
 
# Create two threads as follows
try:
  _thread.start_new_thread( pantilt, () )
except:
  print ("Error: unable to start pantilt thread")
try:
  _thread.start_new_thread( rgbled, () )
except:
  print ("Error: unable to start rgbled thread")
try:
  _thread.start_new_thread( motors, () )
except:
  print ("Error: unable to start rgbled thread")
 
#for event in event0.read_loop():
#   print(event)
# thread.start_new_thread()
 
for event in event0.read_loop():   # this loops infinitely
    # should go to own thread
  if event.type == 3:               # a stick is moved
    if event.code == 0:             # left stick horizontal
      a1horact = event.value
      if event.value > a1hormax:
        a1hormax = event.value
      if event.value < a1hormin:
        a1hormin = event.value
    if event.code == 1:             # left stick vertical
      a1veract = event.value
      if event.value > a1vermax:
        a1vermax = event.value
      if event.value < a1vermin:
        a1vermin = event.value
    if event.code == 2:             # right stick horizontal
      a2horact = event.value
      if event.value > a2hormax:
        a2hormax = event.value
      if event.value < a2hormin:
        a2hormin = event.value
    if event.code == 5:             # right stick vertical
      a2veract = event.value
      if event.value > a2vermax:
        a2vermax = event.value
      if event.value < a2vermin:
        a2vermin = event.value
    if event.code == 10:             # LT
      ltact = event.value
    if event.code == 9:              # RT
      rtact = event.value
    #speedvalue = calculatespeed(event.value)
 
  if event.type == 1:                        # a Buttons is pressed
    if event.code == 307 and event.value == 1:  # x Button
      if rgbvalue < 5:
        rgbvalue += 1
      else:
        rgbvalue = 0
    if event.code == 308 and event.value == 1:  # Y Button
      print('Y')
    if event.code == 304 and event.value == 1:  # A Button
      print('A')
    if event.code == 305 and event.value == 1:  # B Button
      print('B')
 
  calculatepantilt()
  calculatemotorspeeds()
  #print('a1hormin: ' + str(a1hormin) + ' a1horact: ' + str(a1horact) + ' a1hormax: ' + str(a1hormax) + ' a1horsca: ' + str(scalestick(a1horact)) + ' panact: ' + str(panact))
  #print('a1vermin: ' + str(a1vermin) + ' a1veract: ' + str(a1veract) + ' a1vermax: ' + str(a1vermax) + ' a1versca: ' + str(scalestick(a1veract)) + ' tiltact: ' + str(tiltact))
  #print('a2hormin: ' + str(a2hormin) + ' a2horact: ' + str(a2horact) + ' a2hormax: ' + str(a2hormax) + ' a2horsca: ' + str(scalestick(a2horact)))
  #print('a2vermin: ' + str(a2vermin) + ' a2veract: ' + str(a2veract) + ' a2vermax: ' + str(a2vermax) + ' a2versca: ' + str(scalestick(a2veract)))
  #if debug > 10:
  #  print('panact: ' + str(panact) + ' pantemp: ' + str(pantemp) + ' tiltact: ' + str(tiltact) + ' tilttemp: ' + str(tilttemp) + ' ltact: ' + str(ltact) + ' rtact: ' + str(rtact))
   
  if event.type == 1 and event.code == 172 and event.value == 1:
    print("XBox button was pressed. Stopping.")
    pantilthat.servo_enable(1, False)
    pantilthat.servo_enable(2, False)
    running = False
    break