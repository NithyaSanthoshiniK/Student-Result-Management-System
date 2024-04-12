from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class R1:
    def __init__(self,root):
        self.root=root
        self.root.title("1-1")
        self.root.geometry("1350x700+0+0")

        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=0.5,y=80,width=250,height=350)

        frame1=Frame(self.root, bg= "White")
        frame1.place(x=350, y=100, width=900, height=550)

        title=Label(frame1, text= "SEM 1-2" ,font=("times new roman" ,30, "bold"),bg="white",fg='green').place(x=250,y=5)


        f_name=Label(frame1, text= "First Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=5,y=50)
        txt_fname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=10, y=80, width=180)

        HallTicket=Label(frame1, text= "HallTicket No" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=200,y=50)
        txt_HallTicket=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=200, y=80, width=180)

        department=Label(frame1, text= "department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=400,y=50)
        txt_department=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=400, y=80, width=180)

        #===result_labels============

        lb1_subject_name=Label(self.root,text="Subject", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=230,width=180, height=50)
        lb1_Internal_marks=Label(self.root, text="Internal Marks", font=("goudy old style",15,"bold"),bg="white", bd=2,relief=GROOVE) . place(x=430, y=230,width=150, height=50)
        lb1_External_marks=Label(self.root,text="External Marks", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=580, y=230,width=150, height=50)
        lb1_Total_marks=Label(self.root,text="Total Marks", font=("“goudy old style",15,"bold"),bg="white",bd=2, relief=GROOVE) .place(x=730, y=230,width=150, height=50)
        lb1_Grade=Label(self.root,text="Grade", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE). place(x=880, y=230,width=150, height=50)
        lb1_Credits=Label(self.root, text="Credits" ,font=("goudy old style",15,"bold") ,bg="white" ,bd=2, relief=GROOVE).place(x=1030, y=230,width=150, height=50)

        #sgpa============
        SGPA=Label(frame1, text= "SGPA" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=600,y=50)
        self.txt_sgpa=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') 
        self.txt_sgpa.place(x=600, y=80, width=180)

        #======button=======
        btn=Button(text="BACK",font=("times new roman" ,15, "bold"),command=self.mainscreen2 ,bg="green",fg='green').place(x=10,y=650)

    

        #===subject_labels============

       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=280,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=330,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=380,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=430,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=480,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=530,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=580,width=180, height=50)
       # lb1_subject_name=Label(self.root,text="Mathematics", font=("goudy old style",15,"bold"),bg="white", bd=2, relief=GROOVE) .place(x=250, y=630,width=180, height=50)
        
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

    def mainscreen2(self):
        self.root.destroy()
        import mainscreen2



root=Tk()
obj=R1(root)
root.mainloop()        
