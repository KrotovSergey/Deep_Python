num_zadacha = int(input('какую задачу проверить? (их всего 3)  '))
match num_zadacha:
    case 1:
        # Задание No1
        # Треугольник существует только тогда, когда сумма любых двух его сторон больше
        # третьей. Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить
        # длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае
        # отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
        # существует.
        # Отдельно сообщить является ли треугольник разносторонним, равнобедренным или
        # равносторонним.

        print('Введите длины сторон треугольника: ')
        a, b, c = float(input('a = ')), \
            float(input('b = ')), \
            float(input('c = '))

        if a < b + c and \
                b < a + c and \
                c < a + b:
            print('Треугольник существует')
            if a == b == c:
                print('Треугольник равносторонний')
            elif a == b or b == c or a == c:
                print('Треугольник равнобедренный')
            else:
                print('Треугольник разносторонний')
        else:
            print('Треугольник не существует')

    case 2:

        # Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
        # Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
        # и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

        MIN_LIMIT = 0
        MAX_LIMIT = 100000
        UNITY = 1
        MIN_PRIME_NUM = 2

        input_num = -1

        while not (MIN_LIMIT <= input_num <= MAX_LIMIT):
            input_num = int(input('Введите целое число между'))

        if input_num >= MIN_PRIME_NUM:
            sum = 0
            for i in range(UNITY, input_num + 1):
                if input_num % i == 0:
                    sum += 1
            if sum <= 2:
                print(f'Число {input_num} простое')
            else:
                print(f'Число {input_num} составное')
        else:
            print('Числа 0 и 1 не являются ни простыми, ни составными')
    case 3:

        # Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
        # Программа должна подсказывать «больше» или «меньше» после каждой попытки.
        # Для генерации случайного числа используйте код:
        # from random import randint
        # num = randint(LOWER_LIMIT, UPPER_LIMIT).

        from random import randint

        LOWER_LIMIT = 0
        UPPER_LIMIT = 1000
        ATTEMPT_COUNT = 10

        num = randint(LOWER_LIMIT, UPPER_LIMIT)

        count = 1
        while count <= ATTEMPT_COUNT:
            print(f'Попытка {count}. Введите целое число: ')
            your_num = int(input())

            if your_num == num:
                print('Ура, число угадано')
                break
            elif num < your_num:
                print(f'Загаданное число меньше {your_num}')
            else:
                print(f'Загаданное число больше {your_num}')

            count += 1

        else:
            print('Попытки закончились, число НЕ угадано')
