"""
Модуль работы с базой данных
Программист: Казакова Оксана ст. гр.444
Проверил: 
Дата написания: 08.04.2025
"""

import csv
from prettytable import PrettyTable, from_csv
from const import Column, MAX_HEIGHT, MAX_WEIGHT

''' класс упр-я БД (bd) '''
class DataBaseManager:
    table = None
    students = {}
    max_id = 467 # для теста
    
    def __init__(self, db_name):
        self.load_data(db_name)
        #self.display_table()

    """ загрузка базы данных из csv-файла в словарь """
    def load_data(self, db_name):
        try:
            #data = open(db_name, "r")
            with open(db_name) as data:
                #self.students = csv.DictReader(data)
                for row in csv.DictReader(data):
                    params = dict(row)
                    #print(Column.ID.value)
                    id = int(params.pop(Column.ID.value))
                    self.students[id] = params
            with open(db_name) as data:
                self.table = from_csv(data)
            print(self.table)
            print(self.students)
        except:
            print('Ошибка чтения базы данных.')        
            #     #exit(0)
            
    def display_table(self):
        print(self.table)
        #print(self.students)

    """ Функция добавления нового ученика в базу данных """   
    def add(self):     
        last_name = input('Введите фамилию ученика: ')
        first_name = input('Введите имя ученика: ')
        
        gender = input('Введите пол (м/ж): ').lower()
        while gender not in ['м', 'ж']:
            gender = input('Введите корректный пол (м/ж): ').lower()        
        
        weight = input('Введите вес ученика, кг: ')
        while not weight.replace('.', '', 1).isdigit() and weight > MAX_WEIGHT:
            weight = input('Введите корректный вес, кг: ')
        weight = float(weight)        
        
        height = input('Введите рост ученика, см: ')
        while not height.replace('.', '', 1).isdigit() and height > MAX_HEIGHT:
            height = input('Введите корректный рост: ')
        height = float(height)

        self.max_id += 1
        self.students[self.max_id] = {
            Column.LAST_NAME.value: last_name,
            Column.FIRST_NAME.value: first_name,
            Column.GENDER.value: gender,
            Column.HEIGHT.value: height,
            Column.WEIGHT.value: weight,
        }
        print('Запись добавлена успешно.')
        print(self.students)
