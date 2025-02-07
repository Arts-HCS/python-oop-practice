from item import Item

class Phone(Item): 
    def __init__(self, name, price, quantity, broken_phones=0):
        super().__init__(
            name, price, quantity 
        )
        assert broken_phones >= 0, "Debe ser mayor a 0"
        
        self.broken_phones = broken_phones