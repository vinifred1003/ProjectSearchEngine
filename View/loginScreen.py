import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from .registrationScreen import RegistrationScreen
import os
from Controller.userController import UserController
from .clientView import ClientView
from .companyView import CompanyView


class LoginScreen():
  
  def __init__(self):
    self.root = tk.Tk()
    self.custom_font = font.Font(family="Oswald", size=26, weight="bold")
    self.run()
    self.loginSpace()
    

    self.root.bind('<Escape>', self.close)
    self.root.mainloop()

  def run(self):
    AppFolder=os.path.dirname(__file__)
    bg = PhotoImage(file=AppFolder+"\\WhiteBackground.png")
    background_label = Label(self.root, image=bg)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = bg  
    self.root.title("Login")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)

  def on_enter(self, event):
    self.entry_username.delete(0,'end')

  def on_leave(self, event):
    self.name=self.entry_username.get()
    if self.name == '':
      self.entry_username.insert(0,'Username')

  def loginSpace(self):
    self.FrameLogin = Frame(self.root, bd=4, bg="#a0a0a0",highlightbackground="black", highlightthickness=5)
    self.FrameLogin.place(relx=0.35, rely=0.10, relwidth=0.30, relheight=0.80) 
           
    label_username = Label(self.FrameLogin, text="Username", font=self.custom_font, bg="#a0a0a0", fg="white", )
    label_username.place(relx=0.25, rely=0.10, relwidth=0.5, relheight=0.05)
    
    self.entry_username = Entry(self.FrameLogin, text="Amz")
    self.entry_username.place(relx=0.30, rely=0.20, relwidth=0.4, relheight=0.05)
    
    self.entry_username.insert(0,'Amz')
    self.entry_username.bind('<FocusIn>', lambda event: self.on_enter(event))
    self.entry_username.bind('<FocusOut>', lambda event: self.on_leave(event))

    label_password = Label(self.FrameLogin, text="Password", font=self.custom_font, bg="#a0a0a0", fg="white")
    label_password.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.05)
    
    self.entry_password = Entry(self.FrameLogin, show="*", text="01234567")   
    self.entry_password.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)
    self.entry_password.insert(0,'01234567')
    self.typeOfUserList=["Company", "Client"]
    self.optionsList = StringVar()
        
    self.entryCompany = Radiobutton(self.FrameLogin, variable=self.optionsList,value=self.typeOfUserList[0], text="Company" )
    self.entryCompany.place (relx=0.275, rely=0.50)
        
    self.entryClient = Radiobutton(self.FrameLogin, variable=self.optionsList,value=self.typeOfUserList[1], text="Client" )
    self.entryClient.place (relx=0.575, rely=0.50)    

    login_button = Button(self.FrameLogin, text="Sign in", command=self.callSignIn)
    login_button.place(relx=0.30, rely=0.60, relwidth=0.4, relheight=0.07)
    
    signup_button = Button(self.FrameLogin, text="Sign up", command=self.callSignUp)
    signup_button.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.04)
    
    exit_button = Button(self.FrameLogin, text="Exit", command=self.quit)
    exit_button.place(relx=0.35, rely=0.90, relwidth=0.3, relheight=0.04)
  
  def InvisibleWindow(self):
    self.root.withdraw()
  
  def quit(self):
    self.root.destroy()

  def destroyWindows(self):
    messagebox.showinfo("Sucess", "Successful Register")
    self.root.destroy()  

  def callSignUp(self):  
    self.root2 = Toplevel()
    self.root2.withdraw() 
    RegistrationScreen(self.root2)

  def callSignIn(self):
    username = self.entry_username.get()
    password = self.entry_password.get()
    typeOfUser = self.optionsList.get() 

    user_controller = UserController(None, None, username, password, typeOfUser)

    authenticated = user_controller.authentication(username, password, typeOfUser)

    if authenticated and typeOfUser=="Client":
      self.InvisibleWindow()
      ClientView()
    elif authenticated and typeOfUser=="Company":
      CompanyView(username)
      # self.destroyWindows()
    else:    
      messagebox.showerror("Error", "Incorrect username, password or user type")
  
  def close(self, evento=None):
    sys.exit()      