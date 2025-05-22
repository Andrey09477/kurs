"""
Модуль работы с базой данных
Программист: Казакова Оксана ст. гр.444
Проверил: 
Дата написания: 08.04.2025
"""

from prettytable import PrettyTable, from_csv

''' класс упр-я БД (bd) '''
class DataBaseManager:
    MAX_WEIGHT = 150
    MAX_HEIGHT = 200
    students = {}
    
    def __init__(self, db_name):
        self.table = None
        self.load_data(db_name)
        #self.display_table()

    """ загрузка базы данных из csv-файла в словарь """
    def load_data(self, db_name):
        try:
            with open(db_name) as data:
                self.table = from_csv(data)
        except:
            print('Ошибка чтения базы данных.')

    def display_table(self):
        print(self.table)
