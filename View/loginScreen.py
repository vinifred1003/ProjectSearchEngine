import tkinter as tk
import sys
from tkinter import *


class LoginScreen():
  
  def __init__(self):
    self.root = tk.Tk()
    self.run()
    self.loginSpace()
    
    self.root.bind('<Escape>', self.close)
    self.root.mainloop()
  
  def run(self):
    bg = PhotoImage(file="C:/Users/Aluno/Downloads/Nova pasta/ProjectSearchEngine/View/WhiteBackground.png")
    background_label = Label(self.root, image=bg)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = bg  # Para evitar que a imagem seja destruída pela coleta de lixo
    self.root.title("Login")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)

  def loginSpace(self):
    self.FrameLogin = Frame(self.root, bd=4, bg="#a0a0a0",highlightbackground="black", highlightthickness=5)
    self.FrameLogin.place(relx=0.35, rely=0.10, relwidth=0.30, relheight=0.80) 
            # Aqui você pode adicionar widgets de login dentro do FrameLogin
    label_username = Label(self.FrameLogin, text="Username:")
    label_username.place(relx=0.35, rely=0.10, relwidth=0.3, relheight=0.05)

    entry_username = Entry(self.FrameLogin)
    entry_username.place(relx=0.30, rely=0.20, relwidth=0.4, relheight=0.05)

    label_password = Label(self.FrameLogin, text="Password:")
    label_password.place(relx=0.35, rely=0.40, relwidth=0.3, relheight=0.05)

    entry_password = Entry(self.FrameLogin, show="*")  # Para esconder a senha
    entry_password.place(relx=0.30, rely=0.50, relwidth=0.4, relheight=0.05)

    login_button = Button(self.FrameLogin, text="Login")
    login_button.place(relx=0.40, rely=0.70, relwidth=0.2, relheight=0.1)


  def close(self, evento=None):
    sys.exit()
