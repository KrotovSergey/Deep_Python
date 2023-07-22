# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things = {}
things["еда"] = 3
things["вода"] = 2
things["одежда"] = 3
things["инвентарь"] = 4
things["палатка"] = 5
things["еда2"] = 3
things["вода2"] = 2
things["одежда2"] = 3
things["инвентарь2"] = 4
things["палатка2"] = 5

taken_things = []

max_weight = int(input('введи макс вес рюкзака:  '))

weight_left = max_weight

for key in things:
    if weight_left - things.get(key) >= 0:
        taken_things.append(key)
        weight_left -= things.get(key)

if not taken_things:
    print("в рюкзак ничего не влезло")
else:
    print(f"в рюкзак поместилось {taken_things}")
