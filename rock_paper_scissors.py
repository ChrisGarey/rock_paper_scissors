import random

def play():
    user = input("What\'s your choice? 'R' for rock, 'P' for paper. 'S' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie.'

    #r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won.'

    return 'You lost.'

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def is_loss(plaer, opponent):
    # return true if player loses
    if(player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') \
        or (player == 'r' and opponent == 'p'):
        return True

print(play())