#Name:Greg
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a=int(input("Enter a number for a:"))
b=int(input("Enter a number for b:"))
c=int(input("Enter a number for c:"))
#4. Add a and b together, then divide the sum by c. Print the result.
ab=a+b
c_ab=ab / c
print(c_ab)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(c_ab)
if c_ab % 2 == 0:
    print(f"{c_ab} is even")
else:
    print(f"{c_ab} is odd")
#6. Create a list of five different random integers between 1 and 10.
rnd=[random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
print(rnd)
#7. Print the 4th number in the list.
print(rnd[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
rnd.append(random.randint(1,10))
print(rnd)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
rnd.sort()
print(rnd)
print(rnd[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i <= 100:
    print(i)
    i+=i
#11. Create a list containing the names of five other students in the classroom.
Students = ["Ally", "Devon", "Kevin", "Shane", "Greg"]

#12. Create a for loop that individually prints out the names of each student in the list.
for name in Students:
    print(name)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i in range(1, 101):
    print(i)
    if i % 10 == 0:
        break
#14. Free space. Do something creative. :)
import time
for m in range(1, 100001):
    time.sleep(.5)
    print("you are po0py")
