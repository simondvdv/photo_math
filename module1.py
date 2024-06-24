def string_splitter(math_string):
    pass


def number_checker(math_string, index):
    left_index = 0
    right_index = 0
    i = 0
    while True:
        i += 1
        if not math_string[index - i].isdigit() or index - i == 0:
            left_index = i
            break
    i = 0
    while True:
        i += 1
        try:
            if not math_string[index + i].isdigit():
                right_index = i
                break
        except IndexError:
            return left_index, len(math_string) - 1
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

