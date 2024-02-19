import random

from game_art import logo, vs
from instagram_data import data

def random_element():
    '''selects random instagram account, removes it from data list to avoid repeats '''
    random_account = random.choice(data)
    print(random_account)

random_element()
random_element()

# choose 2 random dictionary list
# create comparison with f string referring to dictionary name, career, country

# ask who has more followers

# move B up to A after answer

# if correct, clear and update score on top

# if incorrect, ending screen, final score

# print logos

