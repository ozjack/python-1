"""This is my colors module.

Here is my description of my module.
"""
base02 = '\033[0;30m'
base03 = '\033[1;30m'
red = '\033[0;31m'
yellow = '\033[0;33m'
orange = '\033[1;31m'
magenta = '\033[0;35m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base1 = '\033[1;36m'
base0 = '\033[1;34m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
violet = '\033[1;35m'
blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
reset = '\033[0m'
clear = '\033[H\033[2J'

import random

def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan,
    green])
if __name__ == "__main__":
    print( random_color() + 'random' + reset, end=' ')

