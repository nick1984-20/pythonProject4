# # функция как тип
# def say_hello():
#     print('hello')
# def say_goodbye():
# message = say_hello
# message()
# message = say_goodbye()
# message()

# def sum(a, b):
#     return a + b
# def mult(a,b):
#     return a * b
# operation = sum
# result = operation(5,6)
# print(result)

# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(1)

# факториал числа
# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
# print(fact(4))

# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return check(n-2)
# n = int(input('vvedite chislo '))
# if (check(n) == True):
#     print('chislo chetnoe')
# else:
#     print('chislo nechetnoe')


# генератор списка
# a = [i ** 2 for i in range(1,6)]
# print(a)
#
# a_nod = list(map(int, a))
# print(a_nod)

# выражение генератор
# a = (i ** 2 for i in range(1,6))

# s = [1, 2, 3]
# d = iter (s)
# print(next(d))

# c = (i for i in range(100000000))
# for i in c:
#     print(i)

# def cube_numbers(nums):
#     cube_list = []
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
# print(cube_numbers([1, 2, 3, 4, 5]))

# def cube_numbers(nums):
#     for i in nums:
#         yield(i**3)
# cube = cube_numbers([1, 2, 3, 4, 5])
# print(next(cube))
# print(next(cube))
# print(next(cube))

# декоратор
# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
# def my_func():
#     print('тут основная функция')
# my = my_decor(my_func)
# my()

# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
# @my_decor
# def my_func(number):
#     print(number**2)
# my_func(10)

# number = 111115222222222222225
# digitToFind = 5
# if str(digitToFind) in str(number):
#    print(f"{digitToFind} is in number {number}")

# def print_2_add_2():
#     result = 2+2
#     print(result)
# print_2_add_2()

# def hello_world():
#     print('Hello world!')
# hello_world()
#
# def char_frequency(text):
#     text = text.lower()
#     text = text.replace(" ", "")
#     text = text.replace("\n", "")
#
#     count = {}
#     for char in text:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     for char, cnt in count.items():
#         print(f"Символ {char} встречается {cnt} раз")

# # 4.2.3
# def delitel(n, a):
#     if a % n == 0:
#         print(n, "delitel chisla", a)
#     else:
#         print(n, "nedelitel chisla", a)

# 4.2.4
# def obr_lesenka(n):
#     for i in range(n, 0, -1):
#         print('*'*i)

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))

# 4.2.5
# def qnt_delit(a):
#     count = 0
#     for i in range(1, a+1):
#         if a % i == 0:
#            count += 1
#     return count
#
# print(qnt_delit(4))

# 4.2.6
# def check_palindrome(text):
#     text = text.lower()
#     text = text.replace(" ", "")
#     if text == text[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome("test"))  # False
# print(check_palindrome("Кит на море не романтик"))  # True

# x = 3
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
# func()
# print(x)

# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(5))  # 5 * 2

# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6

# def mult(*num):
#     p = 1
#     for n in num:
#         p *= n
#     return p
# print(mult(1, 2, 3, 4))

# def incorrect_func(name_arg=[]):
#    # name_arg является локальной переменной
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()
#
# # Аргумент до изменения []
# # Аргумент после изменения [1]
# # -----
# # Аргумент до изменения [1]
# # Аргумент после изменения [1, 1]

# установим аргумент name_arg пустым а внутри функции будем проверять его
# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([123])
# print('-----')
# correct_func(name_arg=[123])

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)

# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#     return sum_
# print(adder())
# print(adder(1, 2, 3))

# def mult(*nums):
#     mul_ = 1
#     for n in nums:
#         mul_ *= n
#     return mul_
# print(mult())
# print(mult(1, 2, 3))

# def rec_fibb(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return rec_fibb(n-1) + rec_fibb(n-2)

# def sumn(n):
#     if n == 1:
#         return 1
#     return n + sumn(n-1)
# print(sumn(5))

# def reverse_str(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + reverse_str(string[:-1])
# print(reverse_str('swing'))

# def sum_n(N):
#     if N < 10:
#         return N
#     else:
#         return N % 10 + sum_n(N // 10)
# print(sum_n(1234))

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

# def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         value = list_values.pop(0)
#         list_values.append(value)
#         yield value
# for i in repeat_list([1, 2, 3]):
#     print(i)
# =====================
# import time
#
#
# def decorator_time(fn):
#    def wrapper():
#        # print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        # print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 100000078760 ** 12657
#
#
# def in_build_pow():
#    return pow(10000000566665433, 12676)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
# N, pow_2_count, in_build_pow_count = 100, 0, 0
# for _ in range(N):
#     pow_2_count += pow_2()
#     in_build_pow_count += in_build_pow()
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {pow_2_count / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {in_build_pow_count / N:.10f}")
# ===================
# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# ================================
# def count_func(fn):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         fn(*args, **kwargs)
#         count += 1
#         print(f"Функция {fn} была вызвана {count} раз")
#     return wrapper
# @count_func
# def say_word(word):
#     print(word)
# ================================
# def cache(func):
#     cache_dict = {}
#     def wrapper(num):
#         nonlocal cache_dict
#         if num not in cache_dict:
#             cache_dict[num] = func(num)
#             print(f"Добавление результата в кэш: {cache_dict[num]}")
#         else:
#             print(f"Возвращение результата из кэша: {cache_dict[num]}")
#         print(f"Кэш {cache_dict}")
#         return cache_dict[num]
#     return wrapper
# ================================
