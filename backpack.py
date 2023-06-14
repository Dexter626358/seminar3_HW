"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
 Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
 *Верните все возможные варианты комплектации рюкзака."""
import random

camping_dict = {
    "tent": 3.5,
    "sleeping bag": 1.2,
    "backpack": 1.8,
    "stove": 0.9,
    "water filter": 0.3,
    "flashlight": 0.2,
    "camera": 1.2,
    "deodorant": 0.4
}

status = False
weights = [value for value in camping_dict.values()]
sum_weights = sum(weights) * 10
camping_staff = [thing for thing in camping_dict.keys()]
weight_backpack = random.randint(1, sum_weights) / 10
print(f"Вес рюкзака: {weight_backpack}", "\n")


def generate_combinations(items):
    if len(items) == 0:
        return [[]]
    else:
        first_item = items[0]
        rest_items = items[1:]
        combinations_without_first = generate_combinations(rest_items)
        combinations_with_first = []
        for combo in combinations_without_first:
            combinations_with_first.append(combo + [first_item])
        return combinations_without_first + combinations_with_first


combinations = generate_combinations(weights)
count = 1
for succes_comb in combinations:
    if weight_backpack == sum(succes_comb):
        print(f"Вариант {count}: ")
        count += 1
        for key, value in camping_dict.items():
            if value in succes_comb:
                print(key, value, sep=" - ")
        print()
        status = True
if not status:
    print("Успешных комбинаций не найдено")






