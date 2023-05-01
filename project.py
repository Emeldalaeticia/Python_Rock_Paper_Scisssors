import random
import math


def play():
    player = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors\n")
    player = player.lower()

    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return (0, player, computer)
    
    # r > s, s > p, p > r
    if is_win(player, computer):
        return (1, player, computer) 
    

    return (-1, player, computer)

def is_win(player, opponent):
    #return true if the player beats the opponent
    # winninig conditions r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, player, computer = play()
        # tie
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(player))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. YOU WON!\n'.format(player, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. YOU LOST. \n'.format(player, computer))
        # print('\n')
    
    if player_wins > computer_wins:
        print("You have won the best of {} games! What a CHAMP!".format(n))
    else:
        print("Unfortunately, the computer has won the best of {} games. BETTER LUCK NEXT TIME.".format(n))

    
play_best_of(3)