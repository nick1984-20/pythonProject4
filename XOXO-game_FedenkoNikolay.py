#  создаем пустое поле для игры
pole = [[" ", "1", "2", "3"], ["1", "-", "-", "-"], ["2", "-", "-", "-"], ["3", "-", "-", "-"]]
# for i in range(3):
#     A.append(["-"] * 3)
A = ('\n'.join('\t'.join(map(str, row)) for row in pole))
print(A)
symb = ["X", "O"]
player_1 = input('Игрок 1, Вам необходимо выбрать каким символом Вы будете играть: Х или О: ')
while player_1 not in symb:
    player_1 = input("Вы выбрали не верный символ, попробуйте выбрать между Х и О, еще раз: ")
else:
    print("Отличный выбор!")
    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"
print('Напоминание: Для совершения хода выберите координаты поля, на которое хотите поставить свой символ: ')
# Функция описывающая ход игрока
def player_step(player):
    if player == 1:
        step_result = player_1
    else:
        step_result = player_2
    print(f'Игрок {player} делайте ход.')
    player_step_row = int(input('Введите номер строки: '))
    while player_step_row not in range(1, 4):
        player_step_row = int(input('Не верно! Введите номер столбца еще раз и следите, чтобы он был 1, 2 или 3: '))
        continue
    else:
        player_step_tab = int(input('Введите номер столбца: '))
        while player_step_tab not in range(1, 4):
            player_step_tab = input('Не верно! Введите номер столбца еще раз и следите, чтобы он был 1, 2 или 3: ')
            continue
        else:
            pole[player_step_row][player_step_tab] = step_result
            return print('\n'.join('\t'.join(map(str, row)) for row in pole))
# Условия победы
victory = [bool(pole[1][1] == pole[1][2] == pole[1][3]),
           bool(pole[2][1] == pole[2][2] == pole[2][3]),
           bool(pole[3][1] == pole[3][2] == pole[3][3]),
           bool(pole[1][1] == pole[2][1] == pole[3][1]),
           bool(pole[1][2] == pole[2][2] == pole[3][2]),
           bool(pole[1][3] == pole[2][3] == pole[3][3]),
           bool(pole[1][1] == pole[2][2] == pole[3][3]),
           bool(pole[1][3] == pole[2][2] == pole[3][1]),
           ]
while victory[0] or victory[1] or victory[2] or victory[3] or victory[4] or victory[5] or victory[6] or victory[7] is False:
    player_step(1)
    player_step(2)
    continue
else:
    print(f'ПОБЕДА! Игрок {player} победил!')







player_step(1)
player_step(2)
player_step(1)




# Проверка правильно ли сделан ход, или поле уже занято
# def check_step(func):
#     def wrapper():
#         if pole[player_step_row][player_step_tab] not in symb:
#             func()
#         else:
#             print("Сюда ходить нельзя, сделайте другой выбор")
#     return wrapper
# @check_step
# def player_step_dec(player):
#     if player:
#         step_result = player_1
#     else:
#         step_result = player_2
#     player_step_row = int(input('Введите номер строки: '))
#     while player_step_row not in range(1, 4):
#         player_step_row = int(input('Не верно! Введите номер столбца еще раз и следите, чтобы он был 1, 2 или 3: '))
#     else:
#         player_step_tab = int(input('Введите номер столбца: '))
#         while player_step_tab not in range(1, 4):
#             player_step_tab = input('Не верно! Введите номер столбца еще раз и следите, чтобы он был 1, 2 или 3: ')
#         else:
#             pole[player_step_row][player_step_tab] = step_result
#             return print('\n'.join('\t'.join(map(str, row)) for row in pole))









