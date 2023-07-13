# # Работа в консоли в режиме интерпретатора Python.
# # Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
#
# n = int(input('vvedi a '))
# e = int(input('vvedi e 10'))
# i = 0
# summ = 0
# while i <= n:
#     if i % e != 0:
#         summ += i
#     i += 2
#
# print(summ)
# __________--------------------------------


# # Напишите программу, которая запрашивает год и проверяет его на високосность.
# # Распишите все возможные проверки в цепочке elif
# # Откажитесь от магических чисел
# # Обязательно учтите год ввода Григорианского календаря
# # В коде должны быть один input и один print
#
# year = int(input('vvedi god '))
#
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     result ='obichnii'
# else:
#     result = 'visokos'
#
# print(result)
# --------------------------------------------------------


# #
# # нарисовать Елку
#
#
# num = int(input('vvedi kolisestvo radov '))
#
# for i in range(1, num + 1):
#     print(" " * (num - i) + "*" * (2 * i - 1))

#---------------------------------------------------------

#НАРИСОВАТЬ ТАБЛИЦУ УМНОЖЕНИЯ

for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j} X {i} = {i*j}", end='\t\t')
    print()
print()
for k in range(2, 11):
    for l in range(6, 10):
        print(f"{l} X {k} = {k*l}", end='\t\t')
    print()