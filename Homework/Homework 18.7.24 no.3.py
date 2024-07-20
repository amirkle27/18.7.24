#a#
print ("*a*")
print()

import random
statements: list [bool] = [random.choice ([True, False]) for _ in range (3)];
print(statements);
print()

#b#
print ("*b*")
print()

print (f"All of the statements are 'True'", statements, all (statements));
print()

#c#
print ("*c*")
print()

print (f"There is at least 1 'True' in the list", statements, any (statements))
print()

#d#
print ("*d*")
print()

print (f"The list contains only 'False'", statements, not any (statements))
print()

#e#
print ("*e*")
print()

statements: list [bool] = [True, False, False]
print (f"There is at least 1 'False' in the list", statements, not all (statements));
print()

#f#
print ("*f*")
print()

import random
random_numbers : list [int] = [random.randint (-2,2) for _ in range (10)]
print (random_numbers);
print()

#g#
print ("*g*")
print()

print (f"The list doesn't contain 0", random_numbers, all (random_numbers))
print()

#h#
print ("*h*")
print()

print (f"There is at least one number that isn't 0 in the list", random_numbers, any (random_numbers))
print()

#i#
print ("*i*")
print()

print(f"There are only 0's in the list", random_numbers, not any (random_numbers))
print()

#j#
print ("*j*")
print()

print (f"There is at least one 0 in the list", random_numbers, not all (random_numbers))

