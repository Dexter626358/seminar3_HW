"""Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей."""

friends_items = {
    'Андрей': ('палатка', 'спальник', 'рюкзак'),
    'Борис': ('еда', 'вода', 'плеер', 'палатка', 'спальник', 'кружка'),
    'Виталий': ('топор', 'нож', 'фонарик', 'палатка', 'спальник', 'кружка')
}


def common_staff(dictionary):
    list_value = list(dictionary.values())
    length = len(list_value)
    set_1 = set(list_value[0])
    set_all = set()
    for i in range(1, length):
        for j in list_value[i]:
            set_all.add(j)
    return set_1 & set_all


def print_set(set_to_print):
    common_elms = ""
    for el in set_to_print:
        common_elms += el + ", "
    return common_elms[:-2]


def unique_staff(dictionary):
    list_value = list(dictionary.values())
    all_elements = set()
    for el in list_value:
        for j in el:
            all_elements.add(j)
    common_elements = common_staff(friends_items)
    unique_elms = all_elements - common_elements
    return unique_elms


def except_one_fiend(dictionary):
    key_list = [key for key in dictionary]
    value_list = [value for value in dictionary.values()]
    for ind, val in enumerate(key_list):
        copy_values = value_list.copy()
        one_friend = set(copy_values.pop(ind))
        other_friends = set(copy_values[0])
        for i in range(1, len(copy_values)):
            other_friends &= set(copy_values[i])
        if other_friends - one_friend:
            thing = other_friends - one_friend
            lost_thing = str(thing)
            return f"У {val} отсутсвует: {lost_thing[2:-2]}."


common_elements = common_staff(friends_items)
print(f"Все друзья взяли с собой следующие вещи: {print_set(common_elements)}.")
unique_elms = unique_staff(friends_items)
print(f"Уникальные вещи друзей: {print_set(unique_elms)}.")
print(except_one_fiend(friends_items))