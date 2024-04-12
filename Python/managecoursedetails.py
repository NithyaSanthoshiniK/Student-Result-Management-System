from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 
from MySQLdb import _mysql
import MySQLdb
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Course Details")
        self.root.geometry("1350x700+0+0"
        )
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image====
        #===self.left=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/Left.png")
        #==left=Label(self.root,image=self.left).place(anchor="center",width=250,height=250)====#

        #===left Image===
       # self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        #left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #====Register Frame=====
        frame1=Frame(self.root, bg= "white")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text= "Manage Course Details" ,font=("times new roman" ,20, "bold"),bg="white",fg='green').place(x=10,y=15,width=1180,height=35)
         #=======Variables===========
        self.var_course=StringVar()
        self.var_charges=StringVar()
        self.var_period=StringVar()


     #=======Widgets==============
        lbl_CourseName=Label(self.root,text="Course Name",font=("times new roman",20,'bold'),bg='lightyellow').place(x=10,y=120)
        lbl_period=Label(self.root,text="Duration",font=("times new roman",20,'bold'),bg='lightyellow').place(x=10,y=160)
        lbl_charges=Label(self.root,text="Charges",font=("times new roman",20,'bold'),bg='lightyellow').place(x=10,y=200)
        lbl_description=Label(self.root,text="Description",font=("times new roman",20,'bold'),bg='lightyellow').place(x=10,y=240)

     #====Entry Feilds==========
        self.txt_CourseName=Entry(self.root,textvariable=self.var_course,font=("times new roman",20,'bold'),bg='lightyellow')
        self.txt_CourseName.place(x=150,y=120,width=200)
        self.txt_period=Entry(self.root,textvariable=self.var_period,font=("times new roman",20,'bold'),bg='lightyellow')
        self.txt_period.place(x=150,y=160,width=200)
       # self.txt_period=Entry(self.root,textvariable=self.var_period,font=("times new roman",20,'bold'),bg='lightyellow')
       # self.txt_period.place(x=150,y=100,width=200)
        self.txt_charges=Entry(self.root,textvariable=self.var_charges,font=("times new roman",20,'bold'),bg='lightyellow')
        self.txt_charges.place(x=150,y=200,width=200)
        self.txt_description=Text(self.root,font=("times new roman",20,'bold'),bg='lightyellow')
        self.txt_description.place(x=150,y=240,width=500,height=130)

        #====Buttons===========
        self.btn_add=Button(self.root,text='Save',font=("times new romen",15,"bold"),bg="black",fg="black",cursor="hand2")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("times new romen",15,"bold"),bg="black",fg="black",cursor="hand2")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("times new romen",15,"bold"),bg="black",fg="black",cursor="hand2")
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("times new romen",15,"bold"),bg="black",fg="black",cursor="hand2")
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        #====Search Panel==========
        self.var_search=StringVar()
        lbl_searchCourseName=Label(self.root,text="Course Name",font=("times new roman",20,'bold'),bg='lightyellow').place(x=720,y=120)
        txt_searchCourseName=Entry(self.root,textvariable=self.var_search,font=("times new roman",20,'bold'),bg='lightyellow').place(x=870,y=120,width=180)
        btn_search=Button(self.root,text='Search',font=("times new romen",15,"bold"),bg="#03a9f4",fg="black",cursor="hand2").place(x=1070,y=120,width=120,height=28)
        #=====Content==============
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=200,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text=" Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)


        self.CourseTable.pack(fill=BOTH,expand=1)

root=Tk()
obj=Register(root)
root.mainloop()