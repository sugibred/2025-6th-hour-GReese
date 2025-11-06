#Name:Gregg
#Class: 6th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
import time
huzz= 1
while huzz <= 100 :
    if huzz % 3 == 0 and huzz % 5 == 0:
        print("FizzBuzz")
    elif huzz % 3 == 0 :
        print("Fizz")
    elif huzz % 5  == 0 :
        print("Buzz")
    else:
        print(huzz)
    huzz += 1