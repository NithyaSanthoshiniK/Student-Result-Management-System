from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class dashboard:
    def __init__(self,root):
       
        self.root=root
        self.root.title("DASHBOARD")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="White")


        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/yageshakhil/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #====Register Frame=====
        frame2=Frame(self.root, bg= "white")
        frame2.place(x=480, y=100, width=700, height=500)

        title=Label(frame2, text= "DASHBOARD" ,font=("times new roman" ,20, "bold"),bg="white",fg='green').place(x=50,y=30)

        btn=Button(frame2, text="Manage Student Details",font=("times new roman" ,15, "bold"),command=self.ManageStudentDetails_window, bg="green",fg='green').place(x=200,y=170)
        btn=Button(frame2, text="Manage Course Details",font=("times new roman" ,15, "bold"),command=self.ManageCourseDetails_window,bg="green",fg='green').place(x=200,y=240)
        btn=Button(frame2, text="View Results",font=("times new roman" ,15, "bold"),command=self.ViewResults_window,bg="green",fg='green').place(x=200,y=310)

    def ManageCourseDetails_window(self):
        self.root.destroy()
        import managecoursedetails

    def ManageStudentDetails_window(self):
        self.root.destroy()
        import managestudentdetails
      

    def ViewResults_window(self):
        self.root.destroy()
        import mainscreen2

   
root=Tk()
obj=dashboard(root)
root.mainloop()