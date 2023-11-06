from pymongo import MongoClient
class userModel:
    def __init__(self,userController) -> None:
        self.userController = userController
        self.dbConnection()
        
    def dbConnection(self):
        client= MongoClient("mongodb://localhost:27017")

        db= client["SearchEngineDB"]

        self.collection = db ["Users"]

    def create(self, name,cnpjCpf,username,password,company):
        userData:{'Name':'name',
                  'Identification': 'cnpjCpf',
                  'User name': 'username',
                  'Password': 'password',
                  'Company':'company'}
        self.collection.insert_one(userData)