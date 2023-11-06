from pymongo import MongoClient
class UserModel:
    def __init__(self,userController) -> None:
        self.userController = userController
        self.dbConnection()
        
    def dbConnection(self):
        client= MongoClient("mongodb://localhost:27017")

        db= client["searchEngineDB"]

        self.collection = db ["userTable"]
        
        self.collection.create_index([('Identification', pymongo.ASCENDING), ('Username', pymongo.ASCENDING)], unique=True)

    def create(self, name,cnpjCpf,username,password,typeOfUser):
        userTable = {'Name':name,
                  'Identification': cnpjCpf,
                  'Username': username,
                  'Password': password,
                  'TypeOfUser':typeOfUser}
        self.collection.insert_one(userTable)
        try:
            self.collection.insert_one(userTable)
        except pymongo.errors.DuplicateKeyError as e:
            raise Exception("This Username or CPF or CNPJ does exist")
            
    def authentication(self, username,password,typeOfUser):
        user= userTable.find({ 
            'Username': username, 
            'Password': password,
            'TypeOfUser': typeOfUser
            })
        if not result:
            raise Exception("Usuário não encontrado")
        dataBaseUser = {
            "TypeOfUser": user[2],
            "name": user[0],
            "password": user[1],

        if dataBaseUser["password"] != password:
            raise Exception("Senha inválida")
        
        return {"uid": dataBaseUser["uid"]}
        }