from tkinter import*
import pyodbc
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import*
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from MySQLdb import _mysql
import MySQLdb
import pymysql
import pyodbc
import pandas as pd
import pandasql as ps


class Results:
    def __init__(self,root):
        self.root=root
        self.root.title("Mainscreen")
        self.root.geometry("1350x700+0+0")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=0.5,y=80,width=250,height=350)

        #====Register Frame=====
        frame1=Frame(self.root, bg= "white")
        frame1.place(x=300, y=100, width=1000, height=550)

        title=Label(frame1, text= "VIEW RESULTS HERE" ,font=("times new roman" ,20, "bold"),bg="white",fg='green').place(x=50,y=5)

        #-------------------ROW1---------------------
        f_name=Label(frame1, text= "First Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=5,y=50)
        self.txt_fname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') 
        self.txt_fname.place(x=10, y=80, width=180)

        HallTicket=Label(frame1, text= "HallTicket No" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=200,y=50)
        self.txt_HallTicket=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') 
        self.txt_HallTicket.place(x=200, y=80, width=180)

        Answer=Label(frame1, text= "Department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=400,y=50)
        txt_Answer=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=400, y=80, width=180)

        #--------------------Row2
        '''   First_Y=Label(frame1, text= "First Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=170)
        btn=Button(frame1, text="1-1",font=("times new roman" ,15, "bold"),command=self.r11,bg="green",fg='green').place(x=200,y=170)

        btn=Button(frame1, text="1-2",font=("times new roman" ,15, "bold"),command=self.r12,bg="green",fg='green').place(x=370,y=170)


        #--------------------Row3
        Second_Y=Label(frame1, text= "Second Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=240)
        btn=Button(frame1, text="2-1",font=("times new roman" ,15, "bold"),command=self.r21,bg="green",fg='green').place(x=200,y=240)

        btn=Button(frame1, text="2-2",font=("times new roman" ,15, "bold"),command=self.r22,bg="green",fg='green').place(x=370,y=240)

        #--------------------Row4
        Third_Y=Label(frame1, text= "Third Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=310)
        btn=Button(frame1, text="3-1",font=("times new roman" ,15, "bold"),command=self.r31,bg="green",fg='green').place(x=200,y=310)

        btn=Button(frame1, text="3-2",font=("times new roman" ,15, "bold"),command=self.r32,bg="green",fg='green').place(x=370,y=310)

        #--------------------Row5
        Fourth_Y=Label(frame1, text= "Fourth Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=380)
        btn=Button(frame1, text="4-1",font=("times new roman" ,15, "bold"),command=self.r41,bg="green",fg='green').place(x=200,y=380)

        btn=Button(frame1, text="4-2",font=("times new roman" ,15, "bold"),command=self.r42,bg="green",fg='green').place(x=370,y=380)'''

        btn=Button(frame1, text="search",font=("times new roman" ,15, "bold"),command=self.sql_run,bg="green",fg='green').place(x=370,y=5)

        semester=Label(frame1, text= "Semester" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=600,y=50)
        
        self.cmb_semester=ttk.Combobox(frame1, font= ("times new roman" ,13), state='read only' , justify=CENTER) 
        self.cmb_semester['values']=("Select" , "SEM1-1", "SEM1-2" , "SEM2-1", "SEM2-2", "SEM3-1", "SEM3-2" , "SEM4-1", "SEM4-2")
        self.cmb_semester.place(x=600, y=80, width=180)
        self.cmb_semester.current(0)

         #===result_labels============

        lb1_subject_name=Label(self.root,text="Subject", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=230,width=180, height=50)
        lb1_Internal_marks=Label(self.root, text="Internal Marks", font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE) . place(x=430, y=230,width=150, height=50)
        lb1_External_marks=Label(self.root,text="External Marks", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=580, y=230,width=150, height=50)
        lb1_Total_marks=Label(self.root,text="Total Marks", font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) .place(x=730, y=230,width=150, height=50)
        lb1_Grade=Label(self.root,text="Grade", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE). place(x=880, y=230,width=150, height=50)
        lb1_Credits=Label(self.root, text="Credits" ,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE).place(x=1030, y=230,width=150, height=50)
 
        #=======self1=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=280,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=280,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=280,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=280,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=280,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=280,width=150, height=50)

        #=======self2=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=330,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=330,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=330,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=330,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=330,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=330,width=150, height=50)

        #=======self2=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=380,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=380,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=380,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=380,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=380,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=380,width=150, height=50)

        #=======self4=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=430,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=430,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=430,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=430,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=430,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=430,width=150, height=50)

        #=======self5=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=480,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=480,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=480,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=480,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=480,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=480,width=150, height=50)

        #=======self6=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=530,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=530,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=530,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=530,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=530,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=530,width=150, height=50)

        #=======self7=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=580,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=580,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=580,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=580,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=580,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=580,width=150, height=50)

        #=======self8=========
        self.subject_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.subject_name.place(x=250, y=630,width=180, height=50)
        self.Internal_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE)
        self.Internal_marks.place(x=430, y=630,width=150, height=50)
        self.External_marks=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) 
        self.External_marks.place(x=580, y=630,width=150, height=50)
        self.Total_marks=Label(self.root, font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) 
        self.Total_marks.place(x=730, y=630,width=150, height=50)
        self.Grade=Label(self.root, font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.Grade.place(x=880, y=630,width=150, height=50)
        self.Credits=Label(self.root,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE)
        self.Credits.place(x=1030, y=630,width=150, height=50)


    def r11(self):
        self.root.destroy()
        import r11
    def r12(self):
        self.root.destroy()
        import r12
    def r21(self):
        self.root.destroy()
        import r21
    def r22(self):
        self.root.destroy()
        import r22
    def r31(self):
        self.root.destroy()
        import r31
    def r32(self):
        self.root.destroy()
        import r32
    def r41(self):
        self.root.destroy()
        import r41
    def r42(self):
        self.root.destroy()
        import r42
    def sql_run(self):

        htno = self.txt_HallTicket.get()
        sem = self.cmb_semester.get()
        print(htno)
        if (htno != None):
            server = 'tcp:rmsserver2.database.windows.net'
            database = 'RMSDB'
            username = 'nithya'
            password = 'Akhil387*'
            driver= '{ODBC Driver 17 for SQL Server}'

            con  = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
               #con=pyodbc.connect(host="localhost",user="nithya", password="Akhil387*",database="RMSDB")
            cur=con.cursor()
               #cur.execute("select * from student_details, where email=%s",self.txt_email.get())
            #cur.execute("SELECT TOP (1000) * FROM [dbo].[studentresults]")
            #cur.execute(f"SELECT TOP (1000) * FROM [dbo].[studentresults] where HTNO = '{htno}' and semester = '{sem}'")
            r = ps(f"SELECT TOP (1000) * FROM [dbo].[studentresults] where HTNO = '{htno}' and semester = '{sem}'")
            print(r)
            #row=cur.fetchone()
            if r!=None:
             '''   self.subject_name.config(text=row[1])
                self.Internal_marks.config(text=row[2])
                self.External_marks.config(text=row[3])
                self.Total_marks.config(text=row[4])
                self.Grade.config(text=row[5])
                self.Credits.config(text=row[6])'''
                
          #  print(row)
        else:
            print("enter hall ticket number")
        

root=Tk()
obj=Results(root)
root .mainloop()