__author__ = 'ravi'

#Strings
name = 'Zophie a cat'

print(name[0])

newName = name[0:7] + "the " + name[8:12]
print(newName)



#Tuples - Tuples are immutable where are lists are mutable data types
eggs = ('hello', 42, 0.5)


#Converting type with list and tuple functions
print(list(('hello', 42, 0.5)))

print(tuple(['cat',	'dog',	5]))
