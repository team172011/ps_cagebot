# ps_cagebot
## Repository des Projektseminars "Wirtschaftsinformatik und Operations Research" (WI und OR) SS2017 

Der **erste Commit dieses Repository** entspricht dem **Stand wahrend der Abschlusspraesentation**. Alle darauf aufbauenden Commits wurden anschließend zum Bereinigen und Dokumentieren getaetigt und konnten nicht mehr am Roboter getestet werden.

### Abhaengigkeiten zum Kompilieren und Ausführen der Klassen/Scripte:

Die Entwicklung wurde auf einem Debian OS gestartet, Kompabilitaetsporbleme mit Touch-Screen und Video-Chats 
bedingten kurzfristig einen **Wechsel zu Windows als OS des Roboters** (die apt-Bezeichnungen beschreiben die 
benötigten Pakete in einem Linux-System, welche unvollstaendig sind weil auf windows gewechselt wurde).


* opencv 3.2 			            (https://github.com/opencv/opencv/tree/3.2.0)
  * opencv_contrib 3.2 		      (https://github.com/opencv/opencv_contrib/tree/3.2.0)
* skype	
* zbar (pip + windows builds)	(https://github.com/Polyconseil/zbarlight)
  * libzbar0 (apt)
  * libzbar-dev (apt)
* SpeechRecognition(pip)	    (https://github.com/Uberi/speech_recognition)
  * pyAudio (pip)
  * portaudio19-dev (apt)
* MySQL-python (pip)
* gtts (pip)
* mysql-connector-python-rf (pip install --egg ...)
  * libmysqlclient-dev (apt)
* wit (pip)
* mysql-server (apt)
* imutils (pip)
* libfreenect                   (https://github.com/OpenKinect/libfreenect)
  * libusb-1.0-0-dev (apt)
* Avbin                         (https://avbin.github.io/AVbin/Download.html)
* pyttsx (pip)
  * pywin32 (pip und evtl. Treiber)
* opencv-python (Windows https://pypi.python.org/pypi/opencv-python, wenn opencv nicht kompiliert)
* opencv-contrib-python 

### Sonstige Abhaengigkeiten:

* imultis                       (https://github.com/jrosebr1/imutils.git)
  * zum eingrenzen des HSV-Farbraumes fuer die Ball-Detection
* XAMP mit Apache und MYSQL
  * als (lokaler) Server für die Website (Verbandswagen...) und Datenbank (Verbandswagen und Face-Detection)


### Folgende Batch-Dateien starten die **drei Szenarien**:

* **Ball-Tracking** (erkennen und folgen eines gruenen Balls)
  * start_ball_tracking.bat
* **Line-Following** (folgen einer schwarzen Linie)
  * start_line_following.bat
* **Face-Detection** + Speech-Detection (Gesichtserkennung, identifizierung mit QR-Code und starten des Spracherkennung)
  * start_video_speech_handler.bat

Das vierte Szenario, ein **intelligenter Verbandswagen**, basiert auf **RFID-Chips** die eine URL-auf einem lokalen Webserver aufrufen (XAMP...).
* Den Ordner "**website**" auf Webserver einbinden und einrichten eines Netzwerk in dem sich der Roboter mit Webserver und der RFID-Scanner (z.B. Smartphone) befinden
