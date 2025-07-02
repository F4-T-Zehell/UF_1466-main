



class InventoryManagement: # This is main class for all the program

 def __init__(self):
    """
    here we got empty def bout inventory:
    """
    self.inventory = {}

    
def add_product(self, _product, _quantity):
    """This is the main function what we gonna make all the inventory program"""
    if (int(_quantity)) and _quantity > 0:
       self.inventory[_product] = self.inventory(get(_product, 0)) + _quantity
    else:
        print(f"product: {self._product} quantity: {self._quantity}")


def delete_product(self, product):
    """This function it lets erase a product inner inventory"""
    if self.inventory.pop(product, None) is None:
        print("no found product to delete")


def consult_product(self, product):
    """function to see one product within the inventory"""
    return self.inventory(product, "This product is not in da inventory") 

def mod_quantity(self, product, new_quantity):
   """ Renew quantity product"""
   if product in self.inventory: (new_quantity, int) and new_quantity > 0:
    else:
        print("quantity should be an int number")
 else:
     print("this product doesn't exist in da inventory")
   
def view_inventory(self, sort=False):
   """displays all the quantitis and its inventory products"""
    
"""mandatory rollin"""
def main():
    shop = InventoryManagement()
    shop.add_product("Manzanas", 10)
    shop.add_product("Peras", 5)
    shop.add_product("Manzanas", 5)

    print("consult apples", shop.consult_product("apples"))

    print("inventory")
    shop.view_inventory()
    

    shop.delete_product("Pears")
    print("Inventory aft delete pears")
    print("inventory")
    shop.view_inventory()
    

if __name__ == "__main__":
    main()

