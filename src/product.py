class Product:
    def __init__(self, id:int, category:str, name:str, price:float, in_stock:bool) -> None:
        if type(id) != int:
            raise TypeError
        if id < 0:
            raise ValueError
        self._id = id
        self.set_category(category)
        self.set_name(name)
        self.set_price(price)
        self.set_in_stock(in_stock)

    def get_id(self):
        return self._id
    def get_category(self):
        return self._category
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def get_in_stock(self):
        return self._in_stock
    
    def set_category(self, category):
        if type(category) != str:
            raise TypeError
        if len(category) > 32 or len(category) < 1:
            raise ValueError
        self._category = category
    def set_name(self, name):
        if type(name) != str:
            raise TypeError
        if len(name) > 32 or len(name) < 1:
            raise ValueError
        self._name = name
    def set_price(self, price):
        if type(price) != float:
            raise TypeError
        if price > 99999.99 or price <= 0:
            raise ValueError
        self._price = price
    def set_in_stock(self, in_stock):
        if type(in_stock) != bool:
            raise TypeError
        self._in_stock = in_stock