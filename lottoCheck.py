# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games 
# against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26

import re

def valid_input():
	try:
		game_string = input(
			"Enter 6 game numbers, separated by commas:\n")
		game_string.replace(" ","")
	except:
		print("something went wrong!")
	return result

def getArray():
	return [1]
# step 2
def checkGames():
	# check if jackpot number
	# check check sorted non jackpot numbers
	# return row/game # and win
	return 0

if __name__ == "__main__":
	print("Check if you are winner!\n")
	# Step 0: get winning numbers
	winning_array = valid_input()
	print(winning_array)
	# Step 1: get 2d array of user numbers
	# Step 2.0-2.8: search winning conditions
	# Step 3: output winning game and total match
	exit()