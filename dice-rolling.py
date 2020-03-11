import random
from tkinter import *
from PIL import ImageTk, Image
import os

drawing = [
''' ---
 |1|
 ---''',
 ''' ---
 |2|
 ---''',
''' ---
 |3|
 ---''',
 ''' ---
 |4|
 ---''',
 ''' ---
 |5|
 ---''',
 ''' ---
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

#if __name__ == "__main__":
#    main()


window=Tk()
def onf(args) :
    if args == 1 :
        first = random.randint(0,5)
        panel = Label(window, image = image[first],width=50,height=50) .grid(row=2,column=0) 
        panel = Label(window, image = image[6],width=50,height=50) .grid(row=2,column=1) 
        panel = Label(window, image = image[6],width=50,height=50) .grid(row=2,column=2) 
    elif args == 2 :
        first = random.randint(0,5)
        second = random.randint(0,5)
        panel = Label(window, image = image[first],width=50,height=50) .grid(row=2,column=0)
        panel = Label(window, image = image[second],width=50,height=50) .grid(row=2,column=1) 
        panel = Label(window, image = image[6],width=50,height=50) .grid(row=2,column=2) 
    else :
        first = random.randint(0,5)
        second = random.randint(0,5)
        third = random.randint(0,5)
        panel = Label(window, image = image[first],width=50,height=50) .grid(row=2,column=0) 
        panel = Label(window, image = image[second],width=50,height=50) .grid(row=2,column=1) 
        panel = Label(window, image = image[third],width=50,height=50) .grid(row=2,column=2) 
    
window.title("Rolling Dice")
window.configure(background = 'black')
window.geometry("550x300+550+300")
canvas = Canvas(window, width = 22) 
image = []
image.append(ImageTk.PhotoImage(Image.open('1.png')))
image.append(ImageTk.PhotoImage(Image.open('2.png')))
image.append(ImageTk.PhotoImage(Image.open('3.png')))
image.append(ImageTk.PhotoImage(Image.open('4.png')))
image.append(ImageTk.PhotoImage(Image.open('5.png')))
image.append(ImageTk.PhotoImage(Image.open('6.png')))
image.append(ImageTk.PhotoImage(Image.open('black.png')))
btn1=Button(window,text = '1 Dice',width = '20',highlightbackground='lightyellow',fg='maroon',command = lambda:onf(1)).grid(row=1,column=0)
btn2=Button(window,text = '2 Dices',width = '20',highlightbackground='lightyellow',fg='maroon',command  = lambda:onf(2)).grid(row=1,column=1)
btn3=Button(window,text = '3 Dices',width = '20',highlightbackground='lightyellow',fg='maroon',command  = lambda:onf(3)).grid(row=1,column=2)



window.mainloop()