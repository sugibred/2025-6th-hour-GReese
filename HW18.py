#Name:Gregg
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def wrl():
    print("hello world")
#2. Create two empty integer variables named "heads" and "tails"
heads=0
tails=0
print("this is heads before",heads)
print("this is tails before",tails)
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin():
    global heads,tails
    for i in range(100):
        flip=random.randint(1,2)
        if flip == 1:
            heads=heads+1
        else:
            tails=tails+1
#4. Call the "Hello world" and "Coin Flip" functions here
wrl()
coin()
print("this is heads",heads)
print("this is tails",tails)
#5. Print the final result of heads and tails here

#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag=["red","blue","green","yellow","pink"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def ben():
    randombean= random.choice(beanbag)
    print(randombean)
    beanbag.remove(randombean)
    print(beanbag)
    recall()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def recall():
    choice=(input("beeny weeny y/n"))
    print (choice)
    if choice == "y":
        ben()
    elif choice == "n":
        print("goodbye")
        exit()
    else:
        print("try again")
        recall()
#9. Call the "Bean Pull" function here
ben()