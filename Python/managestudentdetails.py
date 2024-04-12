from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pyodbc
class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Student Details")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="White")


        #===Bg Image===
        #self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        #bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
     #  self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
       # left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #====Register Frame=====
        frame2=Frame(self.root, bg= "white")
        frame2.place(x=480, y=100, width=700, height=500)
        #===title====
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,'bold'))
        #=======Variables============
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        #=======Widgets==============
        #====column1====================
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=60)
        lbl_Name=Label(self.root,text="Name.",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=100)
        lbl_Email=Label(self.root,text="Email.",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender.",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=180)


        lbl_state=Label(self.root,text="state",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=220)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style ",15,'bold'),bg='White').place(x=150,y=220,width=150)

        lbl_city=Label(self.root,text="city",font=("goudy old style ",15,'bold'),bg='White').place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style ",15,'bold'),bg='White').place(x=380,y=220,width=100)

        lbl_pin=Label(self.root,text="pin",font=("goudy old style ",15,'bold'),bg='White').place(x=500,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style ",15,'bold'),bg='White').place(x=560,y=220,width=120)

        lbl_address=Label(self.root,text="Address",font=("goudy old style ",15,'bold'),bg='White').place(x=10,y=260)

        #====Entry Fields==========
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=150,y=60,width=200)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_name.place(x=150,y=100,width=200)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_email.place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","Male","Female","other"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=480,y=60,width=200)

        #========column2==========================
        lbl_dob=Label(self.root,text="D.O.B.",font=("goudy old style ",15,'bold'),bg='White').place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style ",15,'bold'),bg='White').place(x=360,y=100)
        lbl_addmission=Label(self.root,text="Addmission",font=("goudy old style ",15,'bold'),bg='White').place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style ",15,'bold'),bg='White').place(x=360,y=180)


        #====Entry Fields==========
        self.course_list=[]
        #function_call to update the list
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_dob.place(x=480,y=60,width=200)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_contact.place(x=480,y=100,width=200)
        self.txt_addmission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_addmission.place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
       # self.txt_course.current.set("Empty")

        #========Text Address========================

        self.txt_address=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_address.place(x=150,y=260,width=540,height=100)

        #====Buttons===============
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="black")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="black")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="black")
        self.btn_update.place(x=390,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="black")
        self.btn_update.place(x=510,y=400,width=110,height=40)
        #====search panel=============
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No",font=("goud old style",15,'bold'),bg='white').place(x=720,y=60)
        self.txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=870,y=60)
        self.btn_search=Button(self.root,text='search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1070,y=60)

        #======content====================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.Coursetable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact,admission","course","state","city","pin","adrees"),xscrollcommand=Scrollbar.set)

       # scrollx.pack(side=BOTTOM,fill=x)
      #  scrolly.pack(side=RIGHT,fill=y)
        scrollx.config(command=self.Coursetable.xview)
        scrollx.config(command=self.Coursetable.yview)

        
root=Tk()
obj=dashboard(root)
root.mainloop()   



'''
        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender" ,text="Gender")
        self.CourseTable.heading("dob" ,text="D.O.B")
        self.CourseTable.heading("contact" ,text="Contact")
        self.CourseTable.heading("admission" ,text="Admission")
        self.CourseTable.heading("course" ,text="Course")
        self.CourseTable.heading("state" ,text="State")
        self.CourseTable.heading("city", text="city")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.heading("roll",width=100)
        self.CourseTable.heading("name",width=100)
        self.CourseTable.heading("email",width=100)
        self.CourseTable.heading("gender",width=100)
        self.CourseTable.heading("dob",width=100)
        self.CourseTable.heading("contact",width=100)
        self.CourseTable.heading("admission",width=100)
        self.CourseTable.heading("course",width=100)
        self.CourseTable.heading("state",width=100)
        self.CourseTable.heading("city",width=100)
        self.CourseTable.heading("pin",width=100)
        self.CourseTable.heading("address",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()      

    #====================================================================

def clear(self):
     self.show() 
     self.var_roll.set("")  
     self.var_name.set("") 
     self.var_email.set("") 
     self.var_gender.set("") 
     self.var_dob.set("")
     self.var_contact.set("")
     self.var_a_date.set("")
     self.var_a_course.set("")
     self.var_a_state.set("")
     self.var_a_city.set("")
     self.var_a_pin.set("")
     self.txt_address.delete('1.0',END)
     self.txt_roll.config(state=NORMAL)

def delete(self):
    con=pyodbc.connect(database="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from student where name=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror("Error","please select  from student the list first",)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cur.execute("delete from course where name=?",(self.var_roll.get(),))
                    con.comit()
                    messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                    self.clear()

    except Exception as ex:
            messagebox.showerror("Error",f"Error dur to{str(ex)}") 
def get_data(self,ev):
       self.txt_roll.config(state='readonly')
       r=self.CourseTable.focus()
       content=self.CourseTable.item(r)
       row=content["values"]
       self.var_roll.set(row[0])
       self.var_name.set(row[1])
       self.var_email.set(row[2])
       self.var_gender.set(row[3])
       self.var_dob.set(row[4])
       self.var_contact.set(row[5])
       self.var_a_date.set(row[6])
       self.var_course.set(row[7])
       self.var_state.set(row[8])
       self.var_city.set(row[9])
       self.var_pin.set(row[10])
       self.txt_address.delete("1.0",END)
       self.txt_address.insert(END,row[11])

def add(self):
    con=pyodbc.connect(databadase="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get=="" :
           messagebox.showerror("Error","Roll Number should be required",parent=self.root)
        else:
            cur.execute("select * from student where roll=?,(self.var_roll.get(),")
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error student where roll=?",(self.var_roll.get(),))  
            else:
                cur.execute("insert into student(roll,name,gender,dob,contact,admin)\
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.var_address.get("1.0",END)
                )
                con.commit()
                messagebox.showerror("Success","student Added Successfully",parent=self.root)
            self.show()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")


def update(self):
    con=pyodbc.connect(database="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll No. Should be required",parent=self.root)
        else:
            cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Select roll from list",parent=self.root)  
            else:
                cur.execute("update student set duration=?,charges=?,description=?where")
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_description.get("1.0",END),
                self.var_roll.get()
                    
                con.commit()
                messagebox.showerror("Success","student Added Successfully",parent=self.root)
                self.show()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")
def show(self):
    con=pyodbc.connect(database="RMSDB")  
    cur=con.cursor()
    try:
        cur.execute("select * from student") 
        rows=cur.fetchll()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert('',END,values=row)
    except Exception as ex:
       messagebox.showerror("Error",f"Error due to {str(ex)}")


def fetch_course(self): 
    con=pyodbc.connect(database="rms.db")  
    cur=con.cursor()
    try:
        cur.execute("select * name from course") 
        rows=cur.fetchll()
        if len(rows)>0:
            for row in rows:
                self.course_list.append(row[0])
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to{str(ex)}")            


def search(self):
    con=pyodbc.connect(database="rms.db")  
    cur=con.cursor()
    try:    
        cur.execute(f"select * from student where roll=?",(self.var_roll.get())) 
        row=cur.fetchone()
        #print(row)
        if row!=None:
          self.CourseTable.delete(*self.CourseTable.get_children())
          self.courseTable.insert('',END,values=row)
        else:   
            messagebox.showerror("Error","No record found",parent=self.root)      
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to{str(ex)}")      

root=Tk()
obj=dashboard(root)
root.mainloop()      
'''