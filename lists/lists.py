__author__ = 'ravi'
import copy

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)


#Copy and decopy functions
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(cheese)
print(spam)

