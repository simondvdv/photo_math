from module1 import *

test_string1 = '2 + 13 * 415'
test_string2 = '(1 + 2) * (3 + 4)'
test_string3 = '2 * (3 + 4 * (5 - 2))'

# print(math_string_calculator(test_string1))
# print(test_string3[-2].isdigit())
test_string1 = test_string1.replace(' ', '')
print(number_checker(test_string1, 1))
print(number_checker(test_string1, 4))
