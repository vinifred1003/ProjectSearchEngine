import tkinter as tk
from tkinter import ttk
from tkinter import *
from Controller.productController import ProductController
from .registerProductView import RegisterProductView

class CompanyView:

  def __init__(self, username):
    self.root= tk.Tk()
    self.username = username
    self.run()
    self.header()
    self.products()
    self.productController = ProductController(username)
    self.update_list()
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

    self.update_button = Button(self.frame_header, bd=2, text="Update", command=self.product_update)
    self.update_button.place(relx=0.20, rely=0.9, relwidth=0.07, relheight=0.12)
    
    self.create_button = Button(self.frame_header, bd=2, text="New Product", command=self.register_product)
    self.create_button.place(relx=0.70, rely=0.80, relwidth=0.1, relheight=0.15)

  def product_update(self):
    code_selected = self.code_entry.get()
    if code_selected:
      self.register_product(code_selected)
    else:    
      pass

  def register_product(self):  
    self.root2 = Toplevel()
    self.root2.withdraw() 
    RegisterProductView(self.root2, self.username, None)
   
  def update_list(self):
    self.product_list.delete(*self.product_list.get_children())
    product_data = self.productController.read_product_data()
    for i in product_data:
      self.product_list.insert('', tk.END, values=i)


  def products(self):
      self.frame_products = Frame(self.root, bd=4, bg='white',highlightthickness=3 ,highlightbackground='black')
      self.frame_products.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.6)

      self.product_list = ttk.Treeview(self.frame_products, height=4, column=("col1, col2, col3, col4, col5"))
      self.product_list.heading("#0", text="")
      self.product_list.heading("#1", text="Code")
      self.product_list.heading("#2", text="Name")
      self.product_list.heading("#3", text="Brand")
      self.product_list.heading("#4", text="Stock")
      self.product_list.heading("#5", text="Price")

      self.product_list.column("#0", width=1)
      self.product_list.column("#1", width=50)
      self.product_list.column("#2", width=200)
      self.product_list.column("#3", width=125)
      self.product_list.column("#4", width=125)
      self.product_list.column("#5", width=100)
      
      self.product_list.place(relx=0, rely=0, relwidth=1, relheight=1)
      
      self.scrollproduct_list = Scrollbar(self.frame_products, orient_='vertical')
      self.product_list.configure(yscroll=self.scrollproduct_list.set)
      self.scrollproduct_list.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)
