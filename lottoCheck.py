# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games 
# against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26
import os
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
    game = {}
    print("First, regular numbers, 1-70:")
    for i in range(5):
        game[i] = valid_game_input(70)
    print("Second, the jackpot number, 1-26:")
    game[5] = valid_game_input(26)
    return game

def getMatches(x, y):
    matches = {k: x[k] for k in x if k in y and x[k] == y[k]}
    l = len(matches)

    if 5 in matches:
        return (l-1, 1)

    return (l, 0)

def printWin(m):
    strings = {(0, 1):"Matched the Jackpot ball", 
        (1, 1): "Matched 1 regular ball and the Jackpot ball",
        (2, 1): "Matched 2 regular balls and the Jackpot ball",
        (3, 1): "Matched 3 regular balls and the Jackpot ball",
        (4, 1): "Matched 4 regular balls and the Jackpot ball",
        (5, 1): "JACKPOT", 
        (0, 0): "Not a winner, sorry!",
        (1, 0): "Not a winner, sorry!",
        (2, 0): "Not a winner, sorry!",
        (3, 0): "Matched 3 regular balls",
        (4, 0): "Matched 4 regular balls",
        (5, 0): "Matched 5 regular balls"}

    print(strings[m])

def checkSingle():
    print("Check a single game:\n")

    print("Enter the winning numbers:\n")
    winning_game = getSingleGame()

    print("Enter your numbers:\n")
    user_game = getSingleGame()

    matches = getMatches(winning_game, user_game)
    printWin(matches)

def getPath():
    fpath = input("Enter a file path:\n")

    while not (os.path.isfile(fpath) or  fpath.endswith('.csv')):
        print("Path or File does not exist.")
        print("Please enter a path or file:\n")
        fpath = input("Enter a file path:\n")

    return fpath

def getGames(fp):
    games = []
    try:
        f = open(fp, "r")
        for line in f:
            line = line.rstrip()
            gameList = list(map(int, line.split(",")))
            a = gameList[0:5]
            a.sort()
            a.append(gameList[5])
            gameDict = {i : a[i] for i in range(6)}
            games.append(gameDict)
    except IOerror:
        print("Could not read .csv")
    return games

def checkSheet():
    games = getGames(getPath())
    for i in range(1, (len(games) - 1)):
        print("game ", i)
        printWin(getMatches(games[0], games[i]))
        
if __name__ == "__main__":
    print("Check if you are a winner!\n")     
    if query():
        checkSheet()
    else:
        checkSingle()
    exit()