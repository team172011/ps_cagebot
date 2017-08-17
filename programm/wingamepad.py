#!/usr/bin/env python
 
import math
import time
import general
from inputs import get_gamepad

 
# hardcoeded first input
#events = get_gamepad()
 
# vars
# center ~34000 should be 32768 31000&37000 nullzone
# debug log to console 
# >10: log everything

"""
leftspeedvalue = 0
rightspeedvalue = 0
"""
 
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
 
def calculateltrtspeed():
  minltrtval = 0
  maxltrtval = 255
  ltrttempspeed = 0
  ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
  if debug > 10:
    print('speed: ' + str(ltrttempspeed))
  return int(ltrttempspeed)
 
def calculatemotorspeedsgamepad():
  global rtact
  global ltact
  global horact_gamepad

  steermultiplier = 0
  maxltrtval = 255
  maxspeed = 100
  #ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
  ltrttempspeed = int(float((rtact-ltact))/255*100)
  #speedvalue = ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)

  steernull = 1000
  steernullmin = nullmin - steernull
  steernullmax = nullmax + steernull

  #minval = 0
  #maxval = 65535
  #nullmin links
  #nullmax rechts

  if horact_gamepad < nullmin:
    steermultiplier = float(horact_gamepad)/minval
    general.leftspeedvalue = ltrttempspeed - steermultiplier * 100
    general.rightspeedvalue = ltrttempspeed + steermultiplier * 100
  elif horact_gamepad > nullmax:
    steermultiplier = float(horact_gamepad)/maxval
    general.leftspeedvalue = ltrttempspeed + steermultiplier * 100
    general.rightspeedvalue = ltrttempspeed - steermultiplier * 100
  else:
    general.leftspeedvalue = general.rightspeedvalue = ltrttempspeed

  print('sm: ' + str(steermultiplier) + ' horact_gamepad: ' + str(horact_gamepad) + ' ltact: ' + str(ltact) + ' rtact: ' + str(rtact) + ' tempspeed ' + str(ltrttempspeed) + ' lsv: ' + str(general.leftspeedvalue) + ' rsv: ' + str(general.rightspeedvalue))

def run_gamepad():
  debug=0
 
  # nullzone analogstick
  minval = -32768
  nullmin = -500
  nullmax = 3000
  maxval = 32767

    # right analog stick values (horizontal/vertical: min, actual, max)
  hormin = 32000
  hormax = 0
  horact_gamepad = 0
 
  # lt values (min, actual, max)
  ltmin = 255
  ltact = 0
  ltmax = 0
 
  # rt values (min, actual, max)
  rtmin = 255
  rtact = 0
  rtmax = 0


  # speed values (max: 0-100 and actual)
  maxspeed = 100
  speedvalue = 0
  
  while general.Running:
    events = get_gamepad()
    for event in events:
      #print(event.ev_type, event.code, event.state)
        # should go to own thread
      if event.ev_type == "Absolute":               # a stick is moved
        if event.code == "ABS_RX":             # right stick horizontal
          horact_gamepad = event.state
          print "abs_rx "+str(event.state)
          #calculatemotorspeeds()
        if event.code == "ABS_Z":             # LT
          ltact = event.state
          print "abs_z "+str(event.state)
          #calculatemotorspeeds()
        if event.code == "ABS_RZ":              # RT
          rtact = event.state
          print "abs_rz "+str(event.state)
          #calculatemotorspeeds()
        if event.code == 'ABS_HAT0Y'or event.code == 'ABS_HAT0X':
          if event.state == 1:
            general.Gamepad = not general.Gamepad
            print "swith Gamebad  "+str(event.state)
        #speedvalue = calculatespeed(event.value)
      if event.ev_type == "Key":
        if event.code == 'BTN_NORTH' or event.code == 'BTN_SOUTH' or event.code == 'BTN_EAST' or event.code == 'BTN_WEST':
          print("Button was pressed. Stopping.")
          general.Running = False
          break
      if general.Gamepad:
        steermultiplier = 0
        maxltrtval = 255
        maxspeed = 100
        #ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
        ltrttempspeed = int(float((rtact-ltact))/255*100)
        #speedvalue = ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)

        steernull = 1000
        steernullmin = nullmin - steernull
        steernullmax = nullmax + steernull

        #minval = 0
        #maxval = 65535
        #nullmin links
        #nullmax rechts

        if horact_gamepad < nullmin:
          steermultiplier = float(horact_gamepad)/minval
          general.leftspeedvalue = ltrttempspeed - steermultiplier * 100
          general.rightspeedvalue = ltrttempspeed + steermultiplier * 100
        elif horact_gamepad > nullmax:
          steermultiplier = float(horact_gamepad)/maxval
          general.leftspeedvalue = ltrttempspeed + steermultiplier * 100
          general.rightspeedvalue = ltrttempspeed - steermultiplier * 100
        else:
          general.leftspeedvalue = general.rightspeedvalue = ltrttempspeed

        print('sm: ' + str(steermultiplier) + ' horact_gamepad: ' + str(horact_gamepad) + ' ltact: ' + str(ltact) + ' rtact: ' + str(rtact) + ' tempspeed ' + str(ltrttempspeed) + ' lsv: ' + str(general.leftspeedvalue) + ' rsv: ' + str(general.rightspeedvalue))

    