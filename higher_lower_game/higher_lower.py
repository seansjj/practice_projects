import random

from game_art import logo, vs
from instagram_data import data

SLOT_A = random.choice(data)
SLOT_B = random.choice(data)

# prevents slots A, B being the same
if SLOT_B == SLOT_A:
    SLOT_B = random.choice(data)

SCORE = 0
GAME_OVER = False

def account_blurb(account):
    '''gets name, description, country of instagram account'''
    name =  account.get('name')
    description = account.get('description')
    country = account.get('country')
    article = 'a'

    vowels = ['A','E','I','O','U']

    if description[0] in vowels:
        article = 'an' 

    print(f'{name}, {article} {description}, from {country}')

def game_answer(account1, account2):
    '''returns a or b for whichever account has more followers'''
    followers_a = account1.get('follower_count')
    followers_b= account2.get('follower_count')

    if followers_a > followers_b:
        return 'a'
    else:
        return 'b'

while not GAME_OVER:
    print(logo)
    print(f'Current Score: {SCORE}')
    print('Compare A:')
    account_blurb(SLOT_A)

    print(vs)

    print('Against B:')
    account_blurb(SLOT_B)

    guess = input('Who has more followers? Type A or B: ')

    if guess.lower() == game_answer(SLOT_A,SLOT_B):
        SCORE += 1
        SLOT_A = SLOT_B
        SLOT_B = random.choice(data)
        if SLOT_B == SLOT_A:
            SLOT_B = random.choice(data)
    else:
        GAME_OVER = True
  
print(logo)
print(f'Sorry, you are wrong. Final score: {SCORE}')
