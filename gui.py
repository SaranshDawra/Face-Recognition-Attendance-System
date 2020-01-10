# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:07:05 2020

@author: Saransh
"""

import tkinter as tk
import os
import cv2
import time


def saveInfo(root,name,ID):
    i=0
    t_end = time.time() + 60 * 1
    cam = cv2.VideoCapture(0)
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector=cv2.CascadeClassifier(harcascadePath)
    img_counter = 0
    currentDirectory = 'DataSet'
    finalDirectory = name+'_'+ID
    path = f"{currentDirectory}/{finalDirectory}"
    os.mkdir(path)
    while time.time() < t_end:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        
                img_name =ID+"_"+str(i)+".png"
                i=i+1
                cv2.imwrite(os.path.join(path , img_name),gray[y:y+h,x:x+w])
                img_counter=img_counter+1
                cv2.imshow('Dataset Creation',frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            print(path)
            print(name)
            print(ID)
            break
    cam.release()
    cv2.destroyAllWindows()
    root.destroy()


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
    
    submit = tk.Button(root,text="Submit",width=15,font=("times new roman",20),bg="#000000",fg='white',anchor='center',command=lambda:saveInfo(root,userName.get(),userId.get()))
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