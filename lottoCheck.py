# Author: Mike Rizzo
# Description: Checks a ticket with 1...n games 
# against the winning numbers

# Assumes games are 5 regular numbers from 1-70
# Jackpot numbers is 1 integer from 1-26
def valid_game_input(x):
    while(True):
        try:
            game_num = int(input())
            if game_num not in range(1, (x+1)):
                print("Input must be in range, try again:\n")
                continue
            break 
        except:
            print("That was not a game number, try again:\n")
    return game_num

def getGame():
    x = {}
    print("First, regular numbers, 1-70:")
    for i in range(5):
        x[i] = valid_game_input(70)
    print("Second, the jackpot number, 1-26:")
    x[5] = valid_game_input(26)
    return x

def checkGame(x, y):
    matches = {k: x[k] for k in x if k in y and x[k] == y[k]}
    l = len(matches)

    if l == 0:
        return "Not a winner, sorry!"
    elif l == 6:
        return "JACKPOT"

    output = ""
    if 5 in matches:
        output = " And the Jackpot Number!"
        l = l - 1 
    output = "You matched "+str(l)+" regular numbers!"+output
    return output

if __name__ == "__main__":
    print("Check if you are a winner!\n")

    print("Enter the winning numbers:\n")
    winning_game = getGame()

    print("Enter your numbers:\n")
    user_game = getGame()

    print(checkGame(winning_game, user_game))
    exit()