# Переменные s1-s9 - "клетки" игрового поля
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
print(list(var_dict.keys()))  # список всех ключей
print(list(var_dict.values()))  # список всех значений
for i in var_dict:
    print(i)