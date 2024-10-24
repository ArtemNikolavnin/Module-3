def calculate_structure_sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (list, tuple, set)):
            total_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            for key, value in arg.items():
                if isinstance(key, str):
                    total_sum += len(key)
                if isinstance(value, (int, float)):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                elif isinstance(value, (list, tuple, set, dict)):
                    total_sum += calculate_structure_sum(*value)
        else:
            pass
    return total_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)