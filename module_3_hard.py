data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, (int, float)):
        summa += data_structure # проверяем и суммируем числа: целые и с плавающей точкой
    elif isinstance(data_structure, str):
        summa += len(data_structure) # проверяем и суммируем строки
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item) # проверяем и суммируем списки, кортежи и множество
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key) # проверяем и суммируем ключи словаря
            summa += calculate_structure_sum(value) # проверяем и суммируем элементы словаря

    return summa

result = calculate_structure_sum(data_structure)
print(result)