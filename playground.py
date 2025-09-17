import random


yn_answer=input('Do you want to play a game?:')
while True:
    if yn_answer == 'yes':
        rolled_die1=random.randint(1,6)
        print(rolled_die1)
        if rolled_die1 == 1:
            print('you dropped the die in a drain')
            quit()
        else:
            answerplyagn=input('Play Again?:')
            if answerplyagn == 'yes':
                continue
            else:
                exit()