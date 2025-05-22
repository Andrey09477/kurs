"""
Модуль работы с текстовым файлом
Программист: Казакова Оксана, ст. гр.444
Проверил: 
Дата написания: 08.04.2025
"""

def read() -> dict:
    """
    Функция чтения базы данных из текстового файла в словарь
    bd - база данных
    """
    try:
        f = open('data.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        print('База данных не найдена.')
        exit(0)
    else:
        bd = dict()
        for line in f:
            s = line.split()
            bd[(s[0], s[1])] = {'пол': s[2], 'вес': float(s[3]), 'рост': float(s[4])}
        f.close()
        return bd
    
   
def write(bd: dict) -> None:
    """
    Процедура записи базы данных из словаря в текстовый файл
    bd - база данных
    """
    f = open('data.txt', 'w', encoding='utf-8')
    text = ''
    for fio in bd.keys():
        text += fio[0] + ' ' + fio[1] + ' ' + bd[fio]['пол'] + ' ' + str(bd[fio]['вес']) + ' ' + str(bd[fio]['рост']) + '\n'
    text = "\n".join(text.split("\n")[:-1])
    f.write(text)
    f.close()