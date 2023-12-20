import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

#user input

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
   
    print("")
    print("This game is a best out of 3 between you and python ")
   
    print("")
   
    player = int(input("Enter ...\n1 for rock, \n2 for paper, \n3 for scissors:\n\n"))

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computer = random.choice([1, 2, 3])
    print("")

    print("You chose " + str(RPS(player)).replace('RPS.', '' ) + ".")
    
    print("Python chose " + str(RPS(computer)).replace('RPS.', '' ) + ".")
    
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("you lost to python 🤣🤣🤣 ")
        computer_wins += 1

    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("Congrats you beat python 🎉🎊 ") 
        player_wins += 1

    if (player == 1 and computer == 1) or (player == 2 and computer ==2) or (player == 3 and computer ==3):
        print("Go again 🤔🤔 ")   
  
print("\nFinal scores: ")
print(f"player: {player_wins}")
print(f"python: {computer_wins}")

if player_wins == 3:
    print("congrats bum ahh nigga you beat a stupid bot made by a rookie. ")
else:
    print("Damnn Nigga you really suck huh?? Lost to a dumb ahh bot. ")