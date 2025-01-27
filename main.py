import csv

class Item:
    pay_rate = 10
    every = []
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.every.append(self) 
    
    def calculatePrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        return self.price * Item.pay_rate
    
    @classmethod #esto te permite crear y trabajar con instancias directamente en la clase sin necesidad de crear una clase exterior.
    def instantiate_from_csv(cls): 
        with open("items.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(item.get("name"), item.get("price"), item.get("quantity"))
    
    @staticmethod
    def is_integer(num):
       if isinstance(num, float):
           return num.is_integer()
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(10.0))