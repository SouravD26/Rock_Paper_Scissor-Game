#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL PC
#
# Created:     02-12-2023
# Copyright:   (c) DELL PC 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
# Rock_paper_Scissor

import random

def rock_paper_scissor():

    player = input("What is your Choice - 'r' for Rock,'p' for Paper,'s' for Scissor" )

    choices = ['r','p','s']

    opponent = random.choice(choices)

    if(player == opponent):
        return print(f"Its tie! choice is {opponent} ")

    if play_win(player,opponent):
        return print(f"Yah! You won, choice is {opponent}")

    if play_win(player,opponent) != True:
        return print(f"Sorry! You lost. choice is {opponent}")
def play_win(user,computer):
    if(user =='r' and computer == 's') or (user =='s' and computer =='p') or (user =='p' and computer =='r'):
        return True

rock_paper_scissor()

