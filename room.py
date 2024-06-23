from tkinter import *
# from pil import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strptime 



class Roombooking:
        def __init__(self, root):
                self.root=root
                self.root.title('Hotel Management System')
                # self.root.geometry('1295x550+230+200')
                self.root.geometry('1150x540+210+160')
 

                # variables
                self.var_contact=StringVar()
                self.var_checkin=StringVar()
                self.var_checkout=StringVar()
                self.var_roomtype=StringVar()
                self.var_roomavailable=StringVar()
                self.var_meal=StringVar()
                self.var_noofdays=StringVar()
                self.var_paidtax=StringVar()
                self.var_actual=StringVar()
                self.var_total=StringVar()




 
  # title

                lbl_title=Label(self.root, text="ROOM BOOKING DETAILS", font=('times new roman', 18,'bold'),bg='green',fg='white', bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1295,height=50)

                                #logo

                
                # img2=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img2=img1.resize(100,40),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg1,bd=0,relief=RIDGE)
                # lblimg.place(x=5,y=2,width=100,height=40)



                  # label frame
                LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE, text="Room Booking Details", font=('arial',12,'bold'),padx=2)
                # LabelFrameleft.place(x=5,y=50, width=425,height=490)
                LabelFrameleft.place(x=5,y=50, width=375,height=490)




                         # labels and entrys
        # cust Contact
                lbl_cust_contact=Label(LabelFrameleft,text='Customer Contact', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_cust_contact.grid(row=0,column=0,sticky=W)

                entry_contact=ttk.Entry(LabelFrameleft, textvariable=self.var_contact, width=16,font=('times new roman',13,'bold'))
                entry_contact.grid(row=0,
                column=1,sticky=W)


# fetch data button
                btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",width=8,font=('arial',8,'bold'),bg='green',fg='white')
                btnFetchData.place(x=300,y=4)




# check in date
                check_in_date=Label(LabelFrameleft,text='Check_in Date:', font=('arial',12,'bold'),padx=2,pady=6)
                check_in_date.grid(row=1,column=0,sticky=W)

                txtcheck_in_date=ttk.Entry(LabelFrameleft, textvariable=self.var_checkin,width=22,font=('arial',13,'bold'))
                txtcheck_in_date.grid(row=1,column=1)


# check out date
                lbl_Check_out_date=Label(LabelFrameleft,text='Check_Out Date:', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_Check_out_date.grid(row=2,column=0,sticky=W)

                txt_Check_out=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout ,width=22,font=('arial',13,'bold'))
                txt_Check_out.grid(row=2,column=1) 

# Room type
                label_RoomType=Label(LabelFrameleft,text='Room Type:', font=('arial',12,'bold'),padx=2,pady=6)
                label_RoomType.grid(row=3,column=0,sticky=W)


                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()   
                my_cursor.execute('select RoomType from details')
                ide=my_cursor.fetchall()


                combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,width=20,state='readonly',font=('arial',12,'bold'))
                combo_RoomType['value']=ide
                combo_RoomType.current(0)
                combo_RoomType.grid(row=3,column=1)



# Available Room
                lblRoomAvailable=Label(LabelFrameleft,text='Available Room:', font=('arial',12,'bold'),padx=2,pady=6)
                lblRoomAvailable.grid(row=4,column=0,sticky=W)

                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()   
                my_cursor.execute('select RoomNo from details')
                rows=my_cursor.fetchall()
                # txtRoomAvailable=ttk.Entry(LabelFrameleft,textvariable=self.var_roomavailable, width=22,font=('arial',13,'bold'))
                # txtRoomAvailable.grid(row=4,column=1) 
                combo_RoomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,width=20,state='readonly',font=('arial',12,'bold'))
                combo_RoomNo['value']=rows
                combo_RoomNo.current(0)
                combo_RoomNo.grid(row=4,column=1)




# Meal
                lblMeal=Label(LabelFrameleft,text='Meal:', font=('arial',12,'bold'),padx=2,pady=6)
                lblMeal.grid(row=5,column=0,sticky=W)

                txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal ,width=22,font=('arial',13,'bold'))
                txtMeal.grid(row=5,column=1)  

# No of Days

                lblNoOfDays=Label(LabelFrameleft,text='No of Days:', font=('arial',12,'bold'),padx=2,pady=6)
                lblNoOfDays.grid(row=6,column=0,sticky=W)

                txtNoOfDays=ttk.Entry(LabelFrameleft, textvariable=self.var_noofdays,width=22,font=('arial',13,'bold'))
                txtNoOfDays.grid(row=6,column=1)  

# Paid Tax

                lblNoOfDays=Label(LabelFrameleft,text='Paid Tax:', font=('arial',12,'bold'),padx=2,pady=6)
                lblNoOfDays.grid(row=7,column=0,sticky=W)

                txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax ,width=22,font=('arial',13,'bold'))
                txtNoOfDays.grid(row=7,column=1)  

# Sub Total

                lblNoOfDays=Label(LabelFrameleft,text='Sub Total', font=('arial',12,'bold'),padx=2,pady=6)
                lblNoOfDays.grid(row=8,column=0,sticky=W)

                txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_actual ,width=22,font=('arial',13,'bold'))
                txtNoOfDays.grid(row=8,column=1) 
                
     #Total Cost

                lblNoOfDays=Label(LabelFrameleft,text='Total Cost', font=('arial',12,'bold'),padx=2,pady=6)
                lblNoOfDays.grid(row=9,column=0,sticky=W)

                txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_total ,width=22,font=('arial',13,'bold'))
                txtNoOfDays.grid(row=9,column=1)  


         # Bill Button
                btnAdd=Button(LabelFrameleft,text="Bill",command=self.total,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnAdd.grid(row=10,column=0,padx=1,sticky=W)





        # btns
                btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
                btn_frame.place(x=0,y=400,width=412,height=40)
        # add
                btnAdd=Button(btn_frame,text="ADD",command=self.add_data ,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnAdd.grid(row=0,column=0,padx=1)
                
                # Update
                btnUpdate=Button(btn_frame,text="Update",command=self.update,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnUpdate.grid(row=0,column=1,padx=1)
                
                # Delete
                btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnDelete.grid(row=0,column=2,padx=1)
                
                # Reset
                btnReset=Button(btn_frame,text="Reset",command=self.reset,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnReset.grid(row=0,column=3,padx=1)


        # Right Side Image

                   #logo

                
                # img3=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img3=img1.resize(520,300),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg3,bd=0,relief=RIDGE)
                # lblimg.place(x=760,y=55,width=520,height=200)





                
        # Table frame Search System
                # label frame
                Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE, text="View Details and Search System", font=('arial',12,'bold'),padx=2)
                # Table_Frame.place(x=435,y=50, width=860,height=490)
                Table_Frame.place(x=375,y=280, width=860,height=260)

                lblSearchBy=Label(Table_Frame,text='Search By:', font=('arial',12,'bold'),bg='red',fg='white')

                lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

                self.search_var=StringVar()


                combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,width=24,state='readonly',font=('arial',12,'bold'))
                combo_Search['value']=("Contact","Room")
                combo_Search.current(0)
                combo_Search.grid(row=0,column=1,padx=2)

                self.txt_search=StringVar()

                txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, width=24,font=('arial',12,'bold'))
                txtSearch.grid(row=0,column=2,padx=2)


                btnSearch=Button(Table_Frame,text="Search",command=self.search,width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnSearch.grid(row=0,column=3,padx=1)
                
                btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,width=10,font=('arial',11,'bold'),bg='green',fg='white')
                btnShowAll.grid(row=0,column=4,padx=1)



                
        # show data table

                details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
                details_table.place(x=0,y=50,width=750,height=180)


                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

                self.room_Table=ttk.Treeview(details_table,columns=('contact','checkin','checkout','roomtype','roomavailable','meal','noOfdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.room_Table.xview)
                scroll_y.config(command=self.room_Table.yview)


                self.room_Table.heading('contact',text='Contact')
                
                self.room_Table.heading('checkin',text='Check-in')
                self.room_Table.heading('checkout',text='Check-out')

                self.room_Table.heading('roomtype',text='Room Type')
                self.room_Table.heading('roomavailable',text='Room No')
                
                self.room_Table.heading('meal',text='Meal')
                self.room_Table.heading('noOfdays',text='NoOfDays')
               
                self.room_Table['show']="headings"

                # width set
                self.room_Table.column('contact',width=100)
                
                self.room_Table.column('checkin',width=100)
                self.room_Table.column('checkout',width=100)

                self.room_Table.column('roomtype',width=100)
                self.room_Table.column('roomavailable',width=100)
                
                self.room_Table.column('meal',width=100)
                self.room_Table.column('noOfdays',width=100)
                

                self.room_Table.pack(fill=BOTH,expand=1)
                

                self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()

        
        def add_data(self):
                if self.var_contact.get()==''or self.var_checkin.get()=='':
                        messagebox.showerror("Error","All fields are required",parent=self.root) 
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_contact.get(),
                                        self.var_checkin.get(),
                                        self.var_checkout.get(),
                                        self.var_roomtype.get(),
                                        self.var_roomavailable.get(),
                                        self.var_meal.get(),
                                        self.var_noofdays.get()
                                        ))

                                conn.commit()
                                self.fetch_data()
                                conn.close()

                                messagebox.showinfo("Success","Room booked",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent
                                =self.root)



        
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()
                
                my_cursor.execute('select * from room')
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.room_Table.delete(*self.room_Table.get_children())
                        for i in rows:
                                 # type: ignore
                                self.room_Table.insert("",END,values=i)
                       
                        conn.commit()

                conn.close()

        
        # get cursor function
        def get_cursor(self,event=""):
                cursor_row=self.room_Table.focus()
                content=self.room_Table.item(cursor_row)
                row=content['values']
                self.var_contact.set(row[0])
                self.var_checkin.set(row[1])
                self.var_checkout.set(row[2])
                self.var_roomtype.set(row[3])
                self.var_roomavailable.set(row[4])
                self.var_meal.set(row[5])
                self.var_noofdays.set(row[6])

        # Update Functon



        def update(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error","Please enter Contact number",parent=self.root)

                else:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor()
                
                        my_cursor.execute('update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,meal=%s, noOfdays=%s where Contact=%s',( 
                                        self.var_checkin.get(),
                                        self.var_checkout.get(),
                                        self.var_roomtype.get(),
                                        self.var_roomavailable.get(),
                                        self.var_meal.get(),
                                        self.var_noofdays.get(),
                                        self.var_contact.get()
                                        ))
                        
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update", "Room details have been updated sucessfully",parent=self.root)



        
        # Delete Function
        def mDelete(self):
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
                if mDelete>0:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor() 
                        query = "DELETE FROM room WHERE contact = %s"
                        # query="delete from customer Ref=%s"
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mDelete:
                                return
                conn.commit()
                self.fetch_data()
                conn.close()

        # reset function

        def reset(self):
                # self.var_ref.set(""),
                self.var_contact.set("")
                self.var_checkin.set("")
                self.var_checkout.set("")
                self.var_roomtype.set("")
                self.var_roomavailable.set("")
                self.var_meal.set("")
                self.var_noofdays.set("")
                self.var_paidtax.set("")
                self.var_actual.set("")
                self.var_total.set("")
                
                # x=random.randint(1000,9999)
                # self.var_ref.set(str(x))







        



# all data fetch

        def Fetch_contact(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error","Please enter Contact Number", parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor()
                        query=('select Name from customer where Mobile=%s')
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        if row==None:
                                messagebox.showerror("Error","This number not found",parent=self.root)
                        else:
                                conn.commit()
                                conn.close()

                                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                                showDataframe.place(x=440,y=55,width=300,height=180)


                                lblName=Label(showDataframe,text='Name:',font=('arial',12,'bold'))
                                lblName.place(x=0,y=0)


                                lbl=Label(showDataframe,text=row,font=('arial',12,'bold'))
                                lbl.place(x=90,y=0)
                




                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                                my_cursor=conn.cursor()
                                query=('select Gender from customer where Mobile=%s')
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblGender=Label(showDataframe,text='Gender:',font=('arial',12,'bold'))
                                lblGender.place(x=0,y=30)

                                lbl2=Label(showDataframe,text=row,font=('arial',12,'bold'))
                                lbl2.place(x=90,y=30)
        
                        


                # email
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        
                                my_cursor=conn.cursor()
                                query=('select Email from customer where Mobile=%s')
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblEmail=Label(showDataframe,text='Email:',font=('arial',12,'bold'))
                                lblEmail.place(x=0,y=60)

                                lbl3=Label(showDataframe,text=row,font=('arial',12,'bold'))
                                lbl3.place(x=90,y=60)

# nationality
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')

                                my_cursor=conn.cursor()
                                query=('select Nationality from customer where Mobile=%s')
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblNationality=Label(showDataframe,text='Nationality:',font=('arial',12,'bold'))
                                lblNationality.place(x=0,y=90)

                                lbl4=Label(showDataframe,text=row,font=('arial',12,'bold'))
                                lbl4.place(x=90,y=90)


# address
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')

                                my_cursor=conn.cursor()
                                query=('select Address from customer where Mobile=%s')
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                row=my_cursor.fetchone()

                                lblAddress=Label(showDataframe,text='Address:',font=('arial',12,'bold'))
                                lblAddress.place(x=0,y=120)

                                lbl5=Label(showDataframe,text=row,font=('arial',12,'bold'))
                                lbl5.place(x=90,y=120)

# search system
        def search(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()

                # my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
                my_cursor.execute("SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get()), ('%' + str(self.txt_search.get()) + '%',))

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.room_Table.delete(*self.room_Table.get_children())

                        for i in rows:
                                self.room_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()
       






                                # bill functions
        def total(self):
                inDate=self.var_checkin.get()
                outDate=self.var_checkout.get()
                inDate=datetime.strptime(inDate,"%d/%m/%Y")
                outDate=datetime.strptime(outDate,"%d/%m/%Y")
                self.var_noofdays.set(abs(outDate-inDate).days)
                        
                if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)

                                
                elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)
                        
                        
                elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
                        q1=float(400)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT) 
                        
                elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                        q1=float(400)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)
                        
                        
                        
                elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
                        q1=float(500)
                        q2=float(1500)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT) 


                elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Duplex"):
                        q1=float(500)
                        q2=float(1500)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)  
                        
                        
                elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
                        q1=float(500)
                        q2=float(1500)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)
                        
                        
                        
                elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
                        q1=float(500)
                        q2=float(1500)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)
                        
                elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                        q1=float(600)
                        q2=float(1500)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)   
                        
                        
                elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                        q1=float(600)
                        q2=float(1200)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT) 
                        
                elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
                        q1=float(600)
                        q2=float(1300)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)  
                
                elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
                        q1=float(600)
                        q2=float(1400)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        ST="Rs."+str("%.2f"%((q5)))
                        TT="Rs."+str("%.2f"%((q5+(q5)*0.1)))
                        self.var_paidtax.set(Tax)
                        self.var_actual.set(ST)
                        self.var_total.set(TT)

                                

























if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()