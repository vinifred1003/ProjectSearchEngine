import tkinter as tk
import sys
from tkinter import *
from tkinter import font
from .registrationScreen import RegistrationScreen


class LoginScreen():
  
  def __init__(self):
    self.root = tk.Tk()
    self.custom_font = font.Font(family="Oswald", size=26, weight="bold")
    self.run()
    self.loginSpace()
    

    self.root.bind('<Escape>', self.close)
    self.root.mainloop()
  
  def run(self):
    bg = PhotoImage(file="C:/Users/Aluno/Desktop/ProjectSearchEngine/View/WhiteBackground.png")
    background_label = Label(self.root, image=bg)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = bg  
    self.root.title("Login")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)

  def loginSpace(self):
    self.FrameLogin = Frame(self.root, bd=4, bg="#a0a0a0",highlightbackground="black", highlightthickness=5)
    self.FrameLogin.place(relx=0.35, rely=0.10, relwidth=0.30, relheight=0.80) 
            # Aqui você pode adicionar widgets de login dentro do FrameLogin
    label_username = Label(self.FrameLogin, text="Username", font=self.custom_font, bg="#a0a0a0", fg="white")
    label_username.place(relx=0.25, rely=0.10, relwidth=0.5, relheight=0.05)

    entry_username = Entry(self.FrameLogin)
    entry_username.place(relx=0.30, rely=0.20, relwidth=0.4, relheight=0.05)

    label_password = Label(self.FrameLogin, text="Password", font=self.custom_font, bg="#a0a0a0", fg="white")
    label_password.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.05)

    entry_password = Entry(self.FrameLogin, show="*")   
    entry_password.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)

    login_button = Button(self.FrameLogin, text="Login")
    login_button.place(relx=0.30, rely=0.53, relwidth=0.4, relheight=0.07)
    
    signup_button = Button(self.FrameLogin, text="Signup", command=self.callSignup)
    signup_button.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.03)
    
    exit_button = Button(self.FrameLogin, text="Exit", command=self.quit)
    exit_button.place(relx=0.35, rely=0.90, relwidth=0.3, relheight=0.03)

  def quit(self):
    self.root.destroy()

  def callSignup(self):  
    self.root2 = Toplevel()
    self.root2.withdraw() 
    RegistrationScreen(self.root2)
  
  def close(self, evento=None):
    sys.exit()
