class Item:
    pay_rate = 10
    def __init__(self, name, price, quantity):
        
        assert price >= 0, f"Price {price} is less than zero."
        assert quantity >= 4
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculatePrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        return self.price * self.pay_rate


item1 = Item("Phone",91,30)


item2 = Item("Laptop",150,13)

print(item1.applyDiscount())
