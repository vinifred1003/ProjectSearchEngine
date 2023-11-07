import tkinter as tk
from tkinter import *

class CompanyView():

  def __init__(self):
    self.root= tk.Tk()
    self.run()

    self.root.mainloop()
  
  def run(self):
    self.root.title("Company Products")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)
    self.root.configure(background="red")

