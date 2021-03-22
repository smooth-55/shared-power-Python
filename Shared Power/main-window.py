"""
Group-8 (Group Name = MARS)
Shared power

"""

from tkinter import *
from tkinter import ttk, filedialog, messagebox as mb
import tkinter as tk

import datetime

#from PIL import ImageTk
#import PIL.Image

from database import DatabaseManager, UserManager, Orders, ProductManager



class Login:

    def __init__(self, window):
        self.window = window
        self.frame = Frame(window)

        self.frame.pack()
        self.email_label = Label(self.window,
			         text="Email",
			         font = ("arial", 15, "bold")
        )
        self.email_label.place(x = 105, y = 100)
        self.email_entry = Entry(self.window,
			         textvariable = "email_verify",
			         bd=3
	)
        self.email_entry.place(x = 245, y =  100, width = 150, height = 25)
        self.password_label = Label(self.window,
			            text="Password",
			            font = ("arial", 15, "bold")
	)
        self.password_label.place(x = 105, y = 150)
        self.password_entry = Entry(self.window,
			            show = "*",
			            textvariable = "password_verify",
			            bd=3
	)
        self.password_entry.place(x = 245, y =  150, width = 150, height = 25)
        self.login_button = Button(self.window,
			           text = "Login",
			           font = ("arial", 10, "bold"),
			           width = 13,
			           fg = "red",
			           bg = "cyan",
			           relief ="groove",
			           cursor = "hand2",
			           activebackground ="red",
			           activeforeground = "cyan",
			           command = self.login_verify
	)
        self.login_button.place(x = 260, y = 195)
        self.no_account = Button(self.window,
			         text = "New User?, Click Here to Register.",
			         font = ("calibri", 11, "underline", "italic"),
			         relief = "flat",
			         cursor = "hand2",
			         command = self.register_window
	)
        self.no_account.place(x = 160, y = 260)
        self.window.resizable(False, False)

    def login_verify(self):
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()

        if self.email and self.password:
            user = UserManager()
            result = user.insert_login_info(self.email, self.password)

            if type(result) != type('str'):
                username = result[0]
                pwd = result[1]
                status = result[len(result)-1]

                mb.showinfo("Success",
                            "Login Successful")

                self.window.withdraw()
                self.app = Menu(self.window, status, self.email)

            else:
                mb.showerror("Login Failed",result)

        else:
            mb.showerror("Login Failed"
        		 , "Invalid Information"
            )

    def register_window(self):
        self.window.withdraw()
        Register(self.window)

class Register(Frame):

    def __init__(self, window):

        self.window = window
        self.reg = Toplevel()
        self.reg.title("Registration Form")
##        self.reg.iconbitmap('reg_icon.ico')
        self.reg.geometry("500x450+500+250")
        self.frame = tk.Frame(self.reg)
        self.reg_form = Label(self.reg,
                              text="Registration form",
                              width=20,
                              fg='#51931f',
                              font=("Times", 15),
                              borderwidth=3,
                              relief="sunken"
        )
        self.reg_form.place(x=130 , y=10 )
        self.reg_fullname = Label(self.reg,
        	                  text="Full Name",
        	                  width=20,
        	                  font=("bold", 13)
        )
        self.reg_fullname.place(x=50,y=70)
        self.fullname=StringVar()
        self.fullname_entry = Entry(self.reg,
        	                    bd =5,
        	                    textvariable=self.fullname,
        	                    width = 20
        )
        self.fullname_entry.place(x = 200, y = 70, width = 180)
        self.email_label = Label(self.reg,
        	                 text="Email",
        	                 width=20,
        	                 font=("bold", 13)
        )
        self.email_label.place(x=35,y=110)
        self.email_entry = Entry(self.reg,bd =5)
        self.email_entry.place(x=200,y=110,width=180)
        self.password_label = Label(self.reg,
        	                    text="Password",
        	                    width=20,
        	                    font=("bold", 13)
        )
        self.password_label.place(x=50, y=150)
        self.password_entry = Entry(self.reg, bd = 5, show="*")
        self.password_entry.place(x = 200, y = 150, width = 180)
        self.gender_label = Label(self.reg, text = "Gender", width = 20, font = ("bold", 13))
        self.gender_label.place(x = 40, y = 190)

        self.gender_value = StringVar()
        self.gender_value.set('')

        Rbtn1 = Radiobutton(self.reg,
        	            text="Male",
        	            font=("bold", 10),
        	            padx=5 ,
        	            variable=self.gender_value,
        	            value="M",
        )
        Rbtn1.place(x=200, y=190)
        Rbtn2 = Radiobutton(self.reg,
        	            text="Female",
        	            variable=self.gender_value,
        	            value="F",
        )
        Rbtn2.place(x=270, y=190)

        self.contact_label = Label(self.reg,
        	                   text="Contact No.",
        	                   width=20,
        	                   font=("bold", 13)
        )
        self.contact_label.place(x=55, y=250)
        self.contact_entry = Entry(self.reg, bd=5)
        self.contact_entry.place(x=200, y=250, width=180)
        self.address_label = Label(self.reg,
        	                   text="Address",
        	                   width=20,
        	                   font=("bold", 13)
        )
        self.address_label.place(x=45, y=290)
        self.address_entry = Entry(self.reg, bd=5)
        self.address_entry.place(x=200, y=290, width=180)
        self.registerButton=Button(self.reg,
        	                   text='Register',
                                   font=("bold", 10),
                                   width=15,
                                   bg='cyan',
                                   fg='red' ,
                                   cursor = 'hand2',
                                   command =self.save_info).place(x=200,y=350
                                   )
        self.reg.resizable(False, False)


    # @staticmethod
    # def selected_gender(event=None):
    #     self.gender_selected = self.gender_value.get()


    def save_info(self):
        self.name = self.fullname_entry.get()
        self.passw = self.password_entry.get()
        self.email = self.email_entry.get()
        self.gender_selected = self.gender_value.get()
        self.address = self.address_entry.get()
        self.contact = self.contact_entry.get()


        user = UserManager()
        result = user.insert_registered_info(self.email,
                                             self.passw,
                                             self.gender_selected,
                                             self.contact,
                                             self.address,
                                             'N'
        )
        self.reg.destroy()
        if not self.reg:
            self.window.deiconify()
        else:
            mb.showinfo("Success",
                        "Registration Successful")
            
        self.window.deiconify()

class Menu:
    def __init__(self, window, status, email):
       # self.window = window
        self.email = email
        self.window = window
        self.menu = Tk()
        self.menu.title("Homepage-SharedPower")
##        self.menu.iconbitmap('shared_ico.ico')
        self.menu.geometry("800x500+450+200")
        self.menu.resizable(False, False)

        self.content = None



        title = Label(self.menu,
                      text = "Welcome to Shared Power",
                      font=("Heventica", 35, "bold"),
                      bg = "gray",
                      fg = 'snow'
        )

        title.pack(side = TOP, fill = X)

	#Left frame

        self.menu_frame = Frame(self.menu,
                                bd=4,
                                relief = RIDGE,
                                bg = "gray"
        )
        self.menu_frame.place(x=5,y=65,width=225,height= 429)

	#Right Frame

        self.command_frame = Frame(self.menu,
                                   bd = 4,
                                   relief = RIDGE,
                                   bg = "gray"
        )
        self.command_frame.place(x= 232, y = 65, width = 562, height = 429)


	#menu buttons

        if status == 'N':
            self.create_normal()
        elif status == 'O':
            self.create_seller()
        elif status == 'I':
            self.create_insurance()
        elif status == 'D':
            self.create_delivery()

    def create_normal(self):

        self.search_tools = Button(self.menu_frame,
                                   text = "Search Tools",
                                   font=("Arial",10, "bold"),
                                   width = 15,
                                   bg = "#FE6645",
                                   fg = "snow",
                                   cursor="hand2",
                                   command = self.srch_bar,
                                   activebackground = "green",
                                   activeforeground ="snow"
        )
        self.search_tools.place(x = 40, y = 60)

        self.return_tools = Button(self.menu_frame,
                                   text = "Return Tools",
                                   font=("Arial", 10, "bold"),
                                   width = 15,
                                   bg = "#FE6645",
                                   fg = "snow",
                                   cursor="hand2",
                                   activebackground = "green",
                                   activeforeground ="snow",
                                   command = self.rtrnTools_fn
        )

        self.return_tools.place(x = 40, y = 140)
        self.invoice_but = Button(self.menu_frame,
                                  text = " View Invoice",
                                  font=("Arial",10, "bold"),
                                  width = 15,
                                  bg = "#FE6645",
                                  fg = "snow",
                                  cursor="hand2",
                                  activebackground = "green",
                                  activeforeground ="snow",
                                  command = self.invoice_table_user
        )
        self.invoice_but.place(x = 40, y = 180)
        self.logout = Button(self.menu_frame,
                             text = "Log out",
                             font=("Arial",10, "bold"),
                             width = 15,
                             bg = "#FE6645",
                             fg = "snow",
                             cursor="hand2",
                             activebackground = "green",
                             activeforeground ="snow",
                             command = self.cancel_operation
        )
        self.logout.place(x = 40, y = 220)
        self.menu.mainloop()


    def create_seller(self):
        self.add_tools = Button(self.menu_frame,
                                text = "Add tools",
                                font=("Arial",10, "bold"),
                                width = 15,
                                bg = "#FE6645",
                                fg = "snow",
                                cursor="hand2",
                                command = self.Clicktools,
                                activebackground = "green",
                                activeforeground ="snow"
        )
        self.add_tools.place(x = 40, y = 100)

        self.claim_insurance = Button(self.menu_frame,
                                text = "Claim Insurance",
                                font=("Arial",10, "bold"),
                                width = 15,
                                bg = "#FE6645",
                                fg = "snow",
                                cursor="hand2",
                                command = self.claim_ins,
                                activebackground = "green",
                                activeforeground ="snow"
        )
        self.claim_insurance.place(x = 40, y = 150)

        self.invoice_but = Button(self.menu_frame,
        	text = " Generate Invoice",
        	font=("Arial",10, "bold"),
        	width = 15,
        	bg = "#FE6645",
        	fg = "snow",
        	cursor="hand2",
        	activebackground = "green",
        	activeforeground ="snow",
        	command = self.invoice_table_owner
        	)
        self.invoice_but.place(x = 40, y = 184)




        self.logout = Button(self.menu_frame,
                             text = "Log out",
                             font=("Arial",10, "bold"),
                             width = 15,
                             bg = "#FE6645",
                             fg = "snow",
                             cursor="hand2",
                             activebackground = "green",
                             activeforeground ="snow",
                             command = self.cancel_operation
        )
        self.logout.place(x = 40, y = 220)
        self.menu.mainloop()

    def create_insurance(self):
        self.view_damaged = Button(self.menu_frame,
                                text = "View Damaged tools",
                                font=("Arial",10, "bold"),
                                width = 15,
                                bg = "#FE6645",
                                fg = "snow",
                                cursor="hand2",
                                command = self.ins_handler,
                                activebackground = "green",
                                activeforeground ="snow"
        )
        self.view_damaged.place(x = 40, y = 100)
        self.logout = Button(self.menu_frame,
                             text = "Log out",
                             font=("Arial",10, "bold"),
                             width = 15,
                             bg = "#FE6645",
                             fg = "snow",
                             cursor="hand2",
                             activebackground = "green",
                             activeforeground ="snow",
                             command = self.cancel_operation
        )
        self.logout.place(x = 40, y = 220)
        self.menu.mainloop()

    def create_delivery(self):
        self.del_method = Button(self.menu_frame,
                                text = "View Delivery Service",
                                font=("Arial",10, "bold"),
                                width = 18,
                                bg = "#FE6645",
                                fg = "snow",
                                cursor="hand2",
                                command = self.select_delivery,
                                activebackground = "green",
                                activeforeground ="snow"
        )
        self.del_method.place(x = 40, y = 100)
        self.logout = Button(self.menu_frame,
                             text = "Log out",
                             font=("Arial",10, "bold"),
                             width = 15,
                             bg = "#FE6645",
                             fg = "snow",
                             cursor="hand2",
                             activebackground = "green",
                             activeforeground ="snow",
                             command = self.cancel_operation
        )
        self.logout.place(x = 40, y = 220)
        self.menu.mainloop()


    def forget_restore(self):
        self.command_frame.place_forget()
        self.command_frame = Frame(self.menu,
                               bd = 4,
                               relief = RIDGE,
                               bg = "gray"
        )
        self.command_frame.place(x= 232, y = 65, width = 562, height = 429)

    def select_delivery(self):

        self.forget_restore()

        self.sel_delivery = StringVar(self.command_frame)
        self.sel_delivery.set('Options')
        self.options = list()

        statement = 'SELECT user_email from Orders where dispatch_service is not null'
        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement)

        if result:
            resultset = cur.fetchall()
            for result in resultset:
                self.options.append(result)

        if self.options:
            self.search_bar_del = OptionMenu(self.command_frame,
                                             self.sel_delivery,
                                             *self.options
            )
            self.search_bar_del.place(x = 75, y = 25)
            self.search_btn_del = Button(self.command_frame,
                                     text = 'List',
                                     width = 10,
                                     font = ('arial', 10, 'bold'),
                                     cursor = "hand2",
                                     fg = "#51931f",
                                     activebackground = "green",
			             activeforeground = "snow",
                                     command = self.show_delivery_results
            )
            self.search_btn_del.place(x = 375, y = 26)
        else:
            mb.showerror("ERROR", "No dispatch services has been selected")
            self.sel_delivery.set('')
            self.search_bar_del = OptionMenu(self.command_frame,
                                         self.sel_delivery,
                                         ''
            )
            self.search_bar_del.place(x = 75, y = 25)
            self.search_btn_del = Button(self.command_frame,
                                     text = 'List',
                                     width = 10,
                                     font = ('arial', 10, 'bold'),
                                     cursor = "hand2",
                                     fg = "#51931f",
                                     activebackground = "green",
			             activeforeground = "snow",
                                     state = DISABLED
            )
            self.search_btn_del.place(x = 375, y = 26)

    def show_delivery_results(self):

        em_var = self.sel_delivery.get().split("',")[0].split("('")[1]
        statement = 'SELECT Email, Phone, Address from UserInfo where Email= ?'
        conn, cur = DatabaseManager().connect_database()

        result = cur.execute(statement, (em_var,))

        if result:
            resultset = cur.fetchone()
            if resultset:
                email_add = resultset[0]
                phone = resultset[1]
                address = resultset[2]

                self.label_email = Label(self.command_frame,
                                     text="Name :",
                                     width=20,
                                     bg = 'grey',
                                     font=("bold",13),
                                     borderwidth=3
                )
                self.label_email.place(x=80,y=100)

                self.label_email_data = Label(self.command_frame,
                                              text=email_add,
                                              width=20,
                                              bg = 'White',
                                              font=("bold",13),
                                              borderwidth=3
                )
                self.label_email_data.place(x = 240, y=100)

                self.label_phone = Label(self.command_frame,
                                     text="Phone :",
                                     width=20,
                                     bg = 'grey',
                                     font=("bold",13),
                                     borderwidth=3
                )
                self.label_phone.place(x=80,y=140)

                self.label_phone_data = Label(self.command_frame,
                                              text=phone,
                                              width=20,
                                              bg = 'White',
                                              font=("bold",13),
                                              borderwidth=3
                )
                self.label_phone_data.place(x = 240, y=140)

                self.label_address = Label(self.command_frame,
                                     text="Address :",
                                     width=20,
                                     bg = 'grey',
                                     font=("bold",13),
                                     borderwidth=3
                )
                self.label_address.place(x=80,y=180)

                self.label_address_data = Label(self.command_frame,
                                              text=address,
                                              width=20,
                                              bg = 'White',
                                              font=("bold",13),
                                              borderwidth=3
                )
                self.label_address_data.place(x = 240, y=180)



###################################################################################################

    def Clicktools(self):


        self.forget_restore()

        self.label = Label(self.command_frame,
                text="Enter tool's description to Add ",
                width=44,
                fg="#51931f",
                font=("Arial",15, 'bold'),
                borderwidth =3 ,
                )
        self.label.place(x = 9, y = 7)

        self.label_1 = Label(self.command_frame,
                text="Tool's name:",
                width=20,
                bg = 'gray',
                font=("bold",13),
                borderwidth=3
                )
        self.label_1.place(x=35,y=70)

        self.Toolname= StringVar()

        self.entry_Toolname = Entry(self.command_frame,
                text="Toolname",
                width=25,
                font=("bold",13),
                borderwidth=3,
                justify = CENTER
                )
    

        self.entry_Toolname.place(x=200,y=72)

        self.label_2 = Label(self.command_frame,
                text="Tool's description:",
                width=20,
                bg = 'gray',
                font=("bold",13),
                borderwidth=3
                )
        self.label_2.place(x=35,y=110)

        self.Tooldescription= StringVar()

        self.entry_Tooldescription = Entry(self.command_frame,
                text="Tool description",
                width=25,
                font=("bold",13),
                borderwidth=3,
                justify = CENTER
                )
        self.entry_Tooldescription.place(x=200,y=110)

        self.label_3 = Label(self.command_frame,
                text="Half day rate:",
                bg = 'gray',
                width=20,
                font=("bold",13),
                borderwidth=3
                )
        self.label_3.place(x=35,y=150)

        self.Halfdayrate= StringVar()

        self.entry_Halfdayrate = Entry(self.command_frame,
                text="Half day rate",
                width=25,
                font=("bold",13),
                borderwidth=3,
                justify = CENTER
                )
        self.entry_Halfdayrate.place(x=200,y=154)

        self.label_4 = Label(self.command_frame,
                text="Full day rate:",
                width=20,
                bg = 'gray',
                font=("bold",13),
                borderwidth=3
                )
        self.label_4.place(x=35,y=190)

        self.Fulldayrate= StringVar()

        self.entry_Fulldayrate = Entry(self.command_frame,
                text="Full day rate",
                width=25,
                font=("bold",13),
                borderwidth=3,
                justify = CENTER
                )
        self.entry_Fulldayrate.place(x=200,y=192)


        self.label_5 = Label(self.command_frame,
                text="Tool's condition:",
                width=20,
                bg = 'gray',
                font=("bold",13),
                borderwidth=3
                )

        self.label_5.place(x=35,y=230)

        self.Toolcondition= StringVar()

        self.entry_Toolcondition = Entry(self.command_frame,
                text="Tool condition",
                width=25,
                font=("bold",13),
                borderwidth=3,
                justify = CENTER
                )
        self.entry_Toolcondition.place(x = 200, y = 232)





        self.upload_img_btn = Button(self.command_frame,
                                     cursor = "hand2",
                                     bg = "gray",
                                     activebackground = "gray",
                                     activeforeground = "snow",
                                     text = "Upload Image",
                                     border = 1,
                                     command = self.browse_img
                                     )

        self.upload_img_btn.place(x = 70 , y = 295)



        self.add_tools_btn = Button(self.command_frame,
                text = "Add Tool",
                font = ('Arial',10,'bold'),
                cursor = "hand2",
                fg = "#51931f",
                activebackground = "green",
                activeforeground = "snow",
                command = lambda:self.save_tools(self.email),
                border = 1,
                width = 10
                )

        self.add_tools_btn.place(x=270, y=310)

        self.cancel_btn = Button(self.command_frame,
                text = "Cancel",
                font = ('arial', 10, 'bold'),
                cursor = "hand2",
                fg = "#51931f",
                activebackground = "green",
                activeforeground = "snow",
                width = 10,
                command = self.cancel
                )

        self.cancel_btn.place(x = 410, y = 310)
        

        

        #For browsing image
    def browse_img(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                                   title = "select a file",
                                                   filetype = (("All file", "*.*"),)
                                                   )

        self.show_img = Label(self.command_frame,
                              height = 1,
                              width = 30,
                              bg = 'white',
                              font=("bold",7),
                              borderwidth=1,
                              text=self.filename
                              )

        self.show_img.place(x=55,y=334)
        self.send_img(self.filename)

    def send_img(self, filename):
        with open(filename, 'rb') as fn:
            content = fn.read()

        self.content = content


    def save_tools(self, username):
        self.tool_name = self.entry_Toolname.get()
        self.tool_desc = self.entry_Tooldescription.get()
        self.half_day_rate = self.entry_Halfdayrate.get()
        self.full_day_rate = self.entry_Fulldayrate.get()
        self.tool_cond = self.entry_Toolcondition.get()

        tools = ProductManager()
        result = tools.add_tool(self.tool_name,
                                username,
                                self.tool_desc,
                                self.half_day_rate,
                                self.full_day_rate,
                                self.tool_cond,
                                self.content
                                )
        mb.showinfo("Success",
                    "Tool Successfully Added")
        

    def cancel(self):
        self.entry_Toolname.delete(0, END)
        self.entry_Tooldescription.delete(0, END)
        self.entry_Halfdayrate.delete(0, END)
        self.entry_Fulldayrate.delete(0, END)
        self.entry_Toolcondition.delete(0, END)


    def rtrnTools_fn(self):

        self.forget_restore()
        self.retun_tool_lbl = Label(self.command_frame,
                text="Return Tool",
                width=44,
                fg="#51931f",
                font=("Arial",15, "bold"),
                borderwidth=3
                )
        self.retun_tool_lbl.place(x = 9, y = 7)

        self.label_Toolname = Label(self.command_frame,
                text="Tool name:",
                width=20,
                font=("bold",13),
                borderwidth=3,
                bg = 'gray'
                )
        self.label_Toolname.place(x=25,y=100)




        self.var = StringVar()
        self.tools = list()

        conn, cur = DatabaseManager().connect_database()
        #cur.execute('select tool_name from ProdInfo where user_email = ? and tool_taken=1;', (self.email,))
        cur.execute('select tool_name from Orders where user_email = ? and (date_returned is null or date_returned = "");', (self.email,))
        resultset = cur.fetchall()

        for result in resultset:
            self.tools.append(result[0])

        self.var.set("Choose")

        self.entry_to = OptionMenu(self.command_frame,
                                         self.var,
                                         *self.tools)

        self.entry_to.place(x=190,y=100, width = 180 )


        self.return_btn= Button(self.command_frame,
                text="Return",
                width=10,
                font=('Arial', 12, 'bold'),
                cursor="hand2",
                fg="#51931f",
                activebackground="green",
                activeforeground = "snow",
                command=self.update_return
                )
        self.return_btn.place(x=235, y=200)

        self.cancel_btn= Button(self.command_frame,
                text="Cancel",
                width=10,
                font=('Arial', 12, 'bold'),
                cursor="hand2",
                fg="#51931f",
                activebackground="green",
                activeforeground = "snow",
                command=self.cancel
                )
        self.cancel_btn.place(x=235, y=250)


    def update_return(self):

        statement = 'SELECT date_hired, half_day_price, full_day_price \
                    FROM Orders where user_email = ? and tool_name= ?'

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, (self.email,self.var.get()))

        if result:
            resultset = result.fetchone()
            if resultset:
                date_hired = resultset[0]
                half_day = resultset[1]
                full_day = resultset[2]

                cur_date_form = datetime.datetime.now().strftime("%Y-%m-%d %M:%H:%S")

                statement_next = 'UPDATE Orders \
                SET date_returned = ?, fine = ? \
                WHERE user_email=? and tool_name=?;'

                date_hired_date, date_hired_time = date_hired.split(' ')
                date_hired_year,date_hired_month,date_hired_day = date_hired_date.split("-")
                date_hired_hour,date_hired_min,date_hired_sec = date_hired_time.split(":")

                new_hired_date = datetime.datetime(
                    int(date_hired_year),
                    int(date_hired_month),
                    int(date_hired_day),
                    int(date_hired_hour),
                    int(date_hired_min),
                    int(date_hired_sec)
                )

                fine = float()
                current_date = datetime.datetime.now()

                diff = current_date - new_hired_date

                if diff.days > 3:
                    fine += (diff.days - 3) * full_day
                    if diff.seconds:
                        fine += half_day

                result = cur.execute(statement_next, (cur_date_form, fine, self.email, self.var.get()))
                conn.commit()

                statement = 'UPDATE ProdInfo \
                    SET tool_taken = 0 \
                    WHERE tool_name=? and half_day_price = ? and full_day_price = ? '


                inner_result =cur.execute(
                        statement,
                        (self.var.get(), half_day, full_day)
                    )
                conn.commit()
                if inner_result:
                    mb.showinfo("Info", f'{self.var.get()} has been returned')

                else:
                    mb.showerror("Error", 'Sorry there was error in database transaction')
        else:
            mb.showerror("Error", 'Sorry there was error in database transaction')


    ###################################


    def ins_handler(self):

        self.forget_restore()

        self.sel_ins = StringVar(self.command_frame)
        self.sel_ins.set('Options')
        self.options_ins = list()

        statement = 'SELECT tool_name from ProdInfo where tool_taken=2'
        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement)

        if result:
            resultset = cur.fetchall()
            for result in resultset:
                self.options_ins.append(result)

        if self.options_ins:
            self.search_bar_ins = OptionMenu(self.command_frame,
                                             self.sel_ins,
                                             *self.options_ins
            )
            self.search_bar_ins.place(x = 75, y = 25)
            self.search_btn_ins = Button(self.command_frame,
                                     text = 'List',
                                     width = 10,
                                     font = ('arial', 10, 'bold'),
                                     cursor = "hand2",
                                     fg = "#51931f",
                                     activebackground = "green",
			             activeforeground = "snow",
                                     command = self.show_delivery_results_ins
            )
            self.search_btn_ins.place(x = 375, y = 26)
        else:
            mb.showerror("ERROR", "No dispatch services has been selected")
            self.sel_ins.set('')
            self.search_bar_ins = OptionMenu(self.command_frame,
                                         self.sel_delivery,
                                         ''
            )
            self.search_bar_ins.place(x = 75, y = 25)
            self.search_btn_ins = Button(self.command_frame,
                                     text = 'List',
                                     width = 10,
                                     font = ('arial', 10, 'bold'),
                                     cursor = "hand2",
                                     fg = "#51931f",
                                     activebackground = "green",
			             activeforeground = "snow",
                                     state = DISABLED
            )
            self.search_btn_ins.place(x = 375, y = 26)

    def show_delivery_results_ins(self):

        em_var_ins = self.sel_ins.get().split("',")[0].split("('")[1]

        if em_var_ins:
            mb.showinfo('Info', f"{em_var_ins} is taken for insurance claim")

        else:
            mb.showerror('Error', "Sorry, There is an error in database")
    def srch_bar(self):
        self.forget_restore()
        self.search_bar = Entry(self.command_frame,
                                width=30,
                                font=("bold",13),
                                borderwidth=3,
                                justify = CENTER
        )
        self.search_bar.place(x = 75, y = 25)
        self.search_btn = Button(self.command_frame,
                                 text = 'Search',
                                 width = 10,
                                 font = ('arial', 10, 'bold'),
                                 cursor = "hand2",
                                 fg = "#51931f",
                                 activebackground = "green",
			         activeforeground = "snow",
                                 command = self.show_results
        )
        self.search_btn.place(x = 375, y = 26)

    def showdata(self, event):

        dispatch = 0.0
        cur_date_form = datetime.datetime.now().strftime("%Y-%m-%d %M:%H:%S")
        data = event.widget.item(event.widget.selection())
        tool = data['values'][0]
        if tool:
            answer_prod = mb.askyesno("Hire Item",f"Do you want to hire {tool}?")
            if answer_prod:

                self.top.destroy()
                answer_dispatch = mb.askyesno("Hire Item","Do you want to use dispatch rider?")
                if answer_dispatch:
                    dispatch = 1.0
                else:
                    dispatch= 0.0
                conn, cur = DatabaseManager().connect_database()
                statement = 'INSERT INTO Orders \
                (date_hired, date_returned, owner_name, tool_name, user_email, \
                half_day_price, full_day_price, dispatch_service, fine, insurance) \
                VALUES \
                (?,?,?,?,?,?,?,?,?,?);'

                val = (cur_date_form,
                       'null',
                       data['values'][1],
                       data['values'][0],
                       self.email,
                       data['values'][3],
                       data['values'][4],
                       dispatch,
                       'null',
                       0.0
                )
                result = cur.execute(statement, val)
                if result:
                    conn.commit()
                    statement_prod = 'UPDATE ProdInfo \
                    SET tool_taken = 1 \
                    WHERE owner_name = ? and tool_name = ? and \
                    half_day_price = ? and full_day_price = ?'

                    val_prod = (data['values'][1], data['values'][0], data['values'][3], data['values'][4])

                    result_prod = cur.execute(statement_prod, val_prod)
                    if result_prod:
                        conn.commit()
                        message = '{} has been hired'.format(data['values'][0])
                        mb.showinfo('Success', message)

                    else:
                        mb.showerror('Error', "Sorry. There was an error in database transaction.")

        else:
            mb.showerror('Error',  "Sorry. There was an error in database transaction.")


    def show_results(self):

        keyword = self.search_bar.get()

        if not keyword:
            mb.showerror('Error', 'Please enter keyword to search text')

        else:

            full_str = keyword+'%'

            statement = 'SELECT * FROM ProdInfo \
            WHERE tool_name LIKE ? and tool_taken = 0;'

            conn, cur = DatabaseManager().connect_database()
            result = cur.execute(statement, (full_str,))


            if result:
                resultset = cur.fetchall()
                if resultset:
                    self.top = Toplevel()
                    tview = ttk.Treeview(self.top, columns=('Tool Name',
                                                       'Tool Owner',
                                                       'Tool Description',
                                                       'Half Day Price',
                                                       'Full Day Price',
                                                       'Tool Condition'))
                    tview.heading('#0', text='SN')
                    tview.column('#0', stretch=NO, width=5)
                    tview.heading('#1', text='Tool Name')
                    tview.column('#1', stretch=NO)
                    tview.heading('#2', text='Tool Owner')
                    tview.column('#2', stretch=NO)
                    tview.heading('#3', text='Tool Description')
                    tview.column('#3', stretch=NO)
                    tview.heading('#4', text='Half Day Price')
                    tview.column('#4', stretch=NO)
                    tview.heading('#5', text='Full Day Price')
                    tview.column('#5', stretch=NO)
                    tview.heading('#6', text='Tool Condition')
                    tview.column('#6', stretch=NO)
                    tview.bind("<Double-Button-1>", self.showdata)
                    tview.pack(fill=BOTH, expand=1)
                    treeview = tview


                    for data in resultset:
                        tview.insert('',
                                     'end',
                                     text='1',
                                     values=(data[1], data[2],data[3],data[4],data[5],data[6]))
                else:
                    mb.showerror('Error', 'Keyword did not match with the result')


    def claim_ins(self):

        self.forget_restore()
        self.retun_tool_claim_lbl = Label(self.command_frame,
                text="Claim Insurance",
                width=44,
                fg="#51931f",
                font=("Arial",15, "bold"),
                borderwidth=3
                )
        self.retun_tool_claim_lbl.place(x = 9, y = 7)

        self.label_Toolname_claim = Label(self.command_frame,
                text="Tool name:",
                width=20,
                font=("bold",13),
                borderwidth=3,
                bg = 'gray'
                )
        self.label_Toolname_claim.place(x=25,y=100)


        self.claim_btn_claim= Button(self.command_frame,
                text="Claim",
                width=10,
                font=('Arial', 12, 'bold'),
                cursor="hand2",
                fg="#51931f",
                activebackground="green",
                activeforeground = "snow",
                command=self.update_claim_return
                )
        self.claim_btn_claim.place(x=235, y=200)


        self.var_claim = StringVar(self.command_frame)
        self.tools_claim = list()

        conn, cur = DatabaseManager().connect_database()
        #cur.execute('select tool_name from ProdInfo where user_email = ? and tool_taken=1;', (self.email,))
        statement = 'Select DISTINCT Orders.tool_name \
        FROM Orders CROSS JOIN ProdInfo \
        ON ProdInfo.tool_taken = 0 \
        and Orders.insurance = 0.0 \
        and Orders.date_returned is not null \
        and Orders.tool_name = ProdInfo.tool_name \
        and Orders.owner_name = ?;'

        cur.execute(statement, (self.email,))

        resultset = cur.fetchall()
        self.var_claim.set("Choose")

        if len(resultset) > 0:
            for result in resultset:
                self.tools_claim.append(result[0])

                self.entry_to_claim = OptionMenu(self.command_frame,
                                           self.var_claim,
                                           *self.tools_claim)

                self.entry_to_claim.place(x=190,y=100, width = 180 )


        else:
            if len(self.tools_claim) == 0:
                # self.tools.append('NO DATA')
                self.var_claim.set('')
                self.entry_to = OptionMenu(self.command_frame,
                                           self.var_claim,
                                           '')

                self.entry_to.place(x=190,y=100, width = 180 )
                mb.showinfo("ERROR", "NO tools to be claimed")
                self.claim_btn_claim.config(state=DISABLED)


    def update_claim_return(self):
        statement = 'UPDATE ProdInfo \
        SET tool_taken = 2 \
        where owner_name = ? and tool_name= ?;'

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, (self.email,self.var_claim.get()))

        if result:
            conn.commit()
            mb.showinfo("Info", f'{self.var_claim.get()} has been claimed for insurance')
            self.claim_ins()

        else:
            mb.showerror("Error", 'Sorry there was error in database transaction')


    def rtrnTools_fn(self):

        self.forget_restore()
        self.retun_tool_lbl = Label(self.command_frame,
                text="Return Tool",
                width=44,
                fg="#51931f",
                font=("Arial",15, "bold"),
                borderwidth=3
                )
        self.retun_tool_lbl.place(x = 9, y = 7)

        self.label_Toolname = Label(self.command_frame,
                text="Tool name:",
                width=20,
                font=("bold",13),
                borderwidth=3,
                bg = 'gray'
                )
        self.label_Toolname.place(x=25,y=100)


        self.return_btn= Button(self.command_frame,
                text="Return",
                width=10,
                font=('Arial', 12, 'bold'),
                cursor="hand2",
                fg="#51931f",
                activebackground="green",
                activeforeground = "snow",
                command=self.update_return
                )
        self.return_btn.place(x=235, y=200)

        self.cancel_btn= Button(self.command_frame,
                text="Cancel",
                width=10,
                font=('Arial', 12, 'bold'),
                cursor="hand2",
                fg="#51931f",
                activebackground="green",
                activeforeground = "snow",
                # command=self.cancel
                )
        self.cancel_btn.place(x=235, y=250)

        self.var = StringVar(self.command_frame)
        self.tools = list()

        conn, cur = DatabaseManager().connect_database()
        #cur.execute('select tool_name from ProdInfo where user_email = ? and tool_taken=1;', (self.email,))
        statement = 'Select Orders.tool_name \
        FROM Orders CROSS JOIN ProdInfo \
        ON ProdInfo.tool_taken = 1 \
        and Orders.date_returned is null \
        and Orders.user_email = ?;'
        cur.execute(statement, (self.email,))

        resultset = cur.fetchall()
        self.var.set("Choose")

        if len(resultset) > 0:
            for result in resultset:
                self.tools.append(result[0])

                self.entry_to = OptionMenu(self.command_frame,
                                           self.var,
                                           *self.tools)

                self.entry_to.place(x=190,y=100, width = 180 )


        else:
            if len(self.tools) == 0:
                # self.tools.append('NO DATA')
                self.var.set('')
                self.entry_to = OptionMenu(self.command_frame,
                                           self.var,
                                           '')

                self.entry_to.place(x=190,y=100, width = 180 )
                mb.showinfo("ERROR", "NO tools to be returned")
                self.return_btn.config(state=DISABLED)
                self.cancel_btn.config(state=DISABLED)


    def update_return(self):

        statement = 'SELECT date_hired, half_day_price, full_day_price \
                    FROM Orders where user_email = ? and tool_name= ?'

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, (self.email,self.var.get()))

        if result:
            resultset = result.fetchone()
            if resultset:
                date_hired = resultset[0]
                half_day = resultset[1]
                full_day = resultset[2]

                cur_date_form = datetime.datetime.now().strftime("%Y-%m-%d %M:%H:%S")

                statement_next = 'UPDATE Orders \
                SET date_returned = ?, fine = ? \
                WHERE user_email=? and tool_name=?;'

                date_hired_date, date_hired_time = date_hired.split(' ')
                date_hired_year,date_hired_month,date_hired_day = date_hired_date.split("-")
                date_hired_hour,date_hired_min,date_hired_sec = date_hired_time.split(":")

                new_hired_date = datetime.datetime(
                    int(date_hired_year),
                    int(date_hired_month),
                    int(date_hired_day),
                    int(date_hired_hour),
                    int(date_hired_min),
                    int(date_hired_sec)
                )

                fine = float()
                current_date = datetime.datetime.now()

                diff = current_date - new_hired_date

                if diff.days > 3:
                    fine += (diff.days - 3) * full_day
                    if diff.seconds:
                        fine += half_day

                result = cur.execute(statement_next, (cur_date_form, fine, self.email, self.var.get()))
                conn.commit()

                statement = 'UPDATE ProdInfo \
                    SET tool_taken = 0 \
                    WHERE tool_name=? and half_day_price = ? and full_day_price = ? '


                inner_result =cur.execute(
                        statement,
                        (self.var.get(), half_day, full_day)
                    )
                conn.commit()
                if inner_result:
                    mb.showinfo("Info", f'{self.var.get()} has been returned')
                    self.rtrnTools_fn()

                else:
                    mb.showerror("Error", 'Sorry there was error in database transaction')
        else:
            mb.showerror("Error", 'Sorry there was error in database transaction')


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Invoice for Normal user:
    def invoice_table_user(self):
        self.forget_restore()
        self.tool_name = Label(self.command_frame,
                               text = "Tools name",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.tool_name.place(x =8 , y = 15)
        self.date_hired= Label(self.command_frame,
                               text = "Hired Date",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.date_hired.place(x=90 , y =  15)
        self.date_returned = Label(self.command_frame,
                                   text = "Returned Date",
                                   font = ('arial', 9, 'bold'),
                                   bg = 'gray'
                                   )
        self.date_returned.place(x= 165, y = 15)
        self.tool_price = Label(self.command_frame,
                                text = "Half/Full",
                                font = ('arial', 9, 'bold'),
                                bg = 'gray'
                                )
        self.tool_price.place(x=264,y =15 )
        self.dispatch_rider = Label(self.command_frame,
                                    text = "Dispatch Rider",
                                    font = ('arial', 9, 'bold'),
                                    bg = 'gray'
                                    )
        self.dispatch_rider.place(x= 315, y = 15)
        self.insurance = Label(self.command_frame,
                               text = "Insurance",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.insurance.place(x=410, y =15 )
        self.total_cost = Label(self.command_frame,
                                text = "Total cost",
                                font = ('arial', 9, 'bold'),
                                bg = 'gray'
                                )
        self.total_cost.place(x= 480, y = 15 )

        self.total = Label(self.command_frame,
                           text = "Grand Total:",
                           font = ('arial', 9, 'bold'),
                           bg = 'gray'
        )
        self.total.place(x= 385, y = 380)
        # statement = 'SELECT Orders.tool_name, \
        # Orders.date_hired, \
        # Orders.date_returned, \
        # Orders.half_day_price, \
        # Orders.full_day_price, \
        # Orders.dispatch_service \
        # FROM Orders, ProdInfo\
        # WHERE Orders.user_email = ? and (Orders.date_returned is not null or Orders.date_returned != "" or Orders.date_returned != "null") \
        # and ProdInfo.tool_taken=0;'

        statement = 'SELECT DISTINCT Orders.tool_name, \
        Orders.date_hired, \
        Orders.date_returned, \
        Orders.half_day_price, \
        Orders.full_day_price, \
        Orders.dispatch_service \
        FROM Orders JOIN ProdInfo \
        ON Orders.date_returned is not null \
        and Orders.user_email = ? '


        self.total_sum = 0
        yc = 40
        conn, cur = DatabaseManager.connect_database()
        result = cur.execute(statement, (self.email,))
        resultset = result.fetchall()
        if resultset:
            for data in resultset:
                if data[4] is None or data[4] == '' or data[4] == 'null':
                    continue
                tool_name = data[0].capitalize()
                hired = data[1]
                returned = data[2]
                half = float(data[3])
                full = float(data[len(data)-2])
                dispatch = data[5]
                insurance = 5

                hired_convert = self.convert_date(hired)
                returned_convert = self.convert_date(returned)

                print(hired_convert, returned_convert)

                fine = float()
                cost = float()

                diff = returned_convert - hired_convert
                if diff.days > 3:
                    cost += full * 3
                    fine += (diff.days - 3) * float(data[3])
                    if diff.seconds:
                        fine += float(data[4])
                        cost += half
                        cost += 5
                        self.total_sum += cost

                if datetime.datetime.now().day >= 30 or (hired_convert.month != returned_convert.month):
                    dta = str(half)+'/'+str(full)
                    if dispatch is not None:
                        dispatch = 'YES'
                    else:
                        dispatch = 'NO'
                    Label(self.command_frame,
                          text = tool_name,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=18,y=yc)
                    Label(self.command_frame,text = hired.split(' ')[0],
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=90,y=yc)
                    Label(self.command_frame,text = returned.split(' ')[0],
                          font = ('arial', 9, 'bold')
                          ,bg = 'white').place(x=170,y=yc)
                    Label(self.command_frame,text = dta,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=262,y=yc)
                    Label(self.command_frame,text = dispatch,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=330,y=yc)
                    Label(self.command_frame,text = insurance,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=432,y=yc)
                    Label(self.command_frame,text = cost,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=483,y=yc)
                    yc += 25
                    Label(self.command_frame,text = self.total_sum,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=483,y=380)

        else:
            mb.showerror("ERROR", "WE ONLY CALCULATE AT THE END OF THE MONTH")


            #self.command_frame.place(x= 232, y = 65, width = 562, height = 429)

    #Invoice for Normal user:
    def invoice_table_owner(self):
        self.forget_restore()
        self.tool_name = Label(self.command_frame,
                               text = "Tools name",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.tool_name.place(x =8 , y = 15)
        self.date_hired= Label(self.command_frame,
                               text = "Hired Date",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.date_hired.place(x=90 , y =  15)
        self.date_returned = Label(self.command_frame,
                                   text = "Returned Date",
                                   font = ('arial', 9, 'bold'),
                                   bg = 'gray'
                                   )
        self.date_returned.place(x= 165, y = 15)
        self.tool_price = Label(self.command_frame,
                                text = "Half/Full",
                                font = ('arial', 9, 'bold'),
                                bg = 'gray'
                                )
        self.tool_price.place(x=264,y =15 )
        self.dispatch_rider = Label(self.command_frame,
                                    text = "Dispatch Rider",
                                    font = ('arial', 9, 'bold'),
                                    bg = 'gray'
                                    )
        self.dispatch_rider.place(x= 315, y = 15)
        self.insurance = Label(self.command_frame,
                               text = "Insurance",
                               font = ('arial', 9, 'bold'),
                               bg = 'gray'
                               )
        self.insurance.place(x=410, y =15 )
        self.total_cost = Label(self.command_frame,
                                text = "Total cost",
                                font = ('arial', 9, 'bold'),
                                bg = 'gray'
                                )
        self.total_cost.place(x= 480, y = 15 )


        self.total = Label(self.command_frame,
                           text = "Grand Total:",
                           font = ('arial', 9, 'bold'),
                           bg = 'gray'
        )
        self.total.place(x= 385, y = 380)



        statement = 'SELECT tool_name, \
        date_hired, \
        date_returned, \
        half_day_price, \
        full_day_price, \
        dispatch_service \
        FROM Orders \
        WHERE owner_name = ? \
        and date_returned is not null;'


        self.total_sum_own = 0
        yc = 40
        conn, cur = DatabaseManager.connect_database()
        result = cur.execute(statement, (self.email,))
        resultset = result.fetchall()
        if resultset:
            for data in resultset:
                tool_name = data[0].capitalize()
                hired = data[1]
                returned = data[2]
                half = float(data[3])
                full = float(data[len(data)-2])
                dispatch = data[5]
                insurance = 5

                hired_convert = self.convert_date(hired)
                returned_convert = self.convert_date(returned)

                fine = float()
                cost = float()

                diff = returned_convert - hired_convert
                if diff.days > 3:
                    cost += full * 3
                    fine += (diff.days - 3) * float(data[3])
                    if diff.seconds:
                        fine += float(data[4])
                        cost += half
                        cost += 5
                        self.total_sum_own += cost

                if datetime.datetime.now().day >= 30 or (hired_convert.month != returned_convert.month):
                    dta = str(half)+'/'+str(full)
                    if dispatch is not None:
                        dispatch = 'YES'
                    else:
                        dispatch = 'NO'
                    Label(self.command_frame,
                          text = tool_name,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=18,y=yc)
                    Label(self.command_frame,text = hired.split(' ')[0],
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=90,y=yc)
                    Label(self.command_frame,text = returned.split(' ')[0],
                          font = ('arial', 9, 'bold')
                          ,bg = 'white').place(x=170,y=yc)
                    Label(self.command_frame,text = dta,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=262,y=yc)
                    Label(self.command_frame,text = dispatch,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=330,y=yc)
                    Label(self.command_frame,text = insurance,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=432,y=yc)
                    Label(self.command_frame,text = cost,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=483,y=yc)
                    yc += 25
                    Label(self.command_frame,text = self.total_sum_own,
                          font = ('arial', 9, 'bold'),
                          bg = 'white').place(x=483,y=380)

        else:
            mb.showerror("ERROR", "WE ONLY CALCULATE AT THE END OF THE MONTH")




    @staticmethod
    def convert_date(string):

        date_hired_date, date_hired_time = string.split(' ')
        date_hired_year,date_hired_month,date_hired_day = date_hired_date.split("-")
        date_hired_hour,date_hired_min,date_hired_sec = date_hired_time.split(":")

        new_date = datetime.datetime(
            int(date_hired_year),
            int(date_hired_month),
            int(date_hired_day),
            int(date_hired_hour),
            int(date_hired_min),
            int(date_hired_sec)
        )

        return new_date


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Invoice for seller


    def invoice_table_user_s(self):

        self.forget_restore()

        self.user_id = Label(self.command_frame,
                                text = "User Id",
                                font = ('arial',8 , 'bold'),
                                bg = 'gray'
                                 )
        self.user_id.place(x =4 , y = 15)

        self.tool_name_s = Label(self.command_frame,
                                 text = "Tools name",
                font = ('arial',8 , 'bold'),
                bg = 'gray'
                )
        self.tool_name_s.place(x =55 , y = 15)

        self.date_hired_s= Label(self.command_frame,
                text = "Hired Date",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.date_hired_s.place(x=130 , y =  15)

        self.date_returned_s = Label(self.command_frame,
                text = "Returned Date",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.date_returned_s.place(x= 195, y = 15)

        self.tool_price_s = Label(self.command_frame,
                text = "Price",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.tool_price_s.place(x=288,
                y =15 )

        self.dispatch_rider_s = Label(self.command_frame,
                text = "Dispatch Rider",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.dispatch_rider_s.place(x= 325, y = 15)

        self.insurance_s = Label(self.command_frame,
                text = "Insurance",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.insurance_s.place(x=410, y =15 )

        self.total_cost_s = Label(self.command_frame,
                text = "Total cost",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.total_cost_s.place(x= 480, y = 15 )

        self.total_s = Label(self.command_frame,
                text = "Grand Total:",
                font = ('arial', 8, 'bold'),
                bg = 'gray'
                )
        self.total_s.place(x= 385, y = 380)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        self.command_frame.place(x= 232, y = 65, width = 562, height = 429)


    def cancel_operation(self):

        self.menu.destroy()
        self.window.deiconify()



def main_screen():

    root = Tk()
    root.geometry("500x350+500+250")
    root.title("Shared Power-Login")
    up = Login(root)
##    root.iconbitmap('login.ico')
    root.resizable(False, False)
    root.mainloop()

main_screen()



#up = Menu()
