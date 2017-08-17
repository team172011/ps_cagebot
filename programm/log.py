"""
Logger builder for getting a logger that can be used for debugging 
(print on console) and for reales mode (disable console output)
@author: wimmer, simon-justus
"""

import logging
import os

class logger_builder:
    def __init__(self, log_name = 'default Logger', log_dir='logging123'):
        self.log_dir = log_dir 
        self.log_name = log_name
        self.logger = logging.Logger(str(log_name))
        self.set_logging_config()
    
    def set_logging_config(self):
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        logging.getLogger().addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.DEBUG)
        
        self.log_dir = "{0}/{1}".format(os.getcwd(),self.log_dir)
        if not os.path.isdir(self.log_dir):
            os.mkdir(self.log_dir)
        
        fileHandler = logging.FileHandler("{0}/{1}.log".format(self.log_dir,self.log_name))
        fileHandler.setFormatter(logFormatter)
        self.logger.addHandler(fileHandler)
        
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)        
    
    def get_logger(self):
        return self.logger