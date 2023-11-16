from Model.model import Model


class ProductController:
  def __init__(self, username) -> None:
    self.username =username
    self.model = Model(self.username, self)
    
  def saveData(self, productData):
    self.model.productCreate(productData)

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