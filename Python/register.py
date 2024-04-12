from tkinter import*
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from MySQLdb import _mysql
import MySQLdb
import pymysql
import pyodbc


class Register:
    def __init__(self,root):
       # var = StringVar()
       # self.fname_var = tk.StringVar()
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #====Register Frame=====
        frame1=Frame(self.root, bg= "white")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text= "REGISTER HERE" ,font=("times new roman" ,20, "bold"),bg="white",fg='green').place(x=50,y=30)

       
        fname=Label(frame1, text= "First Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=100)
        self.txt_fname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_fname.place(x=50, y=130, width=250)


        lname=Label(frame1, text= "Last Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=100)
        self.txt_lname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_lname.place(x=370, y=130, width=250)

        #--------------------Row2
        HallTicket=Label(frame1, text= "HallTicket No" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=170)
        self.txt_HallTicket=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_HallTicket.place(x=50, y=200, width=250)

        email=Label(frame1, text= "Email" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=170)
        self.txt_email=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_email.place(x=370, y=200, width=250)

        #--------------------Row3
        question=Label(frame1, text= "B.Tech Regulation" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=240)
        
        self.cmb_question=ttk.Combobox(frame1, font= ("times new roman" ,13), state='read only' , justify=CENTER) 
        self.cmb_question['values']=("Select" , "r18", "r19" , "r20", "r21", "r22")
        self.cmb_question.place(x=50, y=270, width=250)
        self.cmb_question.current(0)

        Answer=Label(frame1, text= "Department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=240)
        self.txt_Answer=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_Answer.place(x=370, y=270, width=250)

        #--------------------Row4-----
        Password=Label(frame1, text= "Password" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=310)
        self.txt_Password=Entry(frame1, font= ("times new roman" ,15),show="*",bg= "lightgray",fg='black')
        self.txt_Password.place(x=50, y=340, width=250)

        Cpassword=Label(frame1, text= "Confirm Password" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=310)
        self.txt_Cpassword=Entry(frame1, font= ("times new roman" ,15),show="*",bg= "lightgray",fg='black')
        self.txt_Cpassword.place(x=370, y=340, width=250)

        #----------terms------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk, onvalue=1 , offvalue=0 ,bg="white",fg='purple',font=("times new roman",12)).place(x=50,y=380)
        #if self.txt_HallTicket.get()!=None:
        self.btn=Button(frame1, text="REGISTER NOW",font=("times new roman" ,15, "bold"),command=self.register_data,bg="green",fg='green').place(x=50,y=420)
        btn_signin=Button(frame1, text="OR SIGN IN",font=("times new roman" ,15, "bold"),command=self.login_window ,bg="green",fg='green').place(x=50,y=460)
       
    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
          flag_validation=True
          fname=self.txt_fname.get() # read name
          lname=self.txt_lname.get() # read name
          HallTicket=self.txt_HallTicket.get()# read name
          email=self.txt_email.get() # read name
          question=self.cmb_question.get()# read name
          answer=self.txt_Answer.get() # read name
          password=self.txt_Password.get()# read name
          Cpassword=self.txt_Cpassword.get()# read name
          print(str(fname))
          print(f"'{lname}'")
          print(HallTicket)
           
          if self.txt_fname.get()!="":
             if  self.txt_fname.get()=="" or self.txt_HallTicket.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="SELECT" or self.txt_Answer.get()=="" or self.txt_Password.get()=="" or self.txt_Cpassword.get()=="":
               messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
             elif self.txt_Password.get()!= self.txt_Cpassword.get():   
               messagebox.showerror("ERROR","Password and Confirm Password should be same",parent=self.root)
             elif self.var_chk.get()==0:
               messagebox.showerror("ERROR","Please Agree our Terms And Conditions",parent=self.root) 
             else:
              # return NotImplementedError("Please provide values")
               messagebox.showinfo("SUCCESS","Registered Successfully",parent=self.root) 
          try:
               server = 'tcp:rmsserver2.database.windows.net'
               database = 'RMSDB'
               username = 'nithya'
               password = 'Akhil387*'
               driver= '{ODBC Driver 17 for SQL Server}'

               con  = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
               #con=pyodbc.connect(host="localhost",user="nithya", password="Akhil387*",database="RMSDB")
               cur=con.cursor()
               #cur.execute("select * from student_details, where email=%s",self.txt_email.get())
               cur.execute("SELECT TOP (1000) * FROM [dbo].[test]")
               row=cur.fetchall()
               print(row)
               supports_unicode_statements = True
               #query=("INSERT INTO [dbo].[student_details] (firstname, lastname, hallticketno,email,btech_regulation,department,userpassword,confirm_password) VALUES (?,?,?,?,?,?,?,?)",f"'{fname}'",f"'{lname}'",f"'{HallTicket}'",f"'{email}'",f"'{question}'",f"'{answer}'",f"'{password}'",f"'{Cpassword}'")
               query=(f"INSERT INTO [dbo].[student_details] (firstname, lastname, hallticketno,email,btech_regulation,department,userpassword,confirm_password) VALUES ([{fname},[{lname}],[{HallTicket}],[{email}],[{question}],[{answer}],[{password}],[{Cpassword}]);")
               print(type(str(query)))
               query1 = str(query)
               #query=("insert into [dbo].[student_details] firstname,lastname,hallticketno,email,btech_regulation,department,userpassword,confirm_password values (?,?,?,?,?,?,?,?)",'kk',gg,kk,kk,kk,kk,kk,kk)
               #cur.execute(query,(f"{fname}","{lname}","{HallTicket}","{email}","{question}","{answer}","{password}","{Cpassword}"))
               student_details =(fname,lname,HallTicket,email,question,answer,password,Cpassword)
               cur.execute(query1)
               self.txt_fname.get().delete('1.0',END),
               self.txt_lname.get().delete('1.0',END),
               self.txt_HallTicket.get().delete('1.0',END),
               self.txt_email.get().delete('1.0',END),
               self.cmb_question.get().delete('1.0',END),
               self.txt_Answer.get().delete('1.0',END),
               self.txt_Password.get().delete('1.0',END),
               self.txt_Cpassword.get().delete('1.0',END)
                            
               con.commit()
               con.close()
               messagebox.showinfo("SUCCESS","Registered Successfully",parent=self.root)   
          except Exception as es:
             #  error = str(e.__dict__['orig'])
               print(messagebox.showerror("ERROR",f"Error due to: {str(es)}",parent=self.root))
               print(es)
             #  print(error)
              # info.set(error)
          else:
            #  return NotImplementedError("Please provide values")
              messagebox.showinfo("SUCCESS","Registered Successfully",parent=self.root)

               
    '''def validation(self):
        if  self.txt_fname.get()=="" or self.txt_HallTicket.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="SELECT" or self.txt_Answer.get()=="" or self.txt_Password.get()=="" or self.txt_Cpassword.get()=="":
             messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
        elif self.txt_Password.get()!= self.txt_Cpassword.get():   
            messagebox.showerror("ERROR","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("ERROR","Please Agree our Terms And Conditions",parent=self.root) '''
    

root=Tk()
obj=Register(root)
root.mainloop()






