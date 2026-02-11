#Name:Gregg
#Class: 6th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import Hello_World, calc, animal_list, loop
#2. Call the functions here and run HW19
Hello_World()
calc(1,2,3)
animal_list("dog","cat","mouse","Horse","Zebra")
loop(6)
#3. Delete all calls for problem 5 in HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num=int(input("give me a number:"))
    print(100/num)
except ZeroDivisionError:
    print("you can't divide by zero")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    num=int(input("give me a number again:"))
except ValueError:
    print("that's not a number")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
count=5
while count>0:
    print(count)
    count-=1
raise Exception("it's at zero now leave")