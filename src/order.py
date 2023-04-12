import datetime

class OrderItem:
    def __init__(self, id:int, prod_name:str, prod_price:float, amount:int) -> None:
        if type(id) != int:
            raise TypeError
        if id < 1:
            raise ValueError
        self._id = id
        self.set_prod_name(prod_name)
        self.set_prod_price(prod_price)
        self.set_amount(amount)

    def get_id(self):
        return self._id
    def get_prod_name(self):
        return self._prod_name
    def get_prod_price(self):
        return self._prod_price
    def get_amount(self):
        return self._amount

    def set_prod_name(self, name:str):
        if type(name) != str:
            raise TypeError
        if len(name) < 1 or len(name) > 32:
            raise ValueError
        self._prod_name = name
    def set_prod_price(self, price:float):
        if type(price) != float:
            raise TypeError
        if price <= 0 or price > 99999.99:
            raise ValueError
        self._prod_price = price
    def set_amount(self, amount:int):
        if type(amount) != int:
            raise TypeError
        if amount <= 0:
            raise ValueError
        self._amount = amount

class Order:
    def __init__(self, id:int, cust_fname:str, cust_lname:str, date:datetime.date, payment:str):
        if type(id) != int:
            raise TypeError
        if id < 1:
            raise ValueError
        self._id = id
        self.set_cust_fname(cust_fname)
        self.set_cust_lname(cust_lname)
        self.set_order_date(date)
        self.set_payment(payment)
        self._items = []

    def get_id(self):
        return self._id
    def get_cust_fname(self):
        return self._cust_fname
    def get_cust_lname(self):
        return self._cust_lname
    def get_order_date(self):
        return self._order_date
    def get_payment(self):
        return self._payment
    def get_items(self) -> list[OrderItem]:
        return self._items

    def set_cust_fname(self, fname:str):
        if type(fname) != str:
            raise TypeError
        if len(fname) < 1 or len(fname) > 32:
            raise ValueError
        self._cust_fname = fname
    def set_cust_lname(self, lname:str):
        if type(lname) != str:
            raise TypeError
        if len(lname) < 1 or len(lname) > 32:
            raise ValueError
        self._cust_lname = lname
    def set_order_date(self, date:datetime.date):
        if type(date) != datetime.datetime:
            raise TypeError
        self._order_date = date
    def set_payment(self, payment:str):
        if payment not in ('kreditni karta', 'hotovost'):
            raise ValueError
        self._payment = payment
    def add_item(self, item:OrderItem):
        if type(item) != OrderItem:
            raise TypeError
        self._items.append(item)