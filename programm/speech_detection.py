"""
Python Module for creating and loeading a dialog. Wait for speech input,
speech recognition, analyse and response to user
@author: wimmer, simon-justus
"""

import speech_recognition as sr
import threading
import uuid
import general
import logging
import random
import navigation_handler
import sys
import skype

from wit import Wit
from speech_output import Speaker
from time import sleep


"""
Createing and leading a dialog with a user
@:param user_id existing user id of patient/empoyee that is talking to roboter
@:param db_handler the database handler
"""

class Dialog(threading.Thread):
        def __init__(self, db_handler, thread_id, user_id, logger=logging.getLogger('defaultLogger'), thread_name='Dialog'+str(random.randint(0, 1000))):
            threading.Thread.__init__(self)
            global running

            self.name = thread_name
            self.thread_id = thread_id

            self.logger = logger

            self.db_handler = db_handler

            self.r = sr.Recognizer()
            self.m = sr.Microphone()
            self.actions = self.init_actions()
            self.calibrate_energy_treshold()

            self.client = Wit(general.params.WIT_AI_KEY, self.actions)
            self.speaker = Speaker()

            self.user_id = user_id
            self.stop = False

        """
        By starting the thread (with existing user_id) the thread is waiting for audio input through user and
        tries to handle it until the thread will be stopped
        """
        def run(self):
            self.logger.info("Ein Dialog wurde gestartet")
            self.context = self.init_context(self.user_id)
            if self.user_id in general.params.patient_id:
                result = self.db_handler.get_patient_by_qr(self.user_id)
            elif self.user_id in general.params.employee_id:
                result = self.db_handler.get_employee_by_qr(self.user_id)

            for row in result:
                name = row["Vorname"]
                break

            self.speaker.say("Hallo {0} wie kann ich die behilflich sein?".format(name))
            while not self.stop:
                self.send_and_receive()

        def end_programm(self, values=None):
            self.logger.warning("Programm wird beendet")
            general.Running = False

        def stop_dialog(self, values=None):
            self.logger.info("Dialog wird beendet")
            self.stop = True

        def calibrate_energy_treshold(self):
                with self.m as source:
                        self.r.adjust_for_ambient_noise(source)
        
        def send(self, request, response):
                print(response)
        
        def init_actions(self):
                actions={'send': self.send,
                         'list_all_employees': self.list_all_employees,
                         'list_all_patients': self.list_all_patients,
                         'list_all_materials': self.list_all_materials,
                         'call_skype': self.call_skype,
                         'call_help': self.call_help,
                         'stop_dialog': self.stop_dialog,
                         'end_programm': self.end_programm,
                         'follow_line': self.follow_line,
                         'follow_ball': self.follow_ball}
                return actions
        
        """
        init the current context of the dialog
        """
        #TODO:
        def init_context(self, user_qr):
                context = {'user': 'Unbekannter',
                           'state': 'unbekannt',
                           'permission_level':'0'}
                if user_qr in general.params.employee_id:
                        user_name = self.db_handler.get_employee_by_qr(user_qr)[0]['Vorname']
                        context['user'] = str(user_name)
                        context['state'] = 'Mitarbeiter'
                elif user_qr in general.params.patient_id:
                        user_name = self.db_handler.get_patient_by_qr(user_qr)[0]['Vorname']
                        context['user'] = str(user_name)
                        context['state'] = 'Patient'
                return context

        # actions 
        def send(self, request):
                print(request)
        
        def say_info_for_patient_with_qr(self, values):
                info_pat = self.db_handler.get_patient_by_qr(values)
                if len(info_pat)>0:
                        to_say = "Der Patient nr {0} heisst {1} {2} und wurde aufgrund des folgenden Leiden eingeliefert: {3}"
                        to_say.format(info_pat['p_qrcode'], info_pat['p_firstname'],info_pat['p_lastname'], info_pat['p_reason'])
                        self.speaker.say(to_say)
                else:
                        self.speaker.say('Zu dem angeforderten Patienten konnten keine Informationen gefunden werden')
                pass

        def say_info_for_patient(self, values):
                pass

        def say_info_for_patient(self, values):
                pass
        
        def list_all_employees(self, values):
                self.speaker.say('Folgende Mitarbeiter arbeiten hier')
                all_emp = self.db_handler.get_all_employee()
                for i in all_emp:
                        print i
                return all_emp

        def list_all_patients(self, values):
                self.speaker.say('Folgende Patienten werden hier behandelt')
                all_pat = self.db_handler.get_all_patients()
                for i in all_pat:
                        print i
                return all_pat
        
        def list_all_materials(self, values):
                self.speaker.say('Hier sind alle Materialien aufgelistet die ich finden konnte')
                all_mat = self.db_handler.get_all_materials()
                for i in all_mat:
                        print i
                return all_mat                

        def call_skype(self, values):
            skype.call(values)

        def call_help(self, values):
            self.speaker.say("Ein Hilferuf wird eingeleitet")
            self.call_skype("simelton91")
            self.stop_dialog()

        def follow_line(self, values):
            navigation_handler.modus = 3
            navigation_handler.start()

        def follow_ball(self, values):
            navigation_handler.modus = 2
            navigation_handler.start()

        """
        Sends audio file to wit.ai to get text message. Then the text message will be send to wit.ai as converse to
        analyse the content and call the corresponding function
        @:param user_qr the user id of the user who is talking to the roboter
        """
        def send_and_receive(self):
            try:
                with self.m as source:
                        self.logger.info('warte auf Sprachbefehl...')
                        sleep(1)
                        audio = self.r.listen(source, timeout=4)
                        self.logger.info('[OK]')
                        audio_text = self.r.recognize_wit(audio, general.params.WIT_AI_KEY)  # speech to text
                        resp = self.client.converse(uuid.uuid1(), audio_text, self.context)  # text to response
                        self.logger.info('wit.ai text: ' + str(audio_text))
                        self.logger.info('wit.ai response: ' + str(resp))
                        if 'action' in resp:
                                values = []
                                self.actions[resp['action']](values)
                        elif 'msg' in resp:
                                self.logger.info(resp['msg'])
                                self.speaker.say(resp['msg'])
                        elif 'stop' in resp:
                                self.logger.info('conversation beendet')
                        else:
                            self.logger.info(resp)
            except sr.RequestError as re:
                self.logger.info(str(re))
                self.speaker.say("Das habe ich nicht verstanden")

