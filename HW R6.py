#Name:gregg
#Class: 6th Hour
#Assignment: HW-R6


#1. Create a def function that prints out "Hello World!". Call the function.
def hello_world():
    print("Hello World!")

#2. Create a def function that prints your name. Call the function with the name as the argument.
def name(your_name):
    print(your_name)

#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.
def avg_list(list):
    print(sum(list) / len(list))

#4. Call the function from #3 but with a new list of different numbers.

#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, print x, make z equal the sum of x and y, make x equal y, then y equal z.
def conf (x,y):
    for i in range(1,11):
        print(x)
        z = x+y
        x = y
        y = z

#6. Call the function from #5 with the arguments for x and y being 0 and 1.
hello_world()
name("gregg")
avg_list([1,2,3,4,5,6])
avg_list([3,1,4,1,5,9])
conf(0,1)