
from random import random
import re
import random
import string


def play_game(playerOpt):
    mylist = ["Rock", "Paper", "Scissors"]

    computer = random.choice(mylist)

    if playerOpt == computer:
        print('You picked', playerOpt, 'and the computer picked', computer)
        print("It was a draw!\n")
        return 0
    elif playerOpt == 'Scissors' and computer == 'Rock':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("Computer won!")
        return 1
    elif playerOpt == 'Rock' and computer == 'Paper':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("Computer won!")
        return 1
    elif playerOpt == 'Paper' and computer == 'Scissors':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("Computer won!")
        return 1

    elif playerOpt == 'Rock' and computer == 'Scissors':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("You won!")
        return 1
    elif playerOpt == 'Paper' and computer == 'Rock':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("You won!")
        return 1
    elif playerOpt == 'Scissors' and computer == 'Paper':
        print('\nYou picked', playerOpt, 'and the computer picked', computer)
        print("You won!")
        return 1

    else:
        print('The value entered is invalid try again\n')
        return 0


played_game = (play_game(input("Play game by typing either Rock, Paper or Scissors\n").capitalize()))

while played_game == 0:
    played_game = (play_game(input("Play game by typing either Rock, Paper or Scissors\n").capitalize()))
else:
    print('\n\nGame Ends.')
