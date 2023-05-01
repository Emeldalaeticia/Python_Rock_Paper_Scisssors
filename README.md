# Python_Rock_Paper_Scisssors


This is a python code for a simple rock paper scissors game. The program asks the player to choose between rock, paper, or scissors by typing 'r', 'p', or 's'. The computer then randomly chooses one of the three options as well. The game then compares the player's choice with the computer's choice, using an "if" statement to determine the winner based on the rules: rock beats scissors, scissors beats paper, and paper beats rock.

The "is_win" function is defined to check if the player's choice beats the opponent's choice. It returns "True" if the player wins, and "False" otherwise.

The "play_best_of" function allows the player to play a series of games against the computer until someone wins best of n games. To win, the player must win ceil(n/2) games (e.g., for best of 3 games, the player must win 2 games). The program keeps track of the number of games won by the player and the computer, and prints out the result of each round.

At the end of the game, the program announces the winner of the best-of-n series: if the player wins more games than the computer, it declares the player the champion; otherwise, it tells the player that the computer has won and wishes them better luck next time.
