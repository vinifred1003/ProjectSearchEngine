from Model.model import Model


class ProductController:
  def __init__(self, username) -> None:
    self.username =username
    self.model = Model(self.username, self)
    
  def saveData(self, productData):
    try:
      self.model.productCreate(productData)
    except Exception as e:
      raise e    
  def delete(self,code, username):
    self.model.productDelete(code,self.username)   

  def read_product_data(self):  
    self.model.readData(self.username)
    results = self.model.all_results
    products_data = []
    for final_result in results:
      code = final_result.get('Code')
      name = final_result.get('Name')
      brand = final_result.get('Brand')
      stock = final_result.get('Stock')
      price = final_result.get('Price')
        
      products_data.append((f'{code}',f'{name}',f'{brand}',f'{stock}',f'{price}'))
      
    return products_data
  def read_one(self, username, code_selected):
    self.model.readOneData(self.username,code_selected)
    result= self.model.result_dict
    code = result.get('Code')
    name = result.get('Name')
    brand = result.get('Brand')
    stock = result.get('Stock')
    price = result.get('Price')
    final_result=(code, name, brand,stock,price)
    return final_result

  def update(self, productData):
    self.model.updateProduct(productData)

  def search(self,name_searched):
    self.model.readClientProduct(name_searched)
    results_product = self.model.product_results
    results_user = self.model.user_results
    final_result=[]
    products_data = []
    
    for dict1 in results_product:
        username1 = dict1.get("Username")
        for dict2 in results_user:
            username2 = dict2.get("Username")
            if username1 == username2:
                dict1["BusinessName"] = dict2.get("BusinessName", username2)
                final_result.append(dict1)
    
    for product_searched in final_result:
      code = product_searched.get('Code')
      name = product_searched.get('Name')
      brand = product_searched.get('Brand')
      stock = product_searched.get('Stock')
      price = product_searched.get('Price')
      company = product_searched.get('BusinessName')


      products_data.append((f'{code}',f'{name}',f'{brand}',f'{stock}',f'{price}',f'{company}'))
      
    return products_data