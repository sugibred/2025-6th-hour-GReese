#Name:Gregg
#Class: 6th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print("Hello World!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
ran1=random.randint(1,10)
ran2=random.randint(1,10)
ran3=random.randint(1,10)
print(ran1,ran2,ran3)
#3. Create a list containing 5 strings listing 5 colors.
colors=["red","blue","green","yellow","pink"]

#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(colors))

#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if ran1<=ran2 and ran1<=ran3:
    print(f"ran1 is the lowest with a number of {ran1}")
if ran2<=ran1 and ran2<=ran3:
    print(f"ran2 is the lowest with a number of {ran2}")
if ran3<=ran1 and ran3<=ran2:
    print(f"ran3 is the lowest with a number of {ran3}")
if ran1 == ran2 == ran3:
    print("they're all the same")
