import time  # Библиотека time для выставления задержек
import random  # Библиотека random для случайных фраз обработки неправильных пунктов меню

print("Добро пожаловать в игру 'Крестики-нолики'")
print("created by stonecode27")

# Переменная main_menu - текст главного меню
main_menu = """
\u2554\u2550\u2550\u2550\u2550\u2550\u2550
\u2551\t\u058e Главное меню \u058e
\u2551 Отправьте "старт", чтобы начать игру
\u2551 Отправьте "правила", чтобы узнать правила игры
\u2551 Отправьте "выход", чтобы выйти из программы

"""
# Переменная menu - текст приглашения коммандной строки
menu = ">"

# Переменная rules - текст правил игры
rules = """
        
Игроки ходят поочереди.
Первыми ходят крестики (х). 
Чтобы поставить "х" или "о"
отправьте адрес поля в формате "ху",
где "х" номер столбца,
а "y" номер строки.

        """
# Переменная var_dict - словарь с адресами клеток игрового поля и их значениями
var_dict = {"00": "#", "10": "#", "20": "#",
            "01": "#", "11": "#", "21": "#",
            "02": "#", "12": "#", "22": "#"
            }
# Переменная playing_field - форматированная строка игрового поля
playing_field = f"""  
              0 1 2
            0 {var_dict["00"]} {var_dict["10"]} {var_dict["20"]}
            1 {var_dict["01"]} {var_dict["11"]} {var_dict["21"]}
            2 {var_dict["02"]} {var_dict["12"]} {var_dict["22"]}

                        """
# Переменная turns - текст-приглашение коммандной строки сделать ход в игре
turns = "Отправьте адрес поля \n >"
# Переменная address_error - текст ошибки неправильного адреса клетки
address_error = "Поля с таким адресом не существует!"
# Переменная round_count cчитает ходы, принимает стартовое значение 1
round_count = 1
# Список значений словаря var_dict
list_of_values = list(var_dict.values())
# Переменная finish - индикатор конца игры
finish = None


# Цикл, вызывающий главное меню
while True:
    print(main_menu)  # вывод главного меню
    navigation = input(menu)  # инициация ввода
    if navigation == "правила":  # если ввели "правила"
        print(rules)   # Вывести правила
        time.sleep(10)  # Задержка на показ правил и возвращение в главное меню
    elif navigation == "старт":  # если ввели "старт"
        print("Начало игры.")
        print(f"Ход {round_count}. Ходят 'х'")  # вывод сообщения раунда
        print(playing_field)  # вывод стартового поля
        x_or_o = "x"  # переменная, обозначающая крестик или нолик в зависисоти от очередности хода. В начале "x"
        while True:  # Цикл While с постусловием на проверку результата
            address = input(turns)  # ввести адресс ячейки
            if address in var_dict:  # проверка на корректность введенного адреса
                for i in var_dict:  # итерация по словарю var_dict
                    if i == address:  # Если адресс клетки найден
                        if var_dict[i] == "#":  # Если клетка не занята
                            var_dict[i] = x_or_o  # значение по ключу словаря приняло значение переменной x_or_o
                            round_count += 1  # новый раунд, поскольку "поставили" крестик или нолик
                            x_or_o = "o" if round_count % 2 == 0 else "x"  # раунд четный, очередь 'o', иначе 'x'
                            print(f"Ход {round_count}. Ходят '{x_or_o}'")
                            print(f"""  
              0 1 2
            0 {var_dict["00"]} {var_dict["10"]} {var_dict["20"]}
            1 {var_dict["01"]} {var_dict["11"]} {var_dict["21"]}
            2 {var_dict["02"]} {var_dict["12"]} {var_dict["22"]}

                                            """)
                            break
                        else:  # если клетка уже занята
                            print("Клетка уже занята!")
            else:  # если адрес не существует, вывести ошибку
                print(address_error)
            for j in list(var_dict.values()):  # цикл проверки условий окончания игры,
                if list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[1] == j \
                        and list(var_dict.values())[2] == j:  # первая горизонталь
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[0]}'.")
                    break
                elif list(var_dict.values())[3] == j and j != "#" and list(var_dict.values())[4] == j \
                        and list(var_dict.values())[5] == j:  # вторая горизонталь
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[3]}'.")
                    break
                elif list(var_dict.values())[6] == j and j != "#" and list(var_dict.values())[7] == j \
                        and list(var_dict.values())[8] == j:  # третья горизонталь
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[8]}'.")
                    break
                elif list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[3] == j \
                        and list(var_dict.values())[6] == j:  # первая вертикаль
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[6]}'.")
                    break
                elif list(var_dict.values())[1] == j and j != "#" and list(var_dict.values())[4] == j \
                        and list(var_dict.values())[7] == j:  # вторая вертикаль
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[7]}'.")
                    break
                elif list(var_dict.values())[2] == j and j != "#" and list(var_dict.values())[5] == j \
                        and list(var_dict.values())[8] == j:  # третья вертикаль
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[8]}'.")
                    break
                elif list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[4] == j \
                        and list(var_dict.values())[8] == j:  # первая диагональ
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[8]}'.")
                    break
                elif list(var_dict.values())[2] == j and j != "#" and list(var_dict.values())[4] == j \
                        and list(var_dict.values())[6] == j:  # вторая диагональ
                    finish = 1
                    print(f"Конец игры. Победили '{list(var_dict.values())[6]}'.")
                    break
                elif not ("#" in list(var_dict.values())):  # проверка на ничью
                    finish = 1
                    print(f"Конец игры. Ничья.")
                    break

            if not (finish is None):  # Одно из условий окончания игры сработало и изменило переменную finish.
                # Цикл игры завершает работу
                time.sleep(4)  # задержка на возврат в главное меню
                break  # конец цикла игры

    elif navigation == "выход":
        print("Выход из игры...")
        break
    else:  # если ввели пункт, которого нет в меню
        # Переменная - false_menu_list - список фраз для обработки ошибок
        false_menu_list = ["Такого пункта в меню нет!", "Такой пункт отсутствует в меню!", "Не балуйтесь!",
                           "Кажется, так звали какого-то актера. Но такого пункта в меню точно нет!"]
        random.shuffle(false_menu_list)  # метод перемешивает элементы списка
        print(false_menu_list.pop(random.randint(0, len(false_menu_list)-1)))  # выводит случайную фразу из списка
