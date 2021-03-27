import random
import re

while(1 < 2):
    print('Rock Paper Scissors')
    print('[R]ock [P]aper [S]cissor')
    user = input('Choose your weapon [R]ock [P]aper [S]cissor : ')
    if not re.match("[SsRrPp]", user):
        print('Please choose a weapon')
        print('[R]ock [P]aper [S]cissor')
        continue
    print('You choose : ', user)
    choices = ['R', 'P', 'S']
    opponent = random.choice(choices)
    print('I choose : ', opponent)
    if opponent == user.upper():
        print('Tie')
    
    elif opponent == 'R' and user.upper() == 'S':      
        print("Rock beats scissor, I win! ")
        continue
    elif opponent == 'S' and user.upper() == 'P':      
        print("Scissors beats paper! I win! ")
        continue
    elif opponent == 'P' and user.upper() == 'R':      
        print("Paper beats rock, I win! ")
        continue
    else:       
        print("You win!")
