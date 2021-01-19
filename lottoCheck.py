# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games 
# against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26
import distutils
from distutils import util

def query():
    question = "Do you want to enter a .csv? [y/n]:\n"

    while True:
        try:
            resp = input(question).strip().lower()
            return distutils.util.strtobool(resp)
        except ValueError:
            print(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n") 

def valid_game_input(x):
    while True:
        try:
            game_num = int(input())
            if game_num not in range(1, (x+1)):
                print("Input must be in range, try again:\n")
                continue
            break 
        except:
            print("That was not a game number, try again:\n")
    return game_num

def getSingleGame():
    x = {}
    print("First, regular numbers, 1-70:")
    for i in range(5):
        x[i] = valid_game_input(70)
    print("Second, the jackpot number, 1-26:")
    x[5] = valid_game_input(26)
    return x

def getMatches(x, y):
    matches = {k: x[k] for k in x if k in y and x[k] == y[k]}
    return matches

def printWin(m):
    l = len(m)

    if l == 0:
        Print("Not a winner, sorry!")
    elif l == 6:
        Print("JACKPOT")

    output = ""
    if 5 in m:
        output = " And the Jackpot Number!"
        l = l - 1 
    output = "You matched "+str(l)+" regular numbers!"+output
    
    print(output)

def checkSingle():
    print("Check a single game:\n")

    print("Enter the winning numbers:\n")
    winning_game = getSingleGame()

    print("Enter your numbers:\n")
    user_game = getSingleGame()

    matches = getMatches(winning_game, user_game)
    printWin(matches)

def checkSheet():
    return 0

if __name__ == "__main__":
    print("Check if you are a winner!\n")     
    
    if query():
        checkSheet()
    else:
        checkSingle()

    exit()