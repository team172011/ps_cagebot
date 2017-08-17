"""
Module for connecting and communicating with sql-database
@author: simon-justus wimmer
"""

import mysql.connector as connector
import logging


# TODO: avoid sql injection...
class DatabaseHandler:
    global db_num
    db_num = 0

    def __init__(self, logger=logging.getLogger('DatabaseHandler')):
        global db_num
        self.logger = logger
        self.logger.info('DatabaseHandler Klasse instanziert')
        db_num += 1
        if (db_num > 1):
            print('Achtung, es werden meherer DatabaseHandler genutzt')

    def connect(self):
        db = connector.connect(host="localhost",
                               user="cagebot",
                               passwd="ps_cagebot2017",
                               db="ps_cagebot")  # database
        print db.database
        return db

    def get_employee_by_qr(self, qr):
        query = 'SELECT * FROM employee WHERE id = {}'.format(int(qr))
        return self.execute_query(query)

    def get_employee_by_name(self, lastname):
        query = 'SELECT * FROM employee WHERE Nachname = \'{}\''.format(str(lastname.lower()))
        return self.execute_query(query)

    def get_patient_by_qr(self, qr):
        query = 'SELECT * FROM patients WHERE id = {}'.format(int(qr))
        return self.execute_query(query)

    def get_patient_by_name(self, lastname):
        query = 'SELECT * FROM patients WHERE Nachname = \'{}\''.format(str(lastname))
        return self.execute_query(query)

    def get_all_patients(self):
        query = 'SELECT * FROM patients'
        return self.execute_query(query)

    def get_all_materials(self):
        query = 'SELECT * FROM materials'
        return self.execute_query(query)

    def get_all_employee(self):
        query = 'SELECT * FROM employee'
        return self.execute_query(query)

    def execute_query(self, query):
        db = self.connect()
        cur = db.cursor(dictionary=True)
        self.logger.info(query)
        cur.execute(query)
        results = []
        for key in cur:
            results.append(key)
        db.commit()
        db.close()
        return results
