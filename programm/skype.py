"""
Script to start video chat by calling a skype contact
@author: wimmer, simon-justus
"""

import subprocess

def call(username):
    command = "C:\Users\ITM2\Surrogate\ps_cagebot\programm\callsimelton91.cmd {}".format(username)
    subprocess.call(command, shell=False)
