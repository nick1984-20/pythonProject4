# # while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0': break
#     if s in ('+','-','*','/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
# else:
#     print("Неверный знак операции!")
# a = float(input("a="))
# while b != 0:
#     b = float(input("b="))
#     a = a+b
#     print(a)
# x = 0
# y = 0
# while (x!=100):
#    x += 1
#    y += x
# print (y)

# x = 0
# y=0
# for x in range(1, 101):
#     y+=x
# print (y)

# a = [-4, -9, -8, -56, -89, -99, -5]
# count = 0
# for i in a:
#     if i<0:
#         count += 1
# print (count)

# students = [
#     {"name": "Alice", "grades": [95, 87, 91]},
#     {"name": "Bob", "grades": [78, "A", 85]},
#     {"name": "Charlie", "grades": []},
#     {"name": "David", "grades": [92, 88, 90]},
#     {"name": "Eve", "grades": ["B", 95, 84]},
# ]
# порог
# threshold = 90
# for student in students:
#     grades = student.get("grades")
#     if not grades or not all(isinstance(grade, int) for grade in grades):
#         continue #проверка условия и пропуск выполнения дальнейших операций цикла
#     average_grade = sum(grades) / len(grades)
#     if average_grade > threshold:
#         print(student["name"])

# проверить строку за один проход, плиндром ли он
# s = 'А лис, он умен - крыса сыр ему носила'
# start, end = 0, len(s) - 1
# while start < end:
#     startChar, endChar = s[start].lower(), s[end].lower()
#     # проверяем символы, не являющимися буквами или цифрами
#     if startChar.isalnum() and endChar.isalnum():
#         if startChar != endChar:
#             print(False)
#             break
#         else:
#             start, end = start+1, end - 1
#             continue
#         start, end = start + (not starChar.isalnum()), end - (not endChar.isalnum())
#     else:
#         print(True)

# Есть список целых чисел и целевые значения. Вернуть индексы двух элементов списка, которые в сумме дают целевое значение
# nums = [2, 5, 11, 7]
# target = 9
# for i in range(len(nums)):
#     n = target - nums[i]
#     if n in nums[i+1:]:
#         print(i, nums.index(n, i+1))
#         break
# d = {}
# for i in range(len(nums)):
#     m = target - nums[i]
#     if m in d:
#         print(d[m], i)
#         break
#     else:
#         d[nums[i]] = i

# s = 'pila'
# t = 'lipa'
# if len(s) == len(t):
#     d1 = dict()
#     d2 = dict()
#     for i in range(len(s)):
#         if s[i] in d1:
#             d1[s[i]] += 1
#         else:
#             d1[s[i]] = 1
#         if t[i] in d2:
#             d2[t[i]] += 1
#         else:
#             d2[t[i]] = 1
#     print(d1 == d2)
# else:
#     print(False)
# сложение двух словарей, чтобы сохранились все значения
# A = {'a': 1,
#      'b': [2, 4],
#      'c': 3,
#      'd': [10, 1],
#      'e': 10
#      }
# B = {'a': 2,
#      'b': [3, 5],
#      'c': [4, 5],
#      'd': 5,
#      'f': [1, 2]
#      }
# C = A | B
# for key, value in A.items():
#     if key in B:
#         if isinstance(value, list):
#             C[key] = value + B[key] if isinstance(B[key], list) else value + [B[key]]
#         else:
#             C[key] = [value] + B[key] if isinstance (B[key], list) else [value, B[key]]
#     else:
#         C[key] = value
# print(C)
# name = input("Введите название на этикетке")
# if "Арорат" in name:
#     print("Нашлась подделка!")
# else:
#     print(f"Вино {name} не подделка")

# one = 10
# two = 30
# print((one%2 == 0) and (two%2 == 0))

# hour = 7
# if 6 <= hour < 12:
#     print("Утро!!!")
# x=2
# y=3
# if x > 0 and y > 0:
#         print("Первая четверть")
# if x < 0 and y > 0:
#         print("2 четверть")
# if x > 0 and y < 0:
#         print("4 четверть")
# if x < 0 and y < 0:
#         print("3 четверть")

# month = int(input("vvedite nomer mesyatsa ot 1 do 12: "))
# if month in [3, 4, 5]:
#     print("vesna")
# elif month in [6, 7, 8]:
#     print("leto")
# elif month in [9, 10, 11]:
#     print("osen")
# elif month in [12, 1, 2]:
#     print("zima")
#
# speed = int(input("vvedite skorost vetra: "))
# if 1<=speed<=4:
#     print("weak")
# elif 5<=speed<=10:
#     print("moderate")
# elif 11<=speed<=18:
#     print("strong")
# elif 19<=speed:
#     print("hurricane")
# else:
#     print("error")

# A = int(input("vvedite A: "))
# B = int(input("vvedite B: "))
# C = int(input("vvedite C: "))
# print(((A<45) and (B>=45) and (C>=45)) or ((B<45) and (A>=45) and (C>=45)) or ((C<45) and (B>=45) and (A>=45)))

# number = int(input("vvedite A: "))
# print((number < -10 or number > -1) and (number < 2 or number > 15))

# a = 12344321
# a_str=str(a)
# if a_str != a_str[::-1]:
#     print(f"{a} - ne palindrom")
# else:
#     print(f"{a} - palindrom")

# N=246378900050
# N_st=str(N)
# print(int(N_st[0])%2 == 0)

# list_1 = [1, 2]
#
# list_2 = [1, 2, 3]
# val=list_2.pop() # значение, которое мы удалили из списка
#
# print(list_1 == list_2)

# clothes=['t-shirt', 'shorts', 'raincoat', 'coat', 'puffer', 'rubber boots', 'umbrella']
# temperature=int(input("vvedite temperature: "))
# if temperature>0:
#     isRain=input("est osadki? y/n") == "y"
#     if isRain:
#         w_force=input("osadki silnye? y/n") == "y"
# decision = "Не решил что брать. Останусь дома."
# if (temperature>20) and (temperature<30):
#     if isRain:
#         decision = (f"wear {clothes[0]}, {clothes[1]} and {clothes[2]}")
#     else:
#         decision = (f"wear {clothes[0]} and {clothes[1]}")
# elif temperature>0:
#     if isRain:
#         if w_force:
#             decision = (f"wear {clothes[3]}, {clothes[5]} and {clothes[6]}")
#         else:
#             decision = (f"wear {clothes[2]} and {clothes[3]}")
#     else:
#         decision = (f"wear {clothes[3]}")
# else:
#     decision = (f"wear {clothes[4]}")
# print(decision)

# #Запрашиваем ввод температуры
# temperature = int(input("Input temperature: "))
# #для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
# #если температура <0 то про дождь спрашивать бессмысленно
# if temperature > 0:
#    rainy = input("Is rainy: ") == "yes"
# #если идет дождь спросим насколько он серьезный
#    if rainy:
#        heavyRain = input("Is heavy rain: ") == "yes"
# #реализуем логику по схеме
# decision = "Не решил что брать. Останусь дома."
# if (temperature) > 20 and (temperature < 30) :
#    if rainy:
#        decision = "Взять футболку шорты и дождевик"
#    else:
#        decision = "Взять футболку и шорты"
# elif temperature > 0:
#    if rainy:
#        if heavyRain:
#            decision = "Взять пальто, резиновые сапоги и зонт"
#        else:
#            decision = "Взять пальто и дождевик"
#    else:
#        decision = "Взять пальто"
# else:
#    decision = "Взять пуховик"
# #Выведем наше решение на экран
# print(decision)
# S = 0  # это наша переменная-счетчик, в которой мы будем считать сумму чисел
# n = 1  # текущее натуральное число, с которого начинаем складывать натуральные числа
#
# # заводим цикл while, который будет работать пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n-1)
#
# a = 1000.00
# p = 0
# i = 0
# while a < 3000.00:
#     p = a*0.08
#     a = p + a
#     i += 1
#     print(i)
# print(a)

# S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)
# P = 1
# N = int(input("Введите N: "))
# for a in range(1, N+1):
#     P *= a
# print(P)

# n = int(input("Введите n: "))
# a = None
# b = 0
# c = "*"
# print("n = ", n)
# for a in range(1, n+1):
#     b = c*a
#     print(b)

# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)

# На вывод будут распечатаны последовательно элементы матрицы.
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for row in matrix:
#    for element in row:
#        print(element, end = " ")


# ROWS = 3
# COLS = 2
# matrix = [
#     [1, 2]
#    ,[3, 4]
#    ,[5, 6]
# ]
# for i in range(ROWS):
#    for j in range(COLS):
#        print(matrix[i][j], end = " ")
#    print()

# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 1]
# ]
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", min_value_rows) # минимальные элементы
# print("Their indices:", min_index_rows) # их индексы
# print("Maximal elements:", max_value_rows) # максимальные элементы
# print("Their indices:", max_index_rows) # их индексы

# #Напишите цикл, который ищет наибольший элемент в матрице.
# test_matrix = [[1, 2, 356, 3444],
#                [7, -1, 2, 5],
#                [123, 2, -1, 67655]]
# max_value_rows = []
# max_value_matrix = 0
# for row in test_matrix:
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     max_value_rows.append(max_value)
# for max_value_matrix in max_value_rows:
#     for max_value_matrix_index in range(len(max_value_rows)):
#         if max_value_rows[max_value_matrix_index] > max_value_matrix:
#             max_value_matrix = max_value_rows[max_value_matrix_index]
# print(max_value_matrix)

# test_matrix = [[1, 2, 3],
#               [7, -1, 2],
#               [123, 2, -1]]
#
# max = test_matrix[0][0] # берем в качестве точки отсчета любой элемент из матрицы
# for row in test_matrix:
#    for el in row:
#        # если элемент больше максимального, то это новый максимум
#        if el > max:
#            max = el
# print(max)


# Напишите код, который определяет, является ли матрица квадратной
# (то есть количество строк равно количеству столбцов).
# В конце программа должна выводить на экран значение True или False
# в зависимости от заданной матрицы. Используйте матрицу из предыдущей задачи.
# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# print(len(test_matrix[0]) == len(test_matrix))

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")


# list_ = [-5, 2, 4, 8, 12, -7, 5]
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         print("Новый индекс отрицательного числа: ", i)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", i)

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# # text = text.lower() # привели все к нижнему регистру
# # text = text.replace(" ", "") #убрали пробелы
# # text = text.replace("\n", "") #убрали символы перевода строки
# # count = {}  # для подсчета символов и их количества
# # for letter in text:
# #    if letter in count:  # если символ уже встречался, то увеличиваем его количество на 1
# #        count[letter] += 1
# #    else:
# #        count[letter] = 1
# #    for char, cnt in count.items():
# #        print(f"Символ {char} встречается {cnt} раз")
#
# text = text.lower() # привели все к нижнему регистру
# text = text.replace("\n", " ")
# text = text.split()
# count = {}  # для подсчета символов и их количества
# for words in text:
#    if words in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[words] += 1
#    else:
#        count[words] = 1
#    for wrd, cnt in count.items():
#        print(f"слово {wrd} встречается {cnt} раз")


# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# #1
# list_ = [1,2,3,-1,3,2,1,2,3,2,1,0,0,0,-1,2]
# #2
# negate_index = -1
# #3
# negate_value = 0
# #4
# for i, val in enumerate(list_):
# #5
#    if val < 0:
#        #6
#        negate_index = i
#        #7
#        negate_value = val
#        break
# #9
# print(f'{negate_index}: {negate_value}')
# i_n = int(input("vvedite chislo: "))
# i = i_n
# n_5, n_7, n_9 = 0, 0, 0
# while i>1:
#     if (i-5) % 10 == 0:
#         n_5 = n_5+1
#     if (i - 7) % 10 == 0:
#         n_7 = n_7+1
#     if (i - 9) % 10 == 0:
#         n_9 = n_9+1
#
#     i = i//10
# print(f"Число: {i_n} содержит цифру 5 - {n_5} раз, цифру 7 - {n_7} раз и цифру 9 - {n_9} раз")

# n = 1
# while n**2<1000:
#     n += 1
# print (n-1)

# a = ['hello', ['my list', 5], 'world', 5, 6]
# for x in range(3):
#     print(a[x])


