import random


def play():
    player = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors\n")
    player = player.lower()

    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return "You and the computer have both chosen {}. It's a tie.".format(computer)
    
    # r > s, s > p, p > r
    if is_win(player, computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(player, computer)
    

    return "You have chosen {} and the computer has chosen {}. You Lost!".format(player, computer)

def is_win(player, opponent):
    #return true if the player beats the opponent
    # winninig conditions r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False






print(play())