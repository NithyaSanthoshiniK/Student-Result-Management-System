from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pyodbc
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #====Register Frame=====
        frame1=Frame(self.root, bg= "White")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text= "LOGIN HERE" ,font=("times new roman" ,30, "bold"),bg="white",fg='green').place(x=250,y=50)

        email=Label(frame1, text= "Email Address" ,font=("times new roman" ,18, "bold"),bg="white",fg='purple').place(x=250,y=150)
        self.txt_email=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black')
        self.txt_email.place(x=250, y=180, width=350, height=35)
     
        userpassword=Label(frame1, text= "userpassword" ,font=("times new roman" ,18, "bold"),bg="white",fg='purple').place(x=250,y=250)
        self.txt_userpassword=Entry(frame1, font= ("times new roman" ,15),show="*",bg= "lightgray",fg='black') 
        self.txt_userpassword.place(x=250, y=280, width=350,height=35)

        btn=Button(frame1, text="LOGIN",font=("times new roman" ,20, "bold"),command=self.login,bg="green",fg='green').place(x=250,y=340)

        btn=Button(frame1, text="OR REGISTER NEW ACCOUNT",font=("times new roman" ,15, "bold"),command=self.register_window ,bg="green",fg='green').place(x=250,y=400)

    
    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_userpassword.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            messagebox.showinfo("Success","WELCOME",parent=self.root)
            import mainscreen1
           
        ''' else:
            try:
                server = 'tcp:rmsserver2.database.windows.net'
                database = 'RMSDB'
                username = 'nithya'
                password = 'Akhil387*'
                driver= '{ODBC Driver 17 for SQL Server}'

                con  = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
              #  con=pyodbc.connect (host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from student_details where email=%s and password=%s", (self.txt_email.get(),self.txt_userpassword.get()))
                row=cur. fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
        else:
            messagebox.showinfo("Success","WELCOME",parent=self.root)
            import mainscreen1
        con.close()
        except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)'''



root=Tk()
obj=Login(root)
root .mainloop()