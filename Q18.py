# 18. Property Decorators: @property, @setter, and @deleter
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price 

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print ("Invalid Price. price must be greater than 0")
    
    @price.deleter
    def price(self):
        print("price deleting...")
        del self._price

p1 = Product(90)  
print(p1.price)

p1.price = 40      
print(p1.price)

p1.price = -30     
print(p1.price)

del p1.price