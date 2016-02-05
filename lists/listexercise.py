__author__ = 'ravi'

spam = ['apples', 'bananas', 'tofu', 'cats']

spamString = ""

print(len(spam))

for i in range(0, len(spam)):
    if i == 0:
        spamString = spamString + spam[i]
    elif i == len(spam) - 1:
        spamString = spamString + ", and " + spam[i]
    else:
        spamString = spamString + ", " + spam[i]

print(spamString)


grid	=	[['.',	'.',	'.',	'.',	'.',	'.'],
			 ['.',	'O',	'O',	'.',	'.',	'.'],
			 ['O',	'O',	'O',	'O',	'.',	'.'],
			 ['O',	'O',	'O',	'O',	'O',	'.'],
			 ['.',	'O',	'O',	'O',	'O',	'O'],
			 ['O',	'O',	'O',	'O',	'O',	'.'],
			 ['O',	'O',	'O',	'O',	'.',	'.'],
			 ['.',	'O',	'O',	'.',	'.',	'.'],
			 ['.',	'.',	'.',	'.',	'.',	'.']]

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        print(grid[i][j], end='')
