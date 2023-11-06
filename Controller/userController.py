from Model.userModel import UserModel

class UserController:

    def __init__(self, name, cnpjCpf, username,password,typeOfUser) -> None:
        self.name= name
        self.cnpjCpf= cnpjCpf
        self.username= username
        self.password= password
        self.typeOfUser= typeOfUser

        self.userModel = UserModel(self)


    def saveData(self):
        self.userModel.create(self.name, self.cnpjCpf, self.username, self.password,self.typeOfUser)


    def authentication(self,username, password, typeOfUser):
        try:
            userId = self.usersModel.authenticate(username, password,typeOfUser)
            
            return userId
        
        except Exception as e:
            raise e                 