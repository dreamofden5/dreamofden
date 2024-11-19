def average_num(list_num: list) -> float:
    new_list = []

    for el in list_num:
        if isinstance(el, (int, float)):
            new_list.append(el)
        else:
            try:
                converted = float(el)
                new_list.append(converted)
            except ValueError:
                return "Bad request"

    if len(new_list) == 0:
        return "Bad request"


    average = sum(new_list) / len(new_list)


    rounded_average = round(average + 0.000001, 2)

    print(f"Список для расчета: {new_list}, Среднее значение: {rounded_average}")  # Отладочный вывод
    return rounded_average



assert average_num([1, 2, 3, 4, 5]) == 3.00
assert average_num([1.0, 2.5, 3.0, 4.5]) == 2.75
assert average_num([1, 2.5, 3, 4.5]) == 2.75
assert average_num([0, 0, 0, 0]) == 0.00
assert average_num([-1, -2, -3, -4]) == -2.50
assert average_num(["1", "2", "3", "4"]) == 2.50
assert average_num([1, "2", 3.0, "4.5"]) == 2.63
assert average_num([1, "two", 3, "four"]) == "Bad request"
