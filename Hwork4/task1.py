# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
def keys_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, str | int | float | bool | tuple):
            result[value] = key
        else:
            result[str(value)] = key
    return result


print(keys_to_dict(string='STRING',
                   nunber=10,
                   logic=False,
                   user_list=['aaa', 'bbb', 'ccc']
                   ))
