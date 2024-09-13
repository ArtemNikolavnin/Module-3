def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    
print_params()
print_params(2, 3)
print_params(8)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (10, 'месяц', True)
values_dict = {'a': 15, 'b': 'год', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = (10, 'день')

print_params(*values_list_2, 42)