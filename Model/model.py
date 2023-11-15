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
        
        
        self.userCollection.create_index([('Identification', ASCENDING), ('Username', ASCENDING)], unique=True)
        self.productCollection.create_index([('Code', ASCENDING)], unique=True)

    def userCreate(self, name, cnpjCpf, username, password, typeOfUser):
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
    
    def productCreate(self, username, name, code, brand, stock, price):
        ProductsTable = {
            'Username': username,
            'Code': code,
            'Name': name,
            'Brand': brand,
            'Stock': stock,
            'Price': price
        }
        try:
            self.productCollection.insert_one(ProductsTable)
        except pymongo.errors.DuplicateKeyError as e:
            raise Exception("This Code already exists")        
    
    def updateProduct(self,username, code,name, brand, stock, price):
        code_key = {'Code': code}
        user_key = {'Username': username}
        combination_keys= {**code_key, **user_key}
        new_update = {'$set': {
            'Code': code,
            'Name': name,
            'Brand': brand,
            'Stock': stock,
            'Price': price}}
        self.collection.update_one(combination_keys, new_update)

    def readData(self, username):
        cursor = self.productCollection.find({'Username': username})
        self.all_results = []
        for document in cursor:
            self.all_results.append(dict(document))

        
