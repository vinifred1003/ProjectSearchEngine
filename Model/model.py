from pymongo import MongoClient, ASCENDING
import pymongo
import json

class Model:
    def __init__(self, userController, productController) -> None:
        self.userController = userController
        self.productController= productController
        self.dbConnection()
        
    def dbConnection(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client["searchEngineDB"]
        self.userCollection = db["userTable"]
        self.productCollection= db["ProductsTable"]
        
        # Correção: Importe ASCENDING de pymongo
        self.userCollection.create_index([('Identification', ASCENDING), ('Username', ASCENDING)], unique=True)

    def create(self, name, cnpjCpf, username, password, typeOfUser):
        userTable = {
            'Name': name,
            'Identification': cnpjCpf,
            'Username': username,
            'Password': password,
            'TypeOfUser': typeOfUser
        }
        try:
            self.userCollection.insert_one(userTable)
        except pymongo.errors.DuplicateKeyError as e:
            raise Exception("This Username or CPF or CNPJ already exists")

    def authentication(self, username, password, typeOfUser):
        try:
            user = self.userCollection.find_one({
                'Username': username,  # Correção: 'username' para 'Username'
                'Password': password,
                'TypeOfUser': typeOfUser  # Correção: 'user_type' para 'TypeOfUser'
            })

            if user:
                print("Usuário autenticado com sucesso")
                return True
            else:
                print("Autenticação negada, senha ou usuário incorretos")
                return False
        except Exception as e:
            print(f"Erro na autenticação: {str(e)}")
            return False
    
    def readData(self, username):
        cursor = self.productCollection.find({'Username': username})
        self.all_results = []
        for document in cursor:
            self.all_results.append(dict(document))

        
