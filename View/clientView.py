import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from Controller.productController import ProductController


class ClientView():

  def __init__(self):
    self.root= tk.Tk()
    self.custom_font = font.Font(family="Oswald", size=26, weight="bold")
    self.run()
    self.header()
    self.productController = ProductController(None)
    self.products()
    self.root.mainloop()
    

  def run(self):
    self.root.title("Search")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)
    self.root.configure(background="light gray")

  def header(self):

    self.frame_header = Frame(self.root, bd=4, bg="light gray")
    self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.3)

    self.bar_label = Label(self.frame_header, font=self.custom_font, text="Search Bar", bg="black", fg="white")
    self.bar_label.place(relx=0.20, rely=0.65,relwidth=0.1,relheight=0.1)

    self.search_bar = Entry(self.frame_header, bd=2, bg="white")
    self.search_bar.place(relx=0.2, rely=0.85,relwidth=0.4)

    self.search_button = Button(self.frame_header, bd=2, text="Search", command= self.update_list)
    self.search_button.place(relx=0.733, rely=0.85, relwidth=0.07, relheight=0.12)

  def update_list(self):
    name_searched = self.search_bar.get()
    self.product_list.delete(*self.product_list.get_children())
    product_data = self.productController.search(name_searched)
    for i in product_data:
      self.product_list.insert('', tk.END, values=i) 

  def products(self):
    self.frame_products = Frame(self.root, bd=4, bg='white',highlightthickness=3 ,highlightbackground='black')
    self.frame_products.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.6)

    self.product_list = ttk.Treeview(self.frame_products, height=4, column=("col1, col2, col3, col4, col5, col6"))
    self.product_list.heading("#0", text="")
    self.product_list.heading("#1", text="Code")
    self.product_list.heading("#2", text="Name")
    self.product_list.heading("#3", text="Brand")
    self.product_list.heading("#4", text="Stock")
    self.product_list.heading("#5", text="Price")
    self.product_list.heading("#6", text="Company")

    self.product_list.column("#0", width=1)
    self.product_list.column("#1", width=50)
    self.product_list.column("#2", width=200)
    self.product_list.column("#3", width=125)
    self.product_list.column("#4", width=125)
    self.product_list.column("#5", width=100)
    self.product_list.column("#6", width=100)

    self.product_list.place(relx=0, rely=0, relwidth=1, relheight=1)
      
    self.scrollproduct_list = Scrollbar(self.frame_products, orient_='vertical')
    self.product_list.configure(yscroll=self.scrollproduct_list.set)
    self.scrollproduct_list.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)