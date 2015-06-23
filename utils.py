"""This is RANDOM!!!!!"""
import colors as c

def ask(question,color=c.yellow):
    print(color + question + c.reset)
    answer = input('> ' + c.magenta).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("what is your name?")
    color = ask("what is your name in color?",c.random_color())
