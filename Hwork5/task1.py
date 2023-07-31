# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def path_to_tuple(user_string):
    *a, b = user_string.split("/")
    a = "/".join(a) + "/"
    b, c = b.split(".")
    result = (a, b, c)
    return result


user_string = "D:/Distr/pycharm-community-2022.exe"
print(path_to_tuple(user_string))
