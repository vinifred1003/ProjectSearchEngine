from Controller.productController import ProductController
from tkinter import *
from tkinter import messagebox
def donothing():
    pass

class RegisterProductView(Toplevel):
    def __init__(self, visibleWindow,username,code_selected,CompanyView):
        super().__init__(visibleWindow)
        self.visibleWindow = visibleWindow
        self.run()
        self.labels()
        self.username= username
        self.productController = ProductController(username)
        self.company_view = CompanyView
        self.code_selected = code_selected

        if code_selected:
            self.fill_entries(self.username, self.code_selected)

    def run(self):
        self.title("Product Registration")
        self.geometry("500x600")
        self.configure(background="grey")
        self.resizable(True, True)

    def fill_entries(self, username ,code_selected):
        data=self.productController.read_one(username ,code_selected)
        self.entryCode.delete(0,END)
        self.entryName.delete(0,END)
        self.entryBrand.delete(0,END)
        self.entryStock.delete(0,END)
        self.entryPrice.delete(0,END)
        
        self.entryCode.insert(0,data[0])
        self.entryName.insert(0,data[1])
        self.entryBrand.insert(0,data[2])
        self.entryStock.insert(0,data[3])
        self.entryPrice.insert(0,data[4])
        self.entryCode.config(state= "disabled")
    
    def labels(self):
        
        self.lbName = Label(self, text="Product Name", fg="white", bg="gray")
        self.lbName.place(relx=0.1, rely=0.15)

        self.entryName = Entry(self, bd=2, bg="white")
        self.entryName.place(relx=0.1, rely=0.25)

        self.lbCode = Label(self, text="Code", fg="white", bg="gray")
        self.lbCode.place(relx=0.1, rely=0.35)

        self.entryCode = Entry(self, bd=2, bg="white")
        self.entryCode.place(relx=0.1, rely=0.45)

        self.lbBrand = Label(self, text="Brand", fg="white", bg="gray")
        self.lbBrand.place(relx=0.6, rely=0.15)

        self.entryBrand = Entry(self, bd=2, bg="white")
        self.entryBrand.place(relx=0.6, rely=0.25)

        self.lbStock = Label(self, text="Stock", fg="white", bg="gray")
        self.lbStock.place(relx=0.6, rely=0.35)

        self.entryStock = Entry(self, bd=2, bg="white")
        self.entryStock.place(relx=0.6, rely=0.45)

        self.lbPrice = Label(self, text="Price", fg="white", bg="gray")
        self.lbPrice.place(relx=0.2, rely=0.55)

        self.entryPrice = Entry(self, bd=2, bg="white")
        self.entryPrice.place(relx=0.2, rely=0.65)        

        saveButton = Button(self, text="Save", command=self.saveData)
        saveButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.07)

    def saveData(self):
        code = self.entryCode.get()
        name = self.entryName.get()
        brand = self.entryBrand.get()
        stock = self.entryStock.get()
        price = self.entryPrice.get()
        productData = (self.username,code, name, brand,stock, price)
        PD = ProductController(self.username)
        if self.code_selected:
            PD.update(productData)
        else:
            try:
                PD.saveData(productData)
                self.destroyWindows()
                self.company_view.update_list()
            except Exception as e:
                messagebox.showerror("Error",f"Error: {e}")
                
        
        
    
    def destroyWindows(self):
        messagebox.showinfo("Sucess", "Successful Register")
        
        self.visibleWindow.destroy()
    