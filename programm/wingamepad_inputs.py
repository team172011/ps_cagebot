#!/usr/bin/env python
# coding: utf8
from inputs import get_gamepad

horact = 0
veract = 0
hormin = 0
hormax = 0
vermin = 0
vermax = 0
ltact = 0
rtact= 0

while 1:
  events = get_gamepad()
  for event in events:
    print(event.ev_type, event.code, event.state)
    if event.ev_type == "Absolute":               # a stick is moved
      if event.code == "ABS_RX":             # left stick horizontal
        horact = event.state
        if event.state > hormax:
          hormax = event.state
        if event.state < hormin:
          hormin = event.state
      if event.code == "ABS_RY":             # left stick vertical
        veract = event.state
        if event.state > vermax:
          vermax = event.state
        if event.state < vermin:
          vermin = event.state
      if event.code == "ABS_Z":             # LT
        ltact = event.state
      if event.code == "ABS_RZ":              # RT
        rtact = event.state
    print('hormin: ' + str(hormin) + ' horact: ' + str(horact) + ' hormax: ' + str(hormax))
    print('vermin: ' + str(vermin) + ' veract: ' + str(veract) + ' vermax: ' + str(vermax))
    print('LT: ' + str(ltact) + ' RT: ' + str(rtact))