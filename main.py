"""
Модуль основной программы
Программист: Казакова Оксана ст. гр. 444
Проверил: 
Дата написания: 08.04.2025
"""

from db_manager import DataBaseManager

def select_action():
    print('\n Выберите пункт меню: \n')
    print(' МЕНЮ: '.center(50, '*'))
    print('''
        1. Просмотр всей базы данных
        2. Добавление новых записей
        3. Вычисления: средняя масса мальчиков, средний рост девочек, самый высокий ученик
        4. Поиск записи по фамилии и имени
        5. Удаление записи по фамилии и имени
        6. Выход\n
    ''')
    
    num = input()
    while not num.isdigit() or int(num) not in range(1, 7):
        num = input('Повторите выбор пункта меню: ')
    return num

def main():
    db_manager = DataBaseManager('data.csv')

    num = select_action()
    while num != '6':
        if num == '1':
            db_manager.display_table()
        elif num == '2':
            db_manager.add()
        # elif 3:
        #     calculate.calc(bd)
        # elif 4:
        #     database.search(bd) 
        # elif 5:
        #     bd = database.delete(bd)
        else:
            break
        num = select_action()
    print("Выход из программы.")

if __name__ == "__main__":
    main()
