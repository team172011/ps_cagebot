## ps_cagebot
Repository des Projektseminars "Wirtschaftsinformatik und Operations Research" (WI und OR) SS2017 

Der erste Commit dieses Repository entspricht dem Stand wahrend der Abschlusspraesentation. Alle darauf aufbauenden Commits
wurden anschließend zum Bereinigen und Dokumentieren getaetigt und konnten nicht mehr am Roboter getestet werden.

Abhaengigkeiten zum Kompilieren und Ausführen der Klassen/Scripte:
Die Entwicklung wurde auf einem Debian OS gestartet, Kompabilitaetsporbleme mit Touch-Screen und Video-Chats 
bedingten kurzfristig einen Wechsel zu Windows als OS des Roboters (die apt-Bezeichnungen beschreiben die 
benötigten Pakete in einem Linux-System, welche unvollstaendig sind weil auf windows gewechselt wurde).


1. opencv 3.2 			(https://github.com/opencv/opencv/tree/3.2.0)
⋅⋅* opencv_contrib 3.2 		(https://github.com/opencv/opencv_contrib/tree/3.2.0)
3. skype	
4. zbar (pip + windows builds)		(https://github.com/Polyconseil/zbarlight)
⋅⋅* libzbar0 (apt)
⋅⋅* libzbar-dev (apt)
5. SpeechRecognition(pip)	(https://github.com/Uberi/speech_recognition)
⋅⋅* pyAudio (pip)
⋅⋅* portaudio19-dev (apt)
6. MySQL-python (pip)
7. gtts (pip)
8. mysql-connector-python-rf (pip install --egg ...)
⋅⋅* libmysqlclient-dev (apt)
10. wit (pip)
11. mysql-server (apt)
12. imutils (pip)
13. libfreenect (https://github.com/OpenKinect/libfreenect)
⋅⋅* libusb-1.0-0-dev (apt)
14. Avbin (https://avbin.github.io/AVbin/Download.html)
15. pyttsx (pip)
..*pywin32 (pip und evtl. Treiber)
16. opencv-python (Windows https://pypi.python.org/pypi/opencv-python, wenn opencv nicht kompiliert)
17. opencv-contrib-python 

Sonstige Abhaengigkeiten
A. imultis (https://github.com/jrosebr1/imutils.git)
..* zum eingrenzen des HSV-Farbraumes fuer die Ball-Detection
B. XAMP mit Apache und MYSQL
..* als (lokaler) Server für die Website (Verbandswagen...) und Datenbank (Verbandswagen und Face-Detection)


Folgende Batch-Dateien starten die drei Szenarien:
1. Ball-Tracking (erkennen und folgen eines gruenen Balls)
..* start_ball_tracking.bat
2. Line-Following (folgen einer schwarzen Linie)
..* start_line_following.bat
3. Face-Detection + Speech-Detection (Gesichtserkennung, identifizierung mit QR-Code und starten des Spracherkennung)
..* start_video_speech_handler.bat

Das vierte Szenario, ein intelligenter Verbandswagen, basiert auf RFID-Chips die eine URL-auf einem lokalen Webserver aufrufen (XAMP...).
..* Den Ordner "website" auf Webserver einbinden und einrichten eines Netzwerk in dem sich der Roboter mit Webserver und der RFID-Scanner (z.B. Smartphone) befinden