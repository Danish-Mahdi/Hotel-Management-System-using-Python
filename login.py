from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from PIL import *

# pip install pillow
import mysql.connector



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        # BACKGROUND IMAGE


        self.bg=ImageTk.PhotoImage(file=r"D:\Hotel Management System-YT\images\hotel1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.root, bg="black")
        frame.place(x=570, y=170, width=340, height=450)


        # img1=Image.open(r"D:\Hotel Management System-YT\images\hotel3.jpg")
        # img1=img1.resize((100,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        # lblimg1.place(x=730,y=175,width=100,height=100)



        # img_path = r"D:\Hotel Management System-YT\images\hotel3.jpg"
        # img = Image.open(img_path)

        
        # img_resized = img.resize((100, 100), Image.LANCZOS)

      
        # self.photoimage1 = ImageTk.PhotoImage(img_resized)

    
        # lblimg1 = Label(root, image=self.photoimage1, bg="black", borderwidth=0)
        # lblimg1.place(x=730, y=175, width=100, height=100)




        

        











        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"), fg="white",bg="black")
        get_str.place(x=95,y=100)


        # label
        username=lbl=Label(frame,text="Username",font=("times new roman", 15,"bold"),fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman", 15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman", 15,"bold"),fg="white", bg="black")
        password.place(x=70, y=225)


        self.txtpass=ttk.Entry(frame,font=("times new roman", 15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)




# icon images
        # img2=Image.open(r"")
        # img2=img2.resize((25,25),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lblimg1.place(x=650,y=323,width=25,height=25)



        # img3=Image.open(r"")
        # img3=img3.resize((25,25),Image.ANTIALIAS)
        # self.photoimage3=ImageTk.PhotoImage(img3)
        # lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        # lblimg1.place(x=650,y=395,width=25,height=25)



    # login btn
        loginbtn=Button(frame,command=self.login,text='Login',font=("times new roman", 15,"bold"),bd=3,relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=300, width=120,height=35)



    # register button
        registerbtn=Button(frame,text='New User Register',command=self.register_window,font=("times new roman", 10,"bold"),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        registerbtn.place(x=15,y=350, width=160)

    # forgot password
        registerbtn=Button(frame,text='Forget Password',command=self.forgot_password_window,font=("times new roman", 10,"bold"),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        registerbtn.place(x=10,y=370, width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)






    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success", "login successful")
        else:  
            conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",( 
                self.txtuser.get(),
                self.txtpass.get()     
            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


# reset password window
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Q",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the ans",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Plz enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")

            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())

            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct ans",parent=self.root2)
            else:
                query=("update register set password=%s where email =%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)


                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, plz login new password", parent=self.root2)

                self.root2.destroy()













# forget password window


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please write email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")


                l=Label(self.root2,text="Forget Password",font=("times new roman", 20, "bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman", 15, "bold"),bg="white", fg='black')
                security_Q.place(x=50, y=80)


                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select", "Your Birth Place","Your Best friend name", "Your pet name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman", 15, "bold"),bg="white", fg='black')
                security_A.place(x=50, y=150)


                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)




                new_password=Label(self.root2,text="New Password",font=("times new roman", 15, "bold"),bg="white", fg='black')
                new_password.place(x=50, y=220)


                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
            
                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=100, y=290)







                       












# register class

class Register:
        def __init__(self,root):
                self.root=root
                self.root.title("Register")
                self.root.geometry("1600x900+0+0")

                # variables
                self.var_fname=StringVar()
                self.var_lname=StringVar()
                self.var_contact=StringVar()
                self.var_email=StringVar()
                self.var_securityQ=StringVar()
                self.var_SecurityA=StringVar()
                self.var_pass=StringVar()
                self.var_confpass=StringVar()

        # bg image
                self.bg=ImageTk.PhotoImage(file=r"D:\Hotel Management System-YT\images\hotel1.jpg")

                
                bg_lbl=Label(self.root, image=self.bg)
                bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


        # left image
                # self.bg1=ImageTk.PhotoImage(file=r"D:\Hotel Management System-YT\images\hotel3.jpg")
                img_path3 = r"D:\Hotel Management System-YT\images\hotel3.jpg"
                img3 = Image.open(img_path3)
                 # Resize the image
                img_resized = img3.resize((470, 550), Image.ANTIALIAS)

                # Convert the resized image to a PhotoImage object
                self.bg1 = ImageTk.PhotoImage(img_resized)

        # Create a label to display the resized image


                left_lb1=Label(self.root,image=self.bg1)
                left_lb1.place(x=50, y=100, width=470, height=550)


        # main frame
                frame=Frame(self.root, bg='white')
                frame.place(x=520,y=100,width=800,height=550)


                register_lb1=Label(frame, text="Register Here",font=("times new roman", 20, "bold"), fg="darkgreen",bg="white")
                register_lb1.place(x=20, y=20)


        # label and entry

        # row1
                fname=Label(frame,text="First Name",font=("times new roman", 15, "bold"),bg="white")
                fname.place(x=50, y=100)


                self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))

                self.fname_entry.place(x=50,y=130,width=250)
                
                
                
                lname=Label(frame,text="Last Name",font=("times new roman", 15, "bold"),bg="white", fg='black')
                lname.place(x=370, y=100)

                self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
                self.txt_lname.place(x=370,y=130,width=250)

        # row 2
                contact=Label(frame,text="Contact No",font=("times new roman", 15, "bold"),bg="white", fg='black')
                contact.place(x=50, y=170)


                self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
                self.txt_contact.place(x=50,y=200,width=250)




                email=Label(frame,text="Email",font=("times new roman", 15, "bold"),bg="white", fg='black')
                email.place(x=370, y=170)


                self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
                self.txt_email.place(x=370,y=200,width=250)



                # row3 
                security_Q=Label(frame,text="Select Security Questions",font=("times new roman", 15, "bold"),bg="white", fg='black')
                security_Q.place(x=50, y=240)


                self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select", "Your Birth Place","Your Best friend name", "Your pet name")
                self.combo_security_Q.place(x=50, y=270, width=250)
                self.combo_security_Q.current(0)




                
                
                
                security_A=Label(frame,text="Security Answer",font=("times new roman", 15, "bold"),bg="white", fg='black')
                security_A.place(x=370, y=240)


                self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
                self.txt_security.place(x=370,y=270,width=250)



                # row 4
                pswd=Label(frame,text="Password",font=("times new roman", 15, "bold"),bg="white", fg='black')
                pswd.place(x=50, y=310)

                self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
                self.txt_pswd.place(x=50,y=340,width=250)



                confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman", 15, "bold"),bg="white", fg='black')
                confirm_pswd.place(x=370, y=310)

                self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
                self.txt_confirm_pswd.place(x=370,y=340,width=250)
                



        # check btn
                self.var_check=IntVar()
                self.checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree to the terms and conditions",font=("times new roman",12,"bold"),onvalue=1, offvalue=0)
                self.checkbtn.place(x=50, y=380)

        # btn

                # img=Image.open(r"")
                # img=img.resize((200,50),Image.ANTIALIAS)
                # self.photoimage=ImageTk.PhotoImage(img)
                # b1=Button(frame, image=self.photoimage, borderwidth=0, cursor="hand2", font=("times new roman",12,"bold"))
                # b1.place(x=10, y=420, width=200) 



                # img1=Image.open(r"")
                # img1=img1.resize((200,50),Image.ANTIALIAS)
                # self.photoimage=ImageTk.PhotoImage(img1)
                # b1=Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman",12,"bold"))
                # b1.place(x=10, y=420, width=200)




                btn_frame=Frame(frame,bd=2,relief=RIDGE)
                btn_frame.place(x=70,y=450,width=130,height=37)

                #Register now
                btnReg=Button(btn_frame,text="Register now",command=self.register_data,width=13,font=('arial',11,'bold'),bg='green',fg='white')
                btnReg.grid(row=0,column=0,padx=1)
                
                #Login now
                # btnlogin=Button(btn_frame,text="Login now",width=15,font=('arial',11,'bold'),bg='white',fg='green')
                # btnlogin.grid(row=0,column=1,padx=1)



# Function Declaration
        def register_data(self):
                if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                        messagebox.showerror("Error","All fields are required")
                elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("Error","password and confirm password must be same")
                elif self.var_check.get()==0:
                        messagebox.showerror("Error","Please agree our terms and conditions")
                else: 
                        conn=mysql.connector.connect(host="localhost",username='root',password='dani@2274',port=3307,database='hmanagement')
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s")
                        value=(self.var_email.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","User already exist, please try another email")
                        else:
                                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_securityQ.get(),
                                    self.var_SecurityA.get(),
                                    self.var_pass.get()
                                    ))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Registered successfully!")



class HotelManagementSystem:
        def __init__(self, root):
                self.root=root
                self.root.title('Hotel Management System')
                self.root.geometry('1550x800+0+0')


                
                self.bg=ImageTk.PhotoImage(file=r"D:\Hotel Management System-YT\images\hotel1.jpg")
                lbl_bg=Label(self.root,image=self.bg)
                lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        # 1st image
                # img1=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img1=img1.resize(1550,140),Image.ANTIALIAS
                # self.photoimg1=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg1,bd=4,relief=RIDGE)
                # lblimg.place(x=0,y=0,width=1550,height=140)

        # logo
                # img2=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img2=img1.resize(230,140),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img1)


                # lblimg=Label(self.root, image=self.photoimg1,bd=4,relief=RIDGE)
                # lblimg.place(x=0,y=0,width=230,height=140)


        # title

                lbl_title=Label(self.root, text="Green Palace Hotel Larkana", font=('times new roman', 40,'bold'),bg='Green',fg='white', bd=4,relief=RIDGE)
                # lbl_title.place(x=0,y=140,width=1550,height=50)
                lbl_title.place(x=0,y=0,width=1550,height=60)

        # main frame
                main_frame=Frame(self.root,bd=4, relief=RIDGE)
                # main_frame.place(x=0,y=190,width=1550,height=620)
                main_frame.place(x=0,y=130,width=1550,height=620)
        # menu

                lbl_menu=Label(main_frame, text="MENU", font=('times new roman', 20,'bold'),bg='white',fg='green', bd=4,relief=RIDGE)
                lbl_menu.place(x=0,y=0,width=230)
        # btn frame

                btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
                btn_frame.place(x=0,y=35,width=228,height=190)

                cust_btn=Button(btn_frame,text='CUSTOMER',command=self.cust_details ,width=22,font=('times new roman', 14,'bold'),bg='green',fg='white', bd=4,relief=RIDGE,cursor='hand1')
                cust_btn.grid(row=0,column=0,pady=1)

                room_btn=Button(btn_frame,text='ROOM',command=self.roombooking,width=22,font=('times new roman', 14,'bold'),bg='green',fg='white', bd=4,relief=RIDGE,cursor='hand1')
                room_btn.grid(row=1,column=0,pady=1)

                details_btn=Button(btn_frame,text='DETAILS',command= self.DetailsRoom ,width=22,font=('times new roman', 14,'bold'),bg='green',fg='white', bd=4,relief=RIDGE,cursor='hand1')
                details_btn.grid(row=2,column=0,pady=1)

                # report_btn=Button(btn_frame,text='REPORT',width=22,font=('times new roman', 14,'bold'),bg='black',fg='gold', bd=4,relief=RIDGE,cursor='hand1')
                # report_btn.grid(row=3,column=0,pady=1)

                logout_btn=Button(btn_frame,text='LOGOUT',command=self.logout,width=22,font=('times new roman', 14,'bold'),bg='green',fg='white', bd=4,relief=RIDGE,cursor='hand1')
                logout_btn.grid(row=3,column=0,pady=1)


        # right side image

                img3=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                img3= img3.resize((1300, 570), Image.LANCZOS)
               
                self.photoimg2=ImageTk.PhotoImage(img3)

                lblimg1=Label(main_frame, image=self.photoimg2,bd=4,relief=RIDGE)
                lblimg1.place(x=225,y=0,width=1300,height=570)

                # down images

                # img4=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img4=img4.resize(230,210),Image.ANTIALIAS
                # self.photoimg4=ImageTk.PhotoImage(img4)

                # lblimg1=Label(main_frame, image=self.photoimg4,bd=4,relief=RIDGE)
                # lblimg1.place(x=225,y=225,width=230,height=210)

                # img5=Image.open(r"D:\Hotel Management System-YT\images\hotel1.jpg")
                # img5=img5.resize(230,190),Image.ANTIALIAS
                # self.photoimg2=ImageTk.PhotoImage(img5)

                # lblimg1=Label(main_frame, image=self.photoimg1,bd=4,relief=RIDGE)
                # lblimg1.place(x=0,y=420,width=230,height=190)



        def cust_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Cust_Win(self.new_window)

        def roombooking (self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooking(self.new_window)
        

        def DetailsRoom(self):
                self.new_window=Toplevel(self.root)
                self.app=DetailsRoom(self.new_window)
                

        def logout(self):
            self.root.destroy()











    






if __name__ == "__main__":
   main()