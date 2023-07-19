from fractions import Fraction

num_zadacha = int(input('какую задачу проверить? (их всего 2)  '))
match num_zadacha:
    case 1:
        # Напишите программу, которая получает целое число
        # и возвращает его шестнадцатеричное строковое представление.
        # Функцию hex используйте для проверки своего результата.

        result = ""
        number = int(input("введите целое число: "))
        init_number = number
        base = 16

        while number > 0:
            match (number % base):
                case 10:
                    add = "a"
                case 11:
                    add = "b"
                case 12:
                    add = "c"
                case 13:
                    add = "d"
                case 14:
                    add = "e"
                case 15:
                    add = "f"
                case _:
                    add = str(number % base)

            result = add + result
            number = number // base
        print(init_number, "в шестнадцатерично системе = ", result)

        print("проверка", hex(init_number)[2:])

    case 2:

        # Напишите программу, которая принимает две строки вида “a/b”
        # - дробь с числителем и знаменателем.
        # Программа должна возвращать сумму и произведение* дробей.
        # Для проверки своего кода используйте модуль fractions

        def gcd_user(a, b):
            while b != 0:
                a, b = b, a % b
            return a


        print("слоджение и умножение натуральных дробей")
        numerator1, denominator1 = input("введите первую натуральную дробь вида a/b: ").split("/")
        numerator2, denominator2 = input("введите вторую натуральную дробь вида a/b: ").split("/")

        numerator1 = int(numerator1)
        denominator1 = int(denominator1)
        numerator2 = int(numerator2)
        denominator2 = int(denominator2)

        # проводим сложение двух дробей
        summ_num = numerator1 * denominator2 + numerator2 * denominator1
        summ_denom = denominator2 * denominator1

        res_summ_num = int(summ_num / gcd_user(summ_num, summ_denom))
        res_summ_denom = int(summ_denom / gcd_user(summ_num, summ_denom))

        print(f"сумма двух дробей = : {res_summ_num}/{res_summ_denom}")
        print("проверка методом Fractions: ", Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2))

        # проводим умножение  двух дробей
        mult_num = numerator1 * numerator2
        mult_denom = denominator2 * denominator1

        res_mult_num = int(mult_num / gcd_user(mult_num, mult_denom))
        res_mult_denom = int(mult_denom / gcd_user(mult_num, mult_denom))

        print(f"произведение двух дробей = : {res_mult_num}/{res_mult_denom}")
        print("произведение методом Fractions: ",
              Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2))
