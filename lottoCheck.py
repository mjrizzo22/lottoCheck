# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26

import numpy as np
import re

def checkInput(game, size):
	# TODO make regex for 'numeric,' only
	if len(game) > size:
		print("Too many numbers try again\n")
		return 1
	elif len(game) < size:
		print("Not enough numbers try again \n")
		return 1
	else:
		return 0
		
def getWinningArray():
	winner_input = 1
	while(winner_input == 1):
		winning_string = input("Enter the 6 winning numbers,
                separated by commas:\n")
		winning_string.replace(" ","")
		winner_input = checkInput(winning_string, 11)

	winning_array = winning_string.split(",")
	return winning_array

# step 2
def checkGames():
	# check if jackpot number
	# check check sorted non jackpot numbers
	# return row/game # and win

if __name__ == "__main__":
	print("Check if you are winner!\n")
	# Step 0: get winning numbers
	winning_array = getWinningArray()
	# Step 1: get 2d array of user numbers
	# Step 2.0-2.8: search winning conditions
	# Step 3: output winning game and total match
	exit()
