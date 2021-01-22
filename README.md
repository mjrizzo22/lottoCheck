# lottoCheck.py

## How to Use

This little Python script can be compiled and run in the terminal/command-line.   
Please use Python 3.7.7 for best results.  

For particular lottery rules, consult the game's main site.  
This program generalizes that a game is 6 digits,   
The first 5 are 'regular' digits in the range [1-70]  
and the 'jackpot' digit is in range [1-26].
### Single Ticket
The user will be prompted for the winning digits first, then their single game.  
The program will compare the two games as Python dicts.  
Finally, it will output if there are enough matches to count as a win and exit.
### .csv File
Please format .csv file with winning digits as the first row, like so:  

Regular | reg| reg| reg | reg| Jackpot
--- | --- | --- | --- | --- | ---
winner | win | win | win | win | win |
user | user | user | user | user | user |
user | user | user | user | user | user |
⋮|⋮ | ⋮ |⋮ | ⋮ |⋮ |

In this mode, the prompt will ask for a file path to the .csv and verify it.   
Then it will check the first row of the .csv against the remaining rows,   
Printing out the win status each for each game row.  
Again, the program will exit.