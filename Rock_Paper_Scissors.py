
from random import random
import re
import random
import string


def play_game(playerOpt):
    mylist = ["Rock", "Paper", "Scissors"]

    computer = random.choice(mylist)

    if playerOpt == computer:
        print('{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("It was a draw!\n")
        return 1
    elif playerOpt == 'Scissors' and computer == 'Rock':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You lost!")
        return 1
    elif playerOpt == 'Rock' and computer == 'Paper':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You lost!")
        return 1
    elif playerOpt == 'Paper' and computer == 'Scissors':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You lost!")
        return 1

    elif playerOpt == 'Rock' and computer == 'Scissors':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You won!")
        return 1
    elif playerOpt == 'Paper' and computer == 'Rock':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You won!")
        return 1
    elif playerOpt == 'Scissors' and computer == 'Paper':
        print('\n{} picked:'.format(player_name), playerOpt, '\ncomputer picked:', computer)
        print("You won!")
        return 1

    else:
        print('The value entered is invalid try again\n')
        return 0


print("Hey there! Do you want to play Rock, Paper, Scissors?")

Response = ['Yes', 'No']
Ans = None

while Ans not in Response:
    Ans = input("Yes/No?: ").capitalize()
    if Ans != "Yes":
        print("Get outta here dumbass! Why bother?")
        break

    print("Good Choice!\nLet's Begin!\n")

    player_name = input("Enter your name to begin: ")

    while len(player_name) == 0:
        player_name = input("Enter your name to begin: ")

    while True:
        player_Opt = (play_game(input("\nRock, Paper or Scissors?: ").capitalize()))

        while player_Opt == 0:
            player_Opt = (play_game(input("\nRock, Paper or Scissors?: ").capitalize()))

        play_again = input("Play again? (Yes/No): ").capitalize()
        if play_again != "Yes":
            break

print('\n\nGame Ends.')
