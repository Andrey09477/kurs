"""
Модуль вычислений: средняя масса мальчиков, средний рост девочек и самый высокий ученик
Программист: Казакова Оксана ст. гр.444
Проверил: 
Дата написания: 08.04.2025
"""

def calc(bd: dict) -> None:
    """
    Вычисление средней массы мальчиков и среднего роста девочек
    bd - база данных
    """
    boys_weight = []
    girls_height = []
    highest_student = None

    for fio, data in bd.items():
        # Вычисление самой высокой записи
        if highest_student is None or data['рост'] > highest_student['рост']:
            highest_student = {'fio': fio, 'рост': data['рост']}
        
        if data['пол'] == 'мужской':
            boys_weight.append(data['вес'])
        elif data['пол'] == 'женский':
            girls_height.append(data['рост'])

    if boys_weight:
        avg_weight = sum(boys_weight) / len(boys_weight)
        print(f"Средняя масса мальчиков: {avg_weight:.2f} кг")
    else:
        print("Нет данных о мальчиках.")
    
    if girls_height:
        avg_height = sum(girls_height) / len(girls_height)
        print(f"Средний рост девочек: {avg_height:.2f} см")
    else:
        print("Нет данных о девочках.")
    
    if highest_student:
        print(f"Самый высокий ученик: {highest_student['fio'][0]} {highest_student['fio'][1]}, рост: {highest_student['рост']} см")
