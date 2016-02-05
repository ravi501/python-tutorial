__author__ = 'ravi'

import	random
messages	=	['It	is	certain',
				'It	is	decidedly	so',
				'Yes	definitely',
				'Reply	hazy	try	again',
				'Ask	again	later',
				'Concentrate	and	ask	again',
				'My	reply	is	no',
				'Outlook	not	so	good',
				'Very	doubtful']
print(messages[random.randint(0,	len(messages)	-	1)])

#multiple assignment
one, two, three, four, five, six, seven, eight, nine = messages

#test multiple assignment
print('One = ' + one)

testList = [1, 2, 3] + ['A', 'B', 'C']

print(testList)

list = [1,2,3]

print(testList)
print(list.index(2))

list.append(4)
print(list)
list.insert(2, 5)
print(list)
list.remove(3)
print(list)

print(messages[1:3])
print(len(messages))
