#Name:
#Class: 6th Hour
#Assignment: HW16
import random
#1. Create a def function that prints out "Hello World!"
def Hello_World():
    print("hello world")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def calc(a,b,c):
    avsum=(a+b+c)/3
    print (avsum)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animals):
    print(animals[2])


#4. Create a def function that loops from 1 to the number put in the argument.
def loop(number):
    for i in range(1,number+1):
        print(i)

#5. Call all of the functions created in 1 - 4 with relevant arguments.
Hello_World()
calc(7,4,9)
animal_list("dog","cat","mouse","Horse","Zebra")
loop(6)
#6. Create a variable x that has the value of 2. Print x
x=2
print (x)
#7. Create a def function that multiplies the value of x by a random number between 1 and 5.
def make_x_random():
    global x
    x=x*random.randint(1,5)
make_x_random()
#8. Print the new value of x.
print(x)