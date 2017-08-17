"""
Main Python-Script for human interaction and object detection
@author: wimmer, simon-justus
"""

from video_detection import FaceQrSearch
import database.database_handler as db_ha
import log
import sys
import time
import general
logger_builder = log.logger_builder(log_name='RootLogger')
logger1 = logger_builder.get_logger()
dbhandler = db_ha.DatabaseHandler(logger1)

general.Running = True

try:
    scanner = FaceQrSearch(1, dbhandler, logger1)  # responsible for scanning face, objects and qr-codes
    scanner.start()

    while scanner.is_alive():
        time.sleep(0.1)
        if not general.Running:
            scanner.stop_searching()
            sys.exit()

except KeyboardInterrupt:
    scanner.stop_searching()
    logger1.info('Programm beendet')
