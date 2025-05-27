import random

def play():
    user = input("Whats your choice?'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its a tie'
    if is_win(user, computer):
        return 'You won!'
    
    return ' You lost'
    
def is_win(player , oponent):

    if ( player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') \
         or ( player == 'p' and oponent == 'r'):
        return True
    
print(play())