from Model.model import Model

class ProductController:
  def __init__(self, username) -> None:
    self.username =username

    self.model = Model(self.username, self)
    
  def saveData(self):
    self.model.productCreate(product_data)

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
