import random

from game_art import logo, vs
from instagram_data import data

SLOT_A = random.choice(data)
SLOT_B = random.choice(data)

SCORE = 18

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
    followers1 = account1.get('follower_count')
    followers2 = account2.get('follower_count')
    
    # tester code for follower count
    print(f'A: {followers1}. B: {followers2}')

    if followers1 > followers2:
        return 'a'
    else:
        return 'b'

def clear(seconds = 0):
    '''clears text in terminal '''
    time.sleep(seconds)
    os.system('clear')

print(logo)

print('Compare A:')
account_blurb(SLOT_A)

print(vs)

print('Against B:')
account_blurb(SLOT_B)

guess = input('Who has more followers? Type A or B: ')

if guess.lower() == game_answer(SLOT_A,SLOT_B):
    print('Correct')
else:
    clear()
    print(logo)
    print('Sorry, you are wrong. Final score: {SCORE}')


# find way to clear terminal

# if another answer, go to game over screen

# terminal clears

# score updates on top, comparison B becomes A now

# add case if runs out of questions

# find way for no repeats

