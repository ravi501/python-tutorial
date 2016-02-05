__author__ = 'ravi'

import sre_constants

myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

print(myCat["size"])

print("My cat has " + myCat["color"] + " color fur")


#Dictionaries are not ordered like lists
spam	=	['cats',	'dogs',	'moose']
bacon	=	['dogs',	'moose',	'cats']
print(spam == bacon)

eggs	=	{'name':	'Zophie',	'species':	'cat',	'age':	'8'}
ham	=	{'species':	'cat',	'age':	'8',	'name':	'Zophie'}
print(eggs == ham)


#keys(), values() and items() methods in dictionaries
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(spam[k])

for i in spam.items():
    print(i)


#get() method in dictionaries
picnicItems = {'apples': 5, 'cups': 2}
print('I am brining ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am brining ' + str(picnicItems.get('eggs', 0)) + ' eggs.' )


#setDefault() method in dictionaries
spam	=	{'name':	'Puma',	'age':	5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white') #this wont change the default value black for color





sre_constants.EX_GRAPH0 = {0: [1, 2], 1: [], 2: []}

