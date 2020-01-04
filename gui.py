# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:07:05 2020

@author: Saransh
"""

import tkinter as tk

def exitFunction():
    window.destroy()

window = tk.Tk()
window.title("Face Recognition Attendance System")

dataset_button = tk.Button(window,text="Create Dataset",width=25,font=("times new roman",20),bg="#000000",fg='white')
dataset_button.pack(padx = 10 , pady = 10)

update_button = tk.Button(window, text="Train", width=25,font=("times new roman",20),bg="#000000",fg='white')
update_button.pack(padx = 10 , pady = 10)

next_button = tk.Button(window, text="Mark Attendance", width=25,font=("times new roman",20),bg="#000000",fg='white')
next_button.pack(padx = 10 , pady = 10)

exit_button = tk.Button(window,text="Exit",width=25,font=("times new roman",20),bg="#000000",fg='white',command=exitFunction)
exit_button.pack(padx = 10 , pady = 10)

window.mainloop()