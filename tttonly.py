s1, s2, s3, s4, s5, s6, s7, s8, s9 = "#", "#", "#", "#", "#", "#", "#", "#", "#"
var_dict = {"00": s1, "10": s2, "20": s3,
            "01": s4, "11": s5, "21": s6,
            "02": s7, "12": s8, "22": s9
            }
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
# Переменная round_count cчитает ходы, принимает стартовое значение
round_count = 1
# Список значений словаря var_dict
list_of_values = list(var_dict.values())
# Переменная finish - индикатор конца игры
finish = None

print("Начало игры.")
print(f"Ход {round_count}. Ходят 'х'")  # вывод сообщения раунда
print(playing_field)  # вывод стартового поля
x_or_o = "x"  # переменная, обозначающая крестик или нолик в зависисоти от очередности хода. В начале "x"
while True:  # Цикл While с постусловием на проверку результата
    address = input(turns)  # ввести адресс ячейки
    if address in var_dict: # проверка на корректность введенного адреса
        for i in var_dict:  # итерация по словарю var_dict
            if i == address:  # Если адресс клетки найден
                if var_dict[i] == "#":  # Если клетка не занята
                    var_dict[i] = x_or_o  # значение по ключу словаря приняло значение переменной x_or_o
                    round_count += 1  # новый раунд, поскольку "поставили" крестик или нолик
                    x_or_o = "o" if round_count % 2 == 0 else "x"  # если раунд четный, то очередь ноликов, иначе крестиков
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
        if list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[1] == j\
                and list(var_dict.values())[2] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[0]}'")
            break
        elif list(var_dict.values())[3] == j and j != "#" and list(var_dict.values())[4] == j\
                and list(var_dict.values())[5] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[3]}'")
            break
        elif list(var_dict.values())[6] == j and j != "#" and list(var_dict.values())[7] == j\
                and list(var_dict.values())[8] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[8]}'")
            break
        elif list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[3] == j\
                and list(var_dict.values())[6] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[6]}'")
            break
        elif list(var_dict.values())[1] == j and j != "#" and list(var_dict.values())[4] == j\
                and list(var_dict.values())[7] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[7]}'")
            break
        elif list(var_dict.values())[2] == j and j != "#" and list(var_dict.values())[5] == j\
                and list(var_dict.values())[8] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[8]}'")
            break
        elif list(var_dict.values())[0] == j and j != "#" and list(var_dict.values())[4] == j\
                and list(var_dict.values())[8] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[8]}'")
            break
        elif list(var_dict.values())[2] == j and j != "#" and list(var_dict.values())[4] == j\
                and list(var_dict.values())[6] == j:
            finish = 1
            print(f"Конец игры. Победили '{list(var_dict.values())[6]}'")
            break
        elif not ("#" in list(var_dict.values())):
            finish = 1
            print(f"Конец игры. Ничья")
            break

    if not (finish is None):  # Одно из условий окончания игры сработало и изменило переменную finish.
        # Цикл игры завершает работу
        break
