# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:15:41 2022

@author: PC_RC
"""

from tkinter import *
root = Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label = Label(root)

array_1d = ["Ishaan", "Vasuki", "Darshith"]
print(array_1d[0])

array_2d = [["Ishaan","Keyboard"], ["Vasuki", "Carnatic Vocal"], ["Darshith", "Keyboard"]]
print(array_2d[0][1])

array_3d = [[["Ishaan", "Keyboard", "6LS"], ["Vasuki", "Carnatic Vocal", "6B"], ["Darshith", "Keyboard", "6B"]]]
print(array_3d[0][0][2])

def report():
    label["text"]= array_3d[0][1][0] + " chose " + array_3d[0][1][1] + " M.E and is studying in " + array_3d[0][1][2]
    

btn = Button(root, text = "Show Info", command = report)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()