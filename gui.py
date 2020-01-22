# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:07:05 2020

@author: Saransh
"""

import xlsxwriter
import xlrd
import tkinter as tk
import os
from PIL import Image
import numpy as np
import cv2
from datetime import date
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    faceSamples=[]
    Ids=[]
    currentDirectory = "Dataset"
    for folder in os.listdir(path):
        finalDirectory = folder
        print(folder)
        location = f"{currentDirectory}/{finalDirectory}"
        print(location)
        for f in os.listdir(location):
            print(f)
            imagePath = location+"/"+f
            print(imagePath)
            pilImage=Image.open(imagePath)
            imageNp=np.array(pilImage,'uint8')
            faceSamples.append(imageNp)
            Id=int(f[:f.index("_")])
            print(Id)
            Ids.append(Id)
            
    return faceSamples,Ids

attendance=set()
def attendanceID(roll):
    attendance.add(roll)

def recognizeFace():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0
    cam = cv2.VideoCapture(0)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w]) 
            if (confidence > 35 ):
                attendanceID(id)
                confidence = "  {0}%".format(round(confidence)) 
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('Attendance',img) 
        k = cv2.waitKey(10)
        if k == 27:
            break
    
    today = date.today()
    d = today.strftime("%d-%b-%Y")
    filename=""
    filename+=d+".xlsx"
    
    inputWorkbook = xlrd.open_workbook('studentData.xlsx')
    inputWorksheet = inputWorkbook.sheet_by_index(0)
    row = inputWorksheet.nrows
    
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    
    for i in range(0,row):
        if i == 0:
            worksheet.write(0,0,"Name")
            worksheet.write(0,1,"ID")
            worksheet.write(0,2,"Attendance")
        else:
            cellName = inputWorksheet.cell_value(i,0)
            cellID = int(inputWorksheet.cell_value(i,1))
            if cellID in attendance:
                worksheet.write(i,0,cellName)
                worksheet.write(i,1,cellID)
                worksheet.write(i,2,1)
            else:
                worksheet.write(i,0,cellName)
                worksheet.write(i,1,cellID)
                worksheet.write(i,2,0)
                
    workbook.close()
           
    print(attendance)
    cam.release()
    cv2.destroyAllWindows()

def trainFace():
    faces,Ids = getImagesAndLabels('DataSet')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('Trainer/trainer.yml')


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

update_button = tk.Button(window, text="Train", width=25,font=("times new roman",20),bg="#000000",fg='white',command=trainFace)
update_button.pack(padx = 10 , pady = 10)

next_button = tk.Button(window, text="Mark Attendance", width=25,font=("times new roman",20),bg="#000000",fg='white',command=recognizeFace)
next_button.pack(padx = 10 , pady = 10)

exit_button = tk.Button(window,text="Exit",width=25,font=("times new roman",20),bg="#000000",fg='white',command=exitFunction)
exit_button.pack(padx = 10 , pady = 10)

window.mainloop()