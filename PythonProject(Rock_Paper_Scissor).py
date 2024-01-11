# Name:        module2
#
# Author:      Sourav Dutta
#
# Created:     04-01-2024




# Rock_paper_Scissor

import random

def rock_paper_scissor():
    print("'r' for Rock, 'p' for Paper,'s' for Scissor.")
    player = input("What is your Choice -- " )

    choices = ['r','p','s']

    opponent = random.choice(choices)

    if(player == opponent):
        return print(f"Its tie! Opponent choice is {opponent} ")

    if play_win(player,opponent):
        return print(f"Yah! You won,Opponent choice is {opponent}")

    if play_win(player,opponent) != True:
        return print(f"Sorry! You lost.Opponent choice is {opponent}")
def play_win(user,computer):
    if(user =='r' and computer == 's') or (user =='s' and computer =='p') or (user =='p' and computer =='r'):
        return True

rock_paper_scissor()

