def string_splitter(math_string):
    pass


def number_checker(math_string, index):
    left_index = 0
    right_index = 0
    for i in range(index):
        if not (0 <= ord(math_string[index - i]) <= 9):
            left_index = i
    for i in range(index):
        if not (0 <= ord(math_string[index + i]) <= 9):
            right_index = i
    return left_index, right_index


def math_string_calculator(math_string):
    math_string = math_string.replace(' ', '')
    if not ('*' in math_string or '/' in math_string or '+' in math_string or '-' in math_string):
        print('работает')
        return 1
    if '*' in math_string:
        index = math_string.find('*')
        l_index, r_index = number_checker(math_string, index)
        return 1
    if '/' in math_string:
        index = math_string.find('/')
        pass
    if '+' in math_string:
        index = math_string.find('+')
        pass
    if '-' in math_string:
        index = math_string.find('-')
        pass
    print(math_string)
