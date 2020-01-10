# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:07:05 2020

@author: Saransh
"""

import tkinter as tk

def createData():
    root = tk.Tk()
    root.title("Student Information")
    
    name = tk.StringVar()
    
    enterName = tk.Label(root,text="Enter Name",width=15,font=("times new roman",20))
    enterName.grid(row=0,column=0,padx=10,pady=10)
    
    userName = tk.Entry(root,width = 25,textvariable = name,font=("times new roman",20),justify='center')
    userName.grid(row=0,column=1,padx=10,pady=10)
    
    ID = tk.StringVar()
    
    enterId = tk.Label(root,text="Enter ID",width=15,font=("times new roman",20))
    enterId.grid(row=1,column=0,padx=10,pady=10)
    
    userId = tk.Entry(root,width = 25,textvariable = ID,font=("times new roman",20),justify='center')
    userId.grid(row=1,column=1,padx=10,pady=10)
    
    submit = tk.Button(root,text="Submit",width=15,font=("times new roman",20),bg="#000000",fg='white',anchor='center')
    submit.grid(row=2,column=0,padx=(500,10),pady=20)
    
    root.mainloop()

def exitFunction():
    window.destroy()

window = tk.Tk()
window.title("Face Recognition Attendance System")

dataset_button = tk.Button(window,text="Create Dataset",width=25,font=("times new roman",20),bg="#000000",fg='white',command=createData)
dataset_button.pack(padx = 10 , pady = 10)

update_button = tk.Button(window, text="Train", width=25,font=("times new roman",20),bg="#000000",fg='white')
update_button.pack(padx = 10 , pady = 10)

next_button = tk.Button(window, text="Mark Attendance", width=25,font=("times new roman",20),bg="#000000",fg='white')
next_button.pack(padx = 10 , pady = 10)

exit_button = tk.Button(window,text="Exit",width=25,font=("times new roman",20),bg="#000000",fg='white',command=exitFunction)
exit_button.pack(padx = 10 , pady = 10)

window.mainloop()