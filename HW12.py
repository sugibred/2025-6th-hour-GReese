#Name:Gregg
#Class: 6th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i >= 0 :
    print(i)
    i -= 1
else:
    print("hello world")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
e = 1
while e <= 30 :
    if e % 2 == 0 :
        print(e)
    e += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
l = 1
while l <= 30:
    if l % 3 == 0 :
        l += 1
        continue
    print(l)
    l += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
p = 1
while p >= 1 :
    p = (random.randint(1, 6))
    print(p)
    if p == 1 :
        break

#5. Create a while loop that asks for a number input until the user inputs the number 0.
t = 6
while t >= 1 :
    t = int(input("give me a number>"))
    if t > 0 :
        print("try again(try 0)")
        continue
else:
    print("bye")
