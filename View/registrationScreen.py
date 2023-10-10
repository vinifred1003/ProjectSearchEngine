from tkinter import *
def donothing():
    pass

class RegistrationScreen(Toplevel):
    def __init__(self, visibleWindow):
        super().__init__(visibleWindow)
        self.visibleWindow = visibleWindow
        self.run()
        self.labels()


    def run(self):
        self.title("Signup User")
        self.geometry("500x600")
        self.configure(background="grey")
        self.resizable(True, True)
        
    def labels(self):
        self.var=0
        self.lbName = Label(self, text="Nome", fg="white", bg="gray")
        self.lbName.place(relx=0.1, rely=0.15)

        self.entryName = Entry(self, bd=2, bg="white")
        self.entryName.place(relx=0.1, rely=0.25)

        self.lbCnpjCpf = Label(self, text="CPF or CNPJ", fg="white", bg="gray")
        self.lbCnpjCpf.place(relx=0.1, rely=0.35)

        self.entryCnpjCpf = Entry(self, bd=2, bg="white")
        self.entryCnpjCpf.place(relx=0.1, rely=0.45)

        self.lbUsername = Label(self, text="Username", fg="white", bg="gray")
        self.lbUsername.place(relx=0.6, rely=0.15)

        self.entryUsername = Entry(self, bd=2, bg="white")
        self.entryUsername.place(relx=0.6, rely=0.25)

        self.lbPassword = Label(self, text="Password", fg="white", bg="gray")
        self.lbPassword.place(relx=0.6, rely=0.35)

        self.entryPassword = Entry(self, bd=2, bg="white")
        self.entryPassword.place(relx=0.6, rely=0.45)

        self.lbCompany = Label(self, text="Company?", fg="white", bg="gray")
        self.lbCompany.place(relx=0.2, rely=0.60)

        self.entryCompany = Radiobutton(self, variable=self.var,value=1 )
        self.entryCompany.place (relx=0.15, rely=0.65)