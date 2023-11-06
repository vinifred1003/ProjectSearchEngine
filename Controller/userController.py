    
class UserController:

    def __init__(self, name, cnpjCpf, username,password,company) -> None:
        self.name= name
        self.cnpjCpf= cnpjCpf
        self.username= username
        self.password= password
        self.company= company

    def salvar_dados(self):
        self.model.create(self.name, self.cnpjCpf, self.username, self.password,self.company)
