# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # вызов функции без аргументов
print_params(1, 5)  # вызов функции c 2 аргументами
print_params(True, True, False) # вызов функции c 3 аргументами
print_params(b = 25) # вызов функции работает
print_params(c = [1,2,3]) # вызов функции работает

# 2.Распаковка параметров:
values_list = [True, 2, 'задача']
values_dict = {'a' : 1, 'b' : 'строка', "c" : True}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 =['урок', 5]

print_params(*values_list_2, 42) # итог работает