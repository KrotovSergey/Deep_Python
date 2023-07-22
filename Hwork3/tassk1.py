# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

print(my_list := [1, 1, 2, 2, 3, 3, 3, 4, 4, 4])

result_list = []
i = 0

while i < len(my_list):
    if my_list.count(my_list[i]) > 1:
        result_list.append(i)
    else:
        i += 1
print(result_list)
