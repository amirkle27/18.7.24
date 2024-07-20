#a#
print ("*a*")
print()

numbers: list [int] = ([i for i in range (95,106)]);
print(numbers);
print()

#b#
print ("*b*")
print()

even_numbers: list [int] = ([i for i in range (10,21,2)] );
print (even_numbers)

#c#
print ("*c*")
print()

import random
statements: list [bool] = [random.choice ([True,False]) for _ in range (5)];
print(statements)

#d#
print ("*d*")
print()

print ("We should use '_' as a variable when there is no actual use for the memory cell of '_' \
\nand we only use it to perform the action. If there is further use of the memory cell,  \
\nwe should define it as a letter, for example: 'i'." )

#e#
print ("*e*")
print()

import random
random_numbers: list [int] = [random.randint (1,101) for _ in range (10)]
print (random_numbers)

#f#
print ("*f*")
print()

random_numbers_New: list [int] = [b for b in random_numbers if b>50]
print (random_numbers_New)

#g#
print ("*g*")
print()

import random
random_numbers_3: list [int] = [n for n in (random.randint (1,101)  for _ in range (10)) if n >50]
print(random_numbers_3)

#h#
print ("*h*")
print()

string: list [str] = [s for s in (str(input ("please enter a string"))) if not (s=="t" or (s == " "))]
print(string)




