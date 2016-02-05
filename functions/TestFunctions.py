__author__ = 'ravi'

import random

def personName(number):
    if number == 1:
        return 'XYZ'
    elif number == 2:
        return 'ABC'
    elif number == 3:
        return 'FGH'
    elif number == 4:
        return 'JKL'
    elif number == 5:
        return 'RST'
    elif number == 6:
        return 'LMN'
    else:
        return 'Invalid number'

r = random.randint(1,9)
print(personName(r))

print('Hello', end='')
print('World')

print('Hello1', 'World1')

print('cats', 'dogs', 'mice', sep=',')