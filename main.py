"""
Модуль основной программы
Программист: Казакова Оксана ст. гр. 444
Проверил: 
Дата написания: 08.04.2025
"""

from task import file, menu, database, calculate

bd = file.read()

num = 0
while num != 6:
    num = menu.menu()
    match num:
        case 1:
            database.prnt(bd)
        case 2:
            bd = database.add(bd)
        case 3:
            calculate.calc(bd) 
        case 4:
            database.search(bd) 
        case 5:
            bd = database.delete(bd) 
        case 6:
            print("Выход из программы.")

file.write(bd) 
