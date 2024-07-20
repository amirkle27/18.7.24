#a
print ("*a*")
print()

temps : list = []
temp = None;
MaxTemp: float = None;
MinTemp: float = None;
sum: float = None;

#b
print ("*b*")
print()

temp: float = float (input("Please enter the temperature [Enter -999 to Exit]"));
MaxTemp = temp;
MinTemp = temp;
sum = temp
while temp != None and temp != -999.0:
    if -50<temp<50:
        temps.append (temp)
        if temp > MaxTemp:
            MaxTemp = temp
        elif temp < MinTemp:
            MinTemp = temp;
    temp: float = float(input("Please enter the temperature [Enter -999 to Exit]"));
    if (-50 < temp < 50):
        sum = sum + temp

#c
print ("*c*")
print()

New_Numbers: list = [-20.0, 39.1, 18.5 ]
temps.extend(New_Numbers)

#d
print ("*d*")
print()

NewMax: float = max (temps)

#e
print ("*e*")
print()

NewMin: float = min (temps)
print (f"The highest temperature is {NewMax}") #FOR ORIGINAL MAX --> if MaxTemp != -999 else "No Max temperature");
print (f"The lowest temperature is {NewMin}") #FOR ORIGINAL MIN --> if MinTemp != -999 else "No Min temperature");
New_Sum: float = (sum -20.0 + 39.1 + 18.5)

#f
print ("*f*")
print()

avg: float = (New_Sum/(len(temps)));
print (f"The average temperature is {avg : .2f}");
import statistics

#g
print ("*g*")
print()

print (f"the temps mean is {statistics.mean(temps) : .2f}")

#h
print ("*h*")
print()

del temps [0]

#i
print ("*i*")
print()

temps.remove (18.5)

#j
print ("*j*")
print()

temp_last: float = temps.pop (-1)

#k
print ("*k*")
print()

clone_temps = temps.copy ()

#l
print ("*l*")
print()

clone_temps.sort ()

#m

# - - - - The difference between 'sort' and 'sorted' is that 'sorted doesn't change the list,/    #m
#           only shows it in a sorted way
clone_temps_2 = temps.copy()
clone_temps_2.sort (reverse = True)


#n
# - - - - The 'reversed' function is of 'iterator'sort./
#           in order to turn it to a list, we should type:
#               list(reversed(numbers)).



