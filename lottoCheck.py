# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games 
# against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26
def valid_input(x):
    while(True):
        try:
            game_num = int(input("Enter game numbers:\n"))
            if game_num not in range(1,x):
                print("Input must be in range, try again:")
                continue
            break 
        except:
            print("That was not a game number, try again:")
    return game_num
def getGame():
    x = {}
    print("Enter the regular winning, 1-70")
    for i in range(5):
        x[i] = valid_input(70)
    print("Enter the jackpot number, 1-26")
    x[5] = valid_input(26)
    return x

# step 2
def checkGame():
    # check if jackpot number
    # check check sorted non jackpot numbers
    # return row/game # and win
    return 0

if __name__ == "__main__":
    print("Check if you are winner!\n")
    # Step 0: get winning numbers
    winning_game = getGame()
    # Step 1: get 2d array of user games
    # rows are a game
    # Step 2.0-2.8: search winning conditions
    # split conditions by jackpot
    # Step 3: output winning game and total match
    exit()