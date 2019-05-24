#!/usr/bin/env python3

from tkinter import *

root= Tk()
root.title('OFA-j')
menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()