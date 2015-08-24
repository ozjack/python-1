"""Welcome, to Jurassic World"""

import colors as c
from utils import ask

intro = c.red + '''
Welcome, to the Jurassic Park quiz
'''

def q1():
    answer = ask(c.red + 'Question 1: What was the base gene of the Indominous Rex?')
    if answer == "tyranosaurus rex":
        print('good choice')
        return True
    print('That is incorrect')
    return False

def q2():
    answer = ask(c.red + 'Question 2: How did Owen escape the Indominous?')
    if answer == "he covered himself in oil":
        print('The indominous could not smell him when he did that')
        return True
    print('That is incorrect')
    return False

def q3():
    answer = ask(c.red + 'Question 3: How did the Indominous hid from thermal tech?')
    if answer == "tree frog DNA alowed it to":
        print('correct')
        return True
    print('That is incorrect')
    return False

def q4():
    answer = ask(c.red + 'Question 3: How did the Indominous die?')
    if answer == "eaten by a mosasaurus":
        print('correct')
        return True
    print('That is incorrect')
    return False

def q5():
    answer = ask(c.red + 'Question 3: how many of the 4 raptors died?')
    if answer == "3":
        print('correct, its sad that any of them died')
        return True
    print('That is incorrect')
    return False

def q6():
    answer = ask(c.red + 'how did the chief of security die?')
    if answer == "he was eaten by raptors":
        print('correct')
        return True
    print('That is incorrect')
    return False

def q7():
    answer = ask(c.red + 'how did the owner of the company die??')
    if answer == "he crashed":
        print('correct')
        return True
    print('That is incorrect')
    return False




questions = [q1,q2,q3,q4,q5,q6,q7]


