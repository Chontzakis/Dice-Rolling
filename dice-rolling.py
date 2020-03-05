import random
from tkinter import *

drawing = [
''' ---
 |1|
 ---''',
 ''' ---
 |2|
 ---''',
''' ---
 |3|
 ---''',''' ---
 |4|
 ---''',''' ---
 |5|
 ---''',''' ---
 |6|
 ---''']
 
def main():
    reroll = 1
    number = int(input('Give me the number of dices: '))
    while reroll == 1:
        list = []
        for i in range(number):
            list.append(random.randint(0,5))
        for i in list:
            print(drawing[i])
        reroll = int(input('Type 1 if you want to reroll or 0 if you want to stop: '))

if __name__ == "__main__":
    main()
    

        
 