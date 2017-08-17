"""
Main Python-Script for human interaction and object detection
@author: wimmer, simon-justus
"""

from object_detection import ObjectTracker
import log
from time import sleep
import sys
import threading
import motor
import general
import wingamepad

modus = 3
try:
    modus = sys.argv[1]
except Exception as e:
    print str(e)


def start():
    logger_builder = log.logger_builder(log_name='RootLogger Modus: {}'.format(modus))
    logger1 = logger_builder.get_logger()

    if int(modus) == 0:
        n = "Koerpererkennung"
    elif int(modus) == 1:
        n = "Ball-Tracking"
    elif int(modus) == 2:
        n = "Line-Following"
    elif int(modus) == 3:
        n = "Gamepadsteuerung"

    logger1.info("MODUS {} {}".format(modus, n))

    gamepad_thread = threading.Thread(target=wingamepad.run_gamepad)
    motor_thread = threading.Thread(target=motor.motors)
    tracker = ObjectTracker(2, logger1, "tracker", mod=int(modus))

    try:
        motor_thread.start()
        tracker.start()
        gamepad_thread.start()

        while tracker.isAlive() or motor_thread.isAlive or gamepad_thread.isAlive():
            sleep(900)
            general.Running = False
            motor_thread.stop()
            tracker.stop()
            gamepad_thread.stop()

        sys.exit()

    except KeyboardInterrupt, SystemExit:
        tracker.stop_tracking()
        general.Running = False
        logger1.info('Programm beendet')
        sys.exit()

if __name__ == "__main__":
    start()
