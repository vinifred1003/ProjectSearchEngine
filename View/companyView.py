import tkinter as tk
from tkinter import ttk
from tkinter import *

class CompanyView():

  def __init__(self, username):
    self.root= tk.Tk()
    self.username = username
    self.run()
    self.header()
    self.products()
    self.root.mainloop()
  
  def run(self):
    self.root.title("Company Products")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)
    self.root.configure(background="light gray", bd=4, highlightthickness=3 ,highlightbackground='black')

  def header(self):
    self.frame_header = Frame(self.root, bd=4, bg="light gray")
    self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.3)

    self.delete_button = Button(self.frame_header, bd=2, text="Delete")
    self.delete_button.place(relx=0.3, rely=0.9, relwidth=0.07, relheight=0.12)

    self.lb_code = Label(self.frame_header, text="Code", fg="white", bg="black")
    self.lb_code.place(relx=0.2, rely=0.50)

    self.code_entry = Entry(self.frame_header, bd=2, bg="white")
    self.code_entry.place(relx=0.2, rely=0.65)

    self.update_button = Button(self.frame_header, bd=2, text="Update")
    self.update_button.place(relx=0.20, rely=0.9, relwidth=0.07, relheight=0.12)
    
    self.create_button = Button(self.frame_header, bd=2, text="New Product")
    self.create_button.place(relx=0.70, rely=0.80, relwidth=0.1, relheight=0.15)
    

  def products(self):
      self.frame_products = Frame(self.root, bd=4, bg='white',highlightthickness=3 ,highlightbackground='black')
      self.frame_products.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.6)

      self.listR = ttk.Treeview(self.frame_products, height=4, column=("col1, col2, col3, col4, col5"))
      self.listR.heading("#0", text="")
      self.listR.heading("#1", text="Code")
      self.listR.heading("#2", text="Name")
      self.listR.heading("#3", text="Brand")
      self.listR.heading("#4", text="Stock")
      self.listR.heading("#5", text="Price")

      self.listR.column("#0", width=1)
      self.listR.column("#1", width=50)
      self.listR.column("#2", width=200)
      self.listR.column("#3", width=125)
      self.listR.column("#4", width=125)
      self.listR.column("#5", width=100)
      
      self.listR.place(relx=0, rely=0, relwidth=1, relheight=1)
      
      self.scrollListR = Scrollbar(self.frame_products, orient_='vertical')
      self.listR.configure(yscroll=self.scrollListR.set)
      self.scrollListR.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)
CompanyView()