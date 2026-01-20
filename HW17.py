#Name:Gregg
#Class: 6th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps():
    userinp=int(input("1 for rock, 2 for paper, 3 for scissors:"))
    print(userinp)
    if userinp < 1 or userinp > 3:
        print ("invalid answer")
        rps()
    rpsbot=random.randint(1,3)
    print(f"you chose {userinp}")
    print(f"david chose {rpsbot}")
    if userinp == 3:
        if rpsbot ==1:
            print ("you lose")

        elif rpsbot == 2:
            print ("you win")

        else:
            print ("It's a draw")

    elif userinp == 2:
        if rpsbot ==3:
            print ("you lose")

        elif rpsbot == 1:
            print ("you win")

        else:
            print ("It's a draw")

    elif userinp == 1:
        if rpsbot ==2:
            print ("you lose")

        elif rpsbot == 3:
            print ("you win")

        else:
            print ("It's a draw")


    restart()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def restart():
    answer = input ("do you want to play again y/n?")
    if answer == "y":
        rps()
    elif answer == "n":
        exit()
    else:
        print("invalid input")
        restart()

rps()