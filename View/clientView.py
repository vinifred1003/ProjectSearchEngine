import tkinter as tk
from tkinter import *

class ClientView():

  def __init__(self):
    self.root= tk.Tk()
    self.run()

    self.root.mainloop()
  
  def run(self):
    self.root.title("Search")
    self.root.attributes('-fullscreen', True)
    self.root.resizable(True, True)
    self.root.configure(background="#7092BE")