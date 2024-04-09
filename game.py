# author: Landon Nguyen
# date: March 17, 2023
# file: game.py a Python file that defines a gui for fifteen puzzle game
# input: users click tiles to move them around to get them in order, users can also shuffle the board
# output: a gui window pops up showing users the current state of the board

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

def clickButton(name):
    button_name = name
    tiles.update(button_name)
    for i in range(len(tiles.tiles)):
        text = StringVar()
        text.set(str(tiles.tiles[i]))
        name = tiles.tiles[i]
        if name == 0:
            button = Button(gui, textvariable='', name=str(name),
                          bg='white', fg='black', font=font, height=2, width=5)
        else:
            button = Button(gui, textvariable=text, name=str(name),
                            bg='white', fg='black', font=font, height=2, width=5,
                            command=lambda name=name: clickButton(name))
        buttons.append(button)
    order = [buttons.pop(0) for i in range(16)]
    draw(order) 
    if tiles.is_solved():
        print('Solved!!!')

def shuffle():
    buttons = []
    tiles.shuffle()
    for i in range(len(tiles.tiles)):
        text = StringVar()
        text.set(str(tiles.tiles[i]))
        name = tiles.tiles[i]
        if name == 0:
            button = Button(gui, textvariable='', name=str(name),
                          bg='white', fg='black', font=font, height=2, width=5)
        else:
            button = Button(gui, textvariable=text, name=str(name),
                            bg='white', fg='black', font=font, height=2, width=5,
                            command=lambda name=name: clickButton(name))
        buttons.append(button)
    order = [buttons.pop(0) for i in range(16)]
    draw(order)

def draw(order):
    for i in range(4):
        for j in range(4):
            button = order[i*4 + j]
            button.grid(row=i, column=j)
    t = StringVar()
    t.set(str('shuffle'))
    button = Button(gui, textvariable=t, name=str('shuffle'),
                          bg='white', fg='black', font=font, height=2, width=10,
                          command=lambda name=0: shuffle())
    button.place(x=120, y=279)

if __name__ == '__main__':    
    # make tiles
    tiles = Fifteen()
    # make a window
    gui = Tk()
    gui.geometry('425x350')
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helvetica', size='25', weight='bold')
    # make buttons
    buttons = []
    for i in tiles.tiles:
        text = StringVar()
        text.set(str(i))
        name = i
        if name == 0:
            button = Button(gui, textvariable='', name=str(name),
                          bg='white', fg='black', font=font, height=2, width=5)
        else:
            button = Button(gui, textvariable=text, name=str(name),
                            bg='white', fg='black', font=font, height=2, width=5,
                            command=lambda name=name: clickButton(name))
        buttons.append(button)
    order = [buttons.pop(0) for i in range(16)]
    draw(order)
    
    # update the window
    gui.mainloop()