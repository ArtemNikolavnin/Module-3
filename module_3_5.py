def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        for i in range(len(str_number) - 1, -1, -1):
            if str_number[i] != "0":
                return first * get_multiplied_digits(int(str_number[1:i+1]))
    else:
        return first
result = get_multiplied_digits(40203)
print(result)
