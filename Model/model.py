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
    
    def productCreate(self, productData):
        ProductsTable = {
            'Username': productData[0],
            'Code': productData[1],
            'Name': productData[2],
            'Brand': productData[3],
            'Stock': productData[4],
            'Price': productData[5]
        }
        try:
            self.productCollection.insert_one(ProductsTable)
        except pymongo.errors.DuplicateKeyError as e:
            raise Exception("This Code already exists")        

    def updateProduct(self, productData):
        code_key = {'Code': productData[1]}
        user_key = {'Username': productData[0]}
        combination_keys= {**code_key, **user_key}
        new_update = {'$set': {
            'Name': productData[2],
            'Brand': productData[3],
            'Stock': productData[4],
            'Price': productData[5]}}
        self.productCollection.update_one(combination_keys, new_update)

    def readData(self, username):
        cursor = self.productCollection.find({'Username': username})
        self.all_results = []
        for document in cursor:
            self.all_results.append(dict(document))
    
    def readOneData(self, username, code):
        cursor = self.productCollection.find_one({'Username': username, 'Code':code})
        if cursor:
            self.result_dict=dict(cursor)
            return self.result_dict
        else:
            return None
    def productDelete(self,code,username):
        code_key = {'Code': code}
        user_key = {'Username': username}
        combination_keys= {**code_key, **user_key}
        
        self.productCollection.delete_one(combination_keys)