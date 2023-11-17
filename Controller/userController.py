from Model.model import Model


class UserController:

    def __init__(self, name, cnpjCpf, username,password,typeOfUser) -> None:
        self.name= name
        self.cnpjCpf= cnpjCpf
        self.username= username
        self.password= password
        self.typeOfUser= typeOfUser

        self.model = Model(self,username)
        

    def saveData(self):
        try:
            self.model.userCreate(self.name, self.cnpjCpf, self.username, self.password,self.typeOfUser)
        except Exception as e:
            raise e        

    def authentication(self, username, password, typeOfUser):
        
        auth_result = self.model.authentication(username, password, typeOfUser)
        
        if auth_result:
            # Autenticação bem-sucedida
            return True
        else:
            # Autenticação falhou
            return False