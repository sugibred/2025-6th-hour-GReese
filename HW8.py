#Name:Gregg Reese
#Class: 6th Hour
#Assignment: HW8
import random
#1. Print "Hello World!"
print("Hello World")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
A = random.randint(1,10)
B = random.randint(1,10)
C = random.randint(1,10)
#3. Print A, B, and C on the same line.
print(A, B, C)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if A > 5:
    print("A is greater than 5")
elif A < 5:
    print("A is less than 5")
else:
    print("A is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if B >= 3 and B <= 7:
    print ("B is between 3 and 7")
else:
    print ("B isn't between 3 and 7")
#6. Make an if statement that prints if variable C is even or odd.
if C % 2 == 0:
    print("C is even")
else:
    print("C is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
rando = 3 + random.randint(1,20)

#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if rando > A + B + C:
    print(f"{rando} is greater than {A + B + C}")
elif rando < A + B + C:
    print(f"{rando} is less than {A + B + C}")
else :
    print(f"{rando} is equal to {A + B + C}")