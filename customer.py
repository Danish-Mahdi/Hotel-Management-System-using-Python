from tkinter import *
# from pil import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
        def __init__(self, root):
                self.root=root
                self.root.title('Hotel Management System')
                # self.root.geometry('1295x550+230+200')
                self.root.geometry('1150x540+210+160')



                # variables
                self.var_ref=StringVar()
                x=random.randint(1000,9999)
                self.var_ref.set(str(x))

                self.var_cust_name=StringVar()
                self.var_father=StringVar()
                self.var_gender=StringVar()
                self.var_post=StringVar()
                self.var_mobile=StringVar()
                self.var_email=StringVar()
                self.var_nationality=StringVar()
                self.var_address=StringVar()
                self.var_id_proof=StringVar()
                self.var_id_number=StringVar()









                # title

                lbl_title=Label(self.root, text="ADD CUSTOMER DETAILS", font=('times new roman', 18,'bold'),bg='green',fg='white', bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1295,height=50)

                                #logo

                
                # img2=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img2=img1.resize(100,40),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg1,bd=0,relief=RIDGE)
                # lblimg.place(x=5,y=2,width=100,height=40)



                # label frame
                LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE, text="Customer Details", font=('arial',12,'bold'),padx=2)
                # LabelFrameleft.place(x=5,y=50, width=425,height=490)
                LabelFrameleft.place(x=5,y=50, width=350,height=490)

                # labels and entrys
        # cust ref
                lbl_cust_ref=Label(LabelFrameleft,text='Customer Ref', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_cust_ref.grid(row=0,column=0,sticky=W)

                entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref, width=22,font=('times new roman',13,'bold'),state='readonly')
                entry_ref.grid(row=0,column=1)
                
                
                
        # cust name
                cname=Label(LabelFrameleft,text='Customer Name:', font=('arial',12,'bold'),padx=2,pady=6)
                cname.grid(row=1,column=0,sticky=W)

                txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_name, width=22,font=('arial',13,'bold'))
                txtcname.grid(row=1,column=1)
                
                
                
                # Father name
                lblmname=Label(LabelFrameleft,text='Father Name:', font=('arial',12,'bold'),padx=2,pady=6)
                lblmname.grid(row=2,column=0,sticky=W)

                txtmname=ttk.Entry(LabelFrameleft,textvariable=self.var_father, width=22,font=('arial',12,'bold'))
                txtmname.grid(row=2,column=1)

        # 29 width

                #gender combobox
                label_gender=Label(LabelFrameleft,text='Gender :', font=('arial',12,'bold'),padx=2,pady=6)
                label_gender.grid(row=3,column=0,sticky=W)

                combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,width=20,state='readonly',font=('arial',12,'bold'))
                combo_gender['value']=("Male","Female","Other")
                combo_gender.current(0)
                combo_gender.grid(row=3,column=1)



                # postcode
                lblPostCode=Label(LabelFrameleft,text='Post Code:', font=('arial',12,'bold'),padx=2,pady=6)
                lblPostCode.grid(row=4,column=0,sticky=W)

                txtPostCode=ttk.Entry(LabelFrameleft,textvariable=self.var_post ,width=22,font=('arial',12,'bold'))
                txtPostCode.grid(row=4,column=1)


                # mobile number
                lblMobile=Label(LabelFrameleft,text='Mobile Number:', font=('arial',12,'bold'),padx=2,pady=6)
                lblMobile.grid(row=5,column=0,sticky=W)

                txtMobile=ttk.Entry(LabelFrameleft,textvariable=self.var_mobile, width=22,font=('arial',12,'bold'))
                txtMobile.grid(row=5,column=1)




                # email
                lblEmail=Label(LabelFrameleft,text='Email:', font=('arial',12,'bold'),padx=2,pady=6)
                lblEmail.grid(row=6,column=0,sticky=W)

                txtEmail=ttk.Entry(LabelFrameleft,textvariable=self.var_email, width=22,font=('arial',12,'bold'))
                txtEmail.grid(row=6,column=1)




                # nationality
                lblNationality=Label(LabelFrameleft,text='Nationality:', font=('arial',12,'bold'),padx=2,pady=6)
                lblNationality.grid(row=7,column=0,sticky=W)

                combo_Nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,width=20,state='readonly',font=('arial',12,'bold'))
                combo_Nationality['value']=("Pakistani","American","Chinese")
                combo_Nationality.current(0)
                combo_Nationality.grid(row=7,column=1)


                # ID proof Type
                lblIdProof=Label(LabelFrameleft,text='ID Proof type:', font=('arial',12,'bold'),padx=2,pady=6)
                lblIdProof.grid(row=8,column=0,sticky=W)

                combo_id=ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,width=20,state='readonly',font=('arial',12,'bold'))
                combo_id['value']=("CNIC","StudentCard","DrivingLicence")
                combo_id.current(0)
                combo_id.grid(row=8,column=1)



                # ID no
                lblIdNumber=Label(LabelFrameleft,text='ID No:', font=('arial',12,'bold'),padx=2,pady=6)
                lblIdNumber.grid(row=9,column=0,sticky=W)

                txtIdNumber=ttk.Entry(LabelFrameleft,textvariable=self.var_id_number, width=22,font=('arial',12,'bold'))
                txtIdNumber.grid(row=9,column=1)

                # Address
                lblAddress=Label(LabelFrameleft,text='Address:', font=('arial',12,'bold'),padx=2,pady=6)
                lblAddress.grid(row=10,column=0,sticky=W)

                txtAddress=ttk.Entry(LabelFrameleft, textvariable=self.var_address,width=22,font=('arial',12,'bold'))
                txtAddress.grid(row=10,column=1)



        # btns
                btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
                btn_frame.place(x=0,y=400,width=412,height=40)
        # add
                btnAdd=Button(btn_frame,text="ADD",command=self.add_data,width=8,font=('arial',11,'bold'),bg='green',fg='white')
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

        # Table frame Search System
                # label frame
                Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE, text="View Details and Search System", font=('arial',12,'bold'),padx=2)
                # Table_Frame.place(x=435,y=50, width=860,height=490)
                Table_Frame.place(x=375,y=50, width=860,height=490)

                lblSearchBy=Label(Table_Frame,text='Search By:', font=('arial',12,'bold'),bg='red',fg='white')

                lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

                self.search_var=StringVar()


                combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,width=24,state='readonly',font=('arial',12,'bold'))
                combo_Search['value']=("Mobile","Ref")
                combo_Search.current(0)
                combo_Search.grid(row=0,column=1,padx=2)

                self.txt_search=StringVar()

                txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, width=24,font=('arial',12,'bold'))
                txtSearch.grid(row=0,column=2,padx=2)


                btnSearch=Button(Table_Frame,command=self.search,text="Search",width=8,font=('arial',11,'bold'),bg='green',fg='white')
                btnSearch.grid(row=0,column=3,padx=1)
                
                btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",width=10,font=('arial',11,'bold'),bg='green',fg='white')
                btnShowAll.grid(row=0,column=4,padx=1)


        # show data table

                details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
                details_table.place(x=0,y=50,width=750,height=350)


                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

                self.Cust_Details_Table=ttk.Treeview(details_table,columns=('ref','name','father','gender','post','mobile','email','nationality','idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.Cust_Details_Table.xview)
                scroll_y.config(command=self.Cust_Details_Table.yview)


                self.Cust_Details_Table.heading('ref',text='Refer No')
                
                self.Cust_Details_Table.heading('name',text='Name')
                self.Cust_Details_Table.heading('father',text='Father Name')

                self.Cust_Details_Table.heading('gender',text='Gender')
                self.Cust_Details_Table.heading('post',text='Post Code')
                
                self.Cust_Details_Table.heading('mobile',text='Mobile No')
                self.Cust_Details_Table.heading('email',text='Email')
                
                self.Cust_Details_Table.heading('nationality',text='Nationality')
                self.Cust_Details_Table.heading('idproof',text='Id Proof')
                self.Cust_Details_Table.heading('idnumber',text='Id Number')
                self.Cust_Details_Table.heading('address',text='Address')

                self.Cust_Details_Table['show']="headings"

                # width set
                self.Cust_Details_Table.column('ref',width=100)
                
                self.Cust_Details_Table.column('name',width=100)
                self.Cust_Details_Table.column('father',width=100)

                self.Cust_Details_Table.column('gender',width=100)
                self.Cust_Details_Table.column('post',width=100)
                
                self.Cust_Details_Table.column('mobile',width=100)
                self.Cust_Details_Table.column('email',width=100)
                
                self.Cust_Details_Table.column('nationality',width=100)
                self.Cust_Details_Table.column('idproof',width=100)
                self.Cust_Details_Table.column('idnumber',width=100)
                self.Cust_Details_Table.column('address',width=100)


                self.Cust_Details_Table.pack(fill=BOTH,expand=1)
                self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()


        def add_data(self):
                if self.var_mobile.get()==''or self.var_father.get()=='':
                        messagebox.showerror("Error","All fields are required",parent=self.root) 
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_ref.get(),
                                        self.var_cust_name.get(),
                                        self.var_father.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nationality.get(),
                                        self.var_id_proof.get(),
                                        self.var_id_number.get(),
                                        self.var_address.get()
                                        ))

                                conn.commit()
                                self.fetch_data()
                                conn.close()

                                messagebox.showinfo("Success","customer has been added",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent
                                =self.root)





        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()
                
                my_cursor.execute('select * from customer')
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                        for i in rows:
                                 # type: ignore
                                self.Cust_Details_Table.insert("",END,values=i)
                       
                        conn.commit()

                conn.close()




        def get_cursor(self,event=""):
                cursor_row=self.Cust_Details_Table.focus()
                content=self.Cust_Details_Table.item(cursor_row)
                row=content['values']

                self.var_ref.set(row[0]),
                self.var_cust_name.set(row[1]),
                self.var_father.set(row[2]),
                self.var_gender.set(row[3]),
                self.var_post.set(row[4]),
                self.var_mobile.set(row[5]),
                self.var_email.set(row[6]),
                self.var_nationality.set(row[7]),
                self.var_id_proof.set(row[8]),
                self.var_id_number.set(row[9]),
                self.var_address.set(row[10])




        def update(self):
                if self.var_mobile.get()=="":
                        messagebox.showerror("Error","Please enter mobile number",parent=self.root)

                else:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor()
                
                        my_cursor.execute('update customer set Name=%s, Father=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s, Nationality=%s,Idproof=%s, Idnumber=%s,Address=%s where Ref=%s',( self.var_cust_name.get(),
                                                                self.var_father.get(),
                                                                self.var_gender.get(),
                                                                self.var_post.get(),
                                                                self.var_mobile.get(),
                                                                self.var_email.get(),
                                                                self.var_nationality.get(),
                                                                self.var_id_proof.get(),
                                                                self.var_id_number.get(),
                                                                self.var_address.get(),
                                                                self.var_ref.get()))
                        
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update", "Customer details has been updated sucessfully",parent=self.root)





        def mDelete(self):
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
                if mDelete>0:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor() 
                        query = "DELETE FROM customer WHERE Ref = %s"
                        # query="delete from customer Ref=%s"
                        value=(self.var_ref.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mDelete:
                                return
                conn.commit()
                self.fetch_data()
                conn.close()





        def reset(self):
                # self.var_ref.set(""),
                self.var_cust_name.set(""),
                self.var_father.set(""),
                # self.var_gender.set(""),
                self.var_post.set(""),
                self.var_mobile.set(""),
                self.var_email.set(""),
                # self.var_nationality.set(""),
                # self.var_id_proof.set(""),
                self.var_id_number.set(""),
                self.var_address.set("")


                
                x=random.randint(1000,9999)
                self.var_ref.set(str(x))



        def search(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()

                # my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
                my_cursor.execute("SELECT * FROM customer WHERE {} LIKE %s".format(self.search_var.get()), ('%' + str(self.txt_search.get()) + '%',))

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

                        for i in rows:
                                self.Cust_Details_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()








if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()