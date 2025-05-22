"""
Модуль работы с базой данных
Программист: Казакова Оксана ст. гр.444
Проверил: 
Дата написания: 08.04.2025
"""

from prettytable import PrettyTable

def add(bd: dict) -> dict:
    """
    Функция добавления нового ученика в базу данных
    bd - база данных
    """
    print(bd)
    last_name = input('Введите фамилию ученика: ')
    first_name = input('Введите имя ученика: ')
    gender = input('Введите пол (м/ж): ').lower()
    while gender not in ['м', 'ж']:
        gender = input('Введите корректный пол (м/ж): ').lower()
    
    weight = input('Введите вес ученика: ')
    while not weight.replace('.', '', 1).isdigit():
         weight = input('Введите корректный вес: ')
    weight = float(weight)
    
    height = input('Введите рост ученика: ')
    while not height.replace('.', '', 1).isdigit():
         height = input('Введите корректный рост: ')
    height = float(height)

    bd[(last_name, first_name)] = {'пол': gender, 'вес': weight, 'рост': height}
    print('Запись добавлена успешно.')
    return bd

def search(bd: dict) -> None:
    """
    Поиск записи по фамилии и имени ученика
    bd - база данных
    """
    last_name = input('Введите фамилию ученика: ')
    first_name = input('Введите имя ученика: ')
    
    if (last_name, first_name) in bd:
        student = bd[(last_name, first_name)]
        print(f"ФИО: {last_name} {first_name}, Пол: {student['пол']}, Вес: {student['вес']} кг, Рост: {student['рост']} см")
    else:
        print('Ученик не найден в базе данных.')

def delete(bd: dict) -> dict:
    """
    Удаление записи по фамилии и имени ученика
    bd - база данных
    """
    last_name = input('Введите фамилию ученика, которого хотите удалить: ')
    first_name = input('Введите имя ученика: ')
    
    if (last_name, first_name) in bd:
        del bd[(last_name, first_name)]
        print(f"Запись ученика {last_name} {first_name} удалена.")
    else:
        print('Ученик не найден в базе данных.')
    return bd

def prnt(bd: dict) -> None:
    """
    Функция вывода базы данных в виде таблицы
    bd - база данных
    """
    table = PrettyTable()
    table.field_names = ['ФИО', 'Пол', 'Вес', 'Рост']
    for fio, data in bd.items():
        table.add_row([f"{fio[0]} {fio[1]}", data['пол'], data['вес'], data['рост']])
    print(table)
