from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

class login:
    def __init__(self, window):
        self.window = window
        self.window.title('Login')
        self.window.geometry('1024x612')
        self.window.state('zoomed')
        self.window.resizable(0,0)


        
        self.Username = StringVar()
        self.Password = StringVar()

        #Background Image
        self.frame_bg= Image.open('icons/shopping#6.jpg').resize((1625,1025))
        img = ImageTk.PhotoImage(self.frame_bg)

        #Label to hold the Image
        self.label_bg = Label(self.window, image=img)
        self.label_bg.image =img
        self.label_bg.pack(fill='both', expand='yes')

        #adding a frame
        self.frame = Frame(self.window, bg='#040405', width = 950, height =600).place(x=300, y=100)
        
        
        #adding Labels and Entry to the frame
        self.welcome_label = Label(self.frame, text='WELCOME',bg='#040405', fg='white', font=('Yu gothic ui', 36)).place(x=450,y=150)
        self.sign_label = Label(self.frame, text='Sign In',bg='#040405', fg='white', font=('Yu gothic ui',24)).place(x=940,y=300)
        self.user_label = Label(self.frame, text='Username',bg='#040405', fg='white', font=('Yu gothic ui',24)).place(x=830,y=390)
        self.pass_label = Label(self.frame, text='Password',bg='#040405', fg='white', font=('Yu gothic ui',24)).place(x=830,y=490)

        #Adding entry
        self.userEntry = Entry(self.frame, highlightthickness= 0, textvariable=self.Username, relief=FLAT, font=('Yu gothic ui', 14), fg='white', bg='#040405').place(x=835,y=455)
        self.passEntry =  Entry(self.frame , highlightthickness= 0, textvariable=self.Username, relief=FLAT, font=('Yu gothic ui', 14), fg='white', bg='#040405', show='•').place(x=835,y=555)

        #adding canvas
        self.user_entry_cvs = Canvas(self.frame,width= 300, height=2.0, bg='white', highlightthickness=0).place(x=830,y=485)
        self.user_entry_cvs = Canvas(self.frame,width= 300, height=2.0, bg='white', highlightthickness=0).place(x=830,y=585)
        
        #left placed Image
        self.frame_img= Image.open('icons/shopping2.png').resize((450,320))
        imgll = ImageTk.PhotoImage(self.frame_img)

        #Login button
        self.lg_btn = Button(self.frame,width= 30, text='Log in', bg='#1ea1d7', fg='white', font=('Yu gothic ui', 12), bd=0, activebackground='#f759d0', activeforeground='white',
        cursor='hand2',command=self.authenticate).place(x=840,y=605)

        #Forget password button
        self.fg_btn = Button(self.frame,width= 15, text='Forgot Password?', bg='#040405', fg='white', font=('Yu gothic ui', 10, 'bold underline'), bd=0, activebackground='#040405',
        activeforeground='white', cursor='hand2').place(x=990,y=645)


        #Label to hold the Image
        self.label_img = Label(self.frame, image=imgll, bg='#040405')
        self.label_img.image =imgll
        self.label_img.place(x=305, y=250)

        #icon Image
        self.icon_img= Image.open('icons/loginicon.png').resize((180, 180))
        iconimg = ImageTk.PhotoImage(self.icon_img)
        

        #Label to hold the Image
        self.label_icon_img = Label(self.frame, image=iconimg, bg='#040405')
        self.label_icon_img.image =iconimg
        self.label_icon_img.place(x=905, y=130)
        #Show and hide button Icon 
        self.frame_bg= Image.open('icons/eye_20.png')#.resize((300,60))
        self.imgbtn = ImageTk.PhotoImage(self.frame_bg)
        
        self.hidebtn = Button(self.frame, image=self.imgbtn, bg='#040405', activebackground="#101010", highlightthickness=0,  relief=FLAT, command=self.show)
        self.hidebtn.image =self.imgbtn
        self.hidebtn.place(x=1100, y=550)
        
        
        self.hideicon= Image.open('icons/hide_20.png')#.resize((300,60))
        self.imgbtn = ImageTk.PhotoImage(self.hideicon)
        

    def show(self):
        self.hidebtn = Button(self.frame, image=self.imgbtn, bg='#040405', activebackground="#101010", highlightthickness=0,  relief=FLAT, command=self.hide)
        self.hidebtn.image =self.imgbtn
        self.hidebtn.place(x=1100, y=550)

        self.passEntry.config(show='')
        
    def hide(self):
        self.hidebtn = Button(self.frame, image=self.imgbtn, bg='#040405', activebackground="#101010", highlightthickness=0,  relief=FLAT, command=self.show)
        self.hidebtn.image =imgbtn
        self.hidebtn.place(x=1100, y=550)

        self.passEntry(show='•')
        
    def authenticate(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sa#root@2022",
        database="store"
        )
        
        dbcursor = mydb.cursor()
        if self.Username.get() == "" or self.Password.get()=="":
            print("motherfucker...")
        else:
            sql = "SELECT * FROM Employee WHERE username = %s AND password = %s AND  Role = %s "
            user1 = Username.get()
            pass1 = Password.get()
            dbcursor.execute(sql, user1, pass1);

            if dbcursor.fetchone() is not None:
                print("Login")
                Username.set("")
                Password.set("")
        

        

def page():
    window = Tk()
    login(window)
    window.mainloop()


if __name__ == '__main__':
    page()
