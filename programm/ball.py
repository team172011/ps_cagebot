#!/usr/bin/env python
# coding: utf8
import general
def calculatemotorspeedsball(horact, actradius):
 # global leftspeedvalue
 # global rightspeedvalue
 # global speedvalue

#  global horact
#  global actradius

  steermultiplier = 0
  
  # unter diesem Wert keine Beschleunigung
  minradius = 70

  # ab diesem Wert verfolgt er das Objekt
  defaultradius = 45

  # ab diesem Wert Vollgas
  maxradius = 25

  # Maximalgeschwindigkeit des Motors 
  maxspeed = 100




  #ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
  #ltrttempspeed = int(float((rtact-ltact))/(minradius-maxradius)*maxspeed)
  #speedvalue = ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)

  # Geschwindigkeit anhand des Radius ermitteln
#  tempspeed = (1-((actradius-maxradius)/minradius))*maxspeed
  tempspeed = int((1-((float(actradius)-maxradius)/minradius))*maxspeed)
  if tempspeed<0:
    tempspeed=0
  elif tempspeed>100:
    tempspeed=100

  minval = -1000

  maxval = 1000
  # Ab wann reagiert er
  steernull = 50

  # Möglichkeit den Nullpunkt zu verschieben.
  nullmin = 0 - steernull
  nullmax = 0 + steernull

  if horact < nullmin:
    steermultiplier = float(horact)/minval
    
    for_left = tempspeed - (steermultiplier * maxspeed)*2
    
    # limit left and right speed  -100 >=  speed <= +100
    if for_left >= 0:
      for_left = min(100, for_left)
    else:
      for_left = max(-100, for_left)
    for_right = tempspeed + (steermultiplier * maxspeed)*2
    if for_right >= 0:
      for_right = min(100, for_right)
    else:
      for_right = max(-100, for_right)

    general.leftspeedvalue = for_left
    general.rightspeedvalue = for_right
  elif horact > nullmax:
    steermultiplier = float(horact)/maxval

    for_left = tempspeed + (steermultiplier * maxspeed)*2
    if for_left >= 0:
      for_left = min(100, for_left)
    else:
      for_left = max(-100, for_left)


    for_right = tempspeed - (steermultiplier * maxspeed)*2
    if for_right > 0:
      for_right = min(100, for_right)
    else:
      for_right = max(-100, for_right)

    general.leftspeedvalue = for_left
    general.rightspeedvalue = for_right
  else:
    general.leftspeedvalue = general.rightspeedvalue = tempspeed

  print('sm: ' + str(steermultiplier) + ' actradius: ' + str(actradius) + ' tempspeed ' + str(tempspeed) + ' lsv: ' + str(general.leftspeedvalue) + ' rsv: ' + str(general.rightspeedvalue))

def calculatemotorspeedsline(horact, actradius):
 # global leftspeedvalue
 # global rightspeedvalue
 # global speedvalue

#  global horact
#  global actradius

  steermultiplier = 0
  
  # unter diesem Wert keine Beschleunigung
  minradius = 70

  # ab diesem Wert verfolgt er das Objekt
  defaultradius = 45

  # ab diesem Wert Vollgas
  maxradius = 25

  # Maximalgeschwindigkeit des Motors 
  maxspeed = 100




  #ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)
  #ltrttempspeed = int(float((rtact-ltact))/(minradius-maxradius)*maxspeed)
  #speedvalue = ltrttempspeed = maxspeed/maxltrtval*(rtact-ltact)

  # Geschwindigkeit anhand des Radius ermitteln
#  tempspeed = (1-((actradius-maxradius)/minradius))*maxspeed

  tempspeed = min(20, actradius) # line following always same speed
  minval = -1000

  maxval = 1000
  # Ab wann reagiert er
  steernull = 75 # -1000 bis 1000

  # Möglichkeit den Nullpunkt zu verschieben.
  nullmin = 0 - steernull
  nullmax = 0 + steernull

  if horact < nullmin:
    steermultiplier = float(horact)/minval
    general.leftspeedvalue = tempspeed - (steermultiplier * maxspeed)*2
    general.rightspeedvalue = tempspeed + (steermultiplier * maxspeed)*2
  elif horact > nullmax:
    steermultiplier = float(horact)/maxval
    general.leftspeedvalue = tempspeed + (steermultiplier * maxspeed)*2
    general.rightspeedvalue = tempspeed - (steermultiplier * maxspeed)*2
  else:
    general.leftspeedvalue = general.rightspeedvalue = tempspeed

  print('sm: ' + str(steermultiplier) + ' actradius: ' + str(actradius) + ' tempspeed ' + str(tempspeed) + ' lsv: ' + str(general.leftspeedvalue) + ' rsv: ' + str(general.rightspeedvalue))




  
  
