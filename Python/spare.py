 def add_data(self):
          flag_validation=True
          fname=self.txt_fname.get() # read name
          lname=self.txt_lname.get() # read name
          HallTicket=self.txt_HallTicket.get()# read name
          email=self.txt_email.get() # read name
          btech_regulation=self.cmb_btech_regulation.get()# read name
          department=self.txt_department.get() # read name
          password=self.txt_userpassword.get()# read name
          Cpassword=self.txt_Cpassword.get()# read name


          if(flag_validation):
              info=StringVar.set("Adding data...")
          #try:
            from sqlalchemy import create_engine
            from sqlalchemy.exc import SQLAlchemyError
            
            # add your mysql userid, password and db name here ##
            engine = create_engine("mysql+mysqldb://nithya:Akhil387*@127.0.0.1/RMSDB")
            
            query="INSERT INTO student_details (firstname, lastname, hallticketno,email,btech_regulation,department,userpassword,confirm_password)' \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            my_data=(fname,lname,HallTicket,email,btech_regulation,department,password,Cpassword)
            id=engine.execute(query,my_data) # insert data
            self.txt_fname.get().delete('1.0',END)  # reset the text entry box
            self.txt_lname.get().delete('1.0',END)  # reset the text entry box
            self.txt_HallTicket.get().delete('1.0',END)  # reset the text entry box
            self.txt_email.get().delete('1.0',END)  # reset the text entry box
            self.cmb_btech_regulation.get().delete('1.0',END)  # reset the text entry box
            self.txt_department.get().delete('1.0',END)  # reset the text entry box
            self.txt_userpassword.get().delete('1.0',END)  # reset the text entry box
            self.txt_Cpassword.get().delete('1.0',END)  # reset the text entry box



            (self.txt_fname.get(),
                              self.txt_lname.get(),
                              self.txt_HallTicket.get(),
                              self.txt_email.get(),
                              self.cmb_btech_regulation.get(),
                              self.txt_department.get(),
                              self.txt_userpassword.get(),
                              self.txt_Cpassword.get(),
                              )








       #     l5.grid() 
       #     l5.config(fg='green') # foreground color 
       #     l5.config(bg='white') # background color 
       #     my_str.set("ID:" + str(id.lastrowid))
       #     l5.after(3000,lambda:l5.config(fg='white',bg='white',text=''))
              
          #except SQLAlchemyError as e:
            #error = str(e.__dict__['orig'])
         #   l5.grid() 
            #return error
         #   l5.config(fg='red')   # foreground color
         #   l5.config(bg='yellow') # background color
            #print(error)
            #info.set(error)