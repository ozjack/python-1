"""PINK FLUFFY UNICORNS"""

import colors as c
from utils import ask

intro = c.red + '''
Welcome, to the pink fluffy unicorns quiz
'''

def q1():
    answer = ask(c.red + 'Question 1: What colour are the unicorns?')
    if answer == "pink":
        print('And what a lovely color it is')
        return True
    print('That is incorrect')
    return False

def q2():
    answer = ask(c.red + 'Question 2: Where are they dancing?')
    if answer == "rainbows":
        print('Its a wonderful place to dance on, try it')
        return True
    print('That is incorrect')
    return False

def q3():
    answer = ask(c.red + 'Question 3: Please use one word to describe the texture of their magical fur?')
    if answer == "smiles":
        print('It feels wonderful on your skin' + c.clear)
        return True
    print('That is incorrect' + c.clear)
    return False

questions = [q1,q2,q3]


