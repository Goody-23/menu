import sys
import random
#user input

print("")
playerchoice = input("Enter ...\n1 for rock, \n2 for paper, or\n3 for scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose" + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")