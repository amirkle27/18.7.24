import random
numbers: list [int] = [random.randint (0,100) for i in range (4)]
print (numbers)
answer: int = int (input("Please enter a number between 1 and 4 [enter -999 to exit"));
while (answer != -999):
    try:
        print (numbers [answer-1])
    except:
        print ("oops, wrong key...")
    answer: int = int(input("Please enter a number between 1 and 4 [enter -999 to exit"));

