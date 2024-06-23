from tkinter import *
# from pil import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strptime 



class DetailsRoom:
        def __init__(self, root):
                self.root=root
                self.root.title('Hotel Management System')
                # self.root.geometry('1295x550+230+200')
                self.root.geometry('1150x540+210+160')



        
  # title

                lbl_title=Label(self.root, text="New Room Add", font=('times new roman', 18,'bold'),bg='green',fg='white', bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1295,height=50)

                                    #logo

                    
                # img2=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img2=img1.resize(100,40),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg1,bd=0,relief=RIDGE)
                # lblimg.place(x=5,y=2,width=100,height=40)



                    # label frame
                LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE, text="New Room Add", font=('arial',12,'bold'),padx=2)
                # LabelFrameleft.place(x=5,y=50, width=425,height=490)
                LabelFrameleft.place(x=5,y=50, width=550,height=350)


                         # labels and entrys
        # Floor
                lbl_floor=Label(LabelFrameleft,text='Floor', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_floor.grid(row=0,column=0,sticky=W, padx=20)


                self.var_floor=StringVar()
                entry_floor=ttk.Entry(LabelFrameleft, textvariable=self.var_floor,width=16,font=('times new roman',13,'bold'))
                entry_floor.grid(row=0,column=1,sticky=W)
                
                
                
                #Room no
                lbl_RoomNo=Label(LabelFrameleft,text='Room No', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_RoomNo.grid(row=1,column=0,sticky=W, padx=20)


                self.var_roomNo=StringVar()
                entry_RoomNo=ttk.Entry(LabelFrameleft, textvariable=self.var_roomNo,width=16,font=('times new roman',13,'bold'))
                entry_RoomNo.grid(row=1,column=1,sticky=W)
                
                
                
            # Room Type
                lbl_RoomType=Label(LabelFrameleft,text='Room Type', font=('arial',12,'bold'),padx=2,pady=6)
                lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

                self.var_RoomType=StringVar()

                entry_RoomType=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomType, width=16,font=('times new roman',13,'bold'))
                entry_RoomType.grid(row=2,column=1,sticky=W)


 # btns
                btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
                btn_frame.place(x=0,y=200,width=340,height=40)
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
                Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE, text="Show Room Details", font=('arial',12,'bold'),padx=2)
                # Table_Frame.place(x=435,y=50, width=860,height=490)
                Table_Frame.place(x=575,y=55, width=575,height=350)
# scroll

                scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

                self.room_Table=ttk.Treeview(Table_Frame,columns=('floor','roomno','roomType'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.room_Table.xview)
                scroll_y.config(command=self.room_Table.yview)

# table show columns

                self.room_Table.heading('floor',text='Floor')
                self.room_Table.heading('roomno',text='Room No')
                self.room_Table.heading('roomType',text='Room Type')
                
               
                self.room_Table['show']="headings"

                # width set
                self.room_Table.column('floor',width=100)
                
                self.room_Table.column('roomno',width=100)
                self.room_Table.column('roomType',width=100)


                self.room_Table.pack(fill=BOTH,expand=1)
                self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()



# add data
        def add_data(self):
            if self.var_floor.get()==''or self.var_RoomType.get()=='':
                    messagebox.showerror("Error","All fields are required",parent=self.root) 
            else:
                    try:
                            conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into details values(%s,%s,%s)",(
                                    self.var_floor.get(),
                                    self.var_roomNo.get(),
                                    self.var_RoomType.get()
                                    ))

                            conn.commit()
                            self.fetch_data()
                            conn.close()

                            messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                    except Exception as es:
                            messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent
                            =self.root)


# fetch data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                my_cursor=conn.cursor()   
                my_cursor.execute('select * from details')
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.room_Table.delete(*self.room_Table.get_children())
                        for i in rows:
                                 # type: ignore
                                self.room_Table.insert("",END,values=i)
                       
                        conn.commit()

                conn.close()




        def update(self):
                        if self.var_floor.get()=="":
                                messagebox.showerror("Error","Please enter floor number",parent=self.root)

                        else:
                                conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                                my_cursor=conn.cursor()
                        
                                my_cursor.execute('update details set Floor=%s,RoomType=%s where RoomNo=%s',( 
                                                self.var_floor.get(),
                                                self.var_RoomType.get(),
                                                self.var_roomNo.get()          
                                                ))  
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Update", "New Room details have been updated sucessfully",parent=self.root)





  
# get cursor function
        def get_cursor(self,event=""):
                cursor_row=self.room_Table.focus()
                content=self.room_Table.item(cursor_row)
                row=content['values']
                self.var_floor.set(row[0])
                self.var_roomNo.set(row[1])
                self.var_RoomType.set(row[2])
              




         # Delete Function
        def mDelete(self):
                mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details?",parent=self.root)
                if mDelete>0:
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor() 
                        query = "DELETE FROM details WHERE RoomNo  = %s"
                        # query="delete from customer Ref=%s"
                        value=(self.var_roomNo.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mDelete:
                                return
                conn.commit()
                self.fetch_data()
                conn.close()




         # reset function

        def reset(self):
                self.var_floor.set(""),
                self.var_roomNo.set(""),
                self.var_RoomType.set("")
             










if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()