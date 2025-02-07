import csv

class Item:
    pay_rate = 10
    every = []
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.every.append(self) 
        
    @property
    def name(self):
        return self.__name
    
    def calculatePrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        return self.price * Item.pay_rate
    
    @classmethod
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    