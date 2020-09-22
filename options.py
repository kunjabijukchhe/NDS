from tkinter import *
from tkinter import messagebox
import os
import sys


py = sys.executable


# creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('350x350')
        self.configure(bg="#20c997")
        self.title("Encryption")
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)


        def add_user():
            os.system('%s %s' % (py, 'addUser.py'))

        def rem_user():
            os.system('%s %s' % (py, 'removeUser.py'))

        def one():
            os.system('%s %s' % (py, 'caser.py'))

        def two():
            os.system('%s %s' % (py, 'mono.py'))

        def three():
            os.system('%s %s' % (py, 'rsa.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to quit?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'main.py'))

        list = Menu(self)
        list.add_command(label="Add User", command=add_user)
        list.add_command(label="Remove User", command=rem_user)

        self.mymenu.add_cascade(label='Admin Tools', menu=list)

        self.config(menu=self.mymenu)

        self.label = Label(self, text="Select Your Enctytion", bg='#17a2b8', fg='white', font=('Arial',20,'bold')).place(x=30, y=10)

        self.button = Button(self, text="Caser Cipher Encryption",bg='#495057',fg='#f9f9f9', command=one, width=10, height=2,
                             font=('Arial',15,'bold'))
        self.button.place(x=45, y=70, width=260)

        self.button1 = Button(self, text="Mono Alphabetic Cipher",bg='#495057',fg='#f9f9f9', command=two, width=10, height=2,
                              font=('Arial',15,'bold'))
        self.button1.place(x=45, y=140, width=260)

        self.button2 = Button(self, text="Rivest Shamir Adleman",bg='#495057',fg='#f9f9f9', command=three, width=10, height=2,
                              font=('Arial',15,'bold'))
        self.button2.place(x=45, y=210, width=260)

        self.button_quit = Button(self, text="Quit", bg='#dc3545',fg='white', command=log, width=10, height=2,
                                  font='Helvetica')
        self.button_quit.place(x=125, y=280)


MainWin().mainloop()
