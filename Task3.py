class Product:
  def __init__(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price
class Inventory:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def remove_product(self, name):
    for product in self.products:
      if product.name == name:
        self.products.remove(product)
        print(f"Product '{name}' removed from inventory")
        return
    print(f"Product '{name}' not found in inventory")

  def update_quantity(self, name, quantity):
    for product in self.products:
      if product.name == name:
        product.quantity = quantity
        print(f"Quantity of '{name}' updated to {quantity}")
        return
    print(f"Product '{name}' not found in inventory")

  def display_products(self):
    print("Inventory:")
    for product in self.products:
      print(f"Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

  def search_product(self, name):
    for product in self.products:
      if product.name == name:
        return product
    return None

# Create an instance of the inventory
inventory = Inventory()

# Add some products
inventory.add_product(Product("Apple", 10, 1.00))
inventory.add_product(Product("Banana", 20, 0.50))
inventory.add_product(Product("Orange", 30, 1.50))

inventory.display_products()

inventory.update_quantity("Apple", 15)

inventory.remove_product("Banana")

product = inventory.search_product("Orange")
if product:
  print(f"Product found: {product.name}, {product.quantity}, {product.price}")
else:
  print("Product not found")

# Display products again
inventory.display_products()