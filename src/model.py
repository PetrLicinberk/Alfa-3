from category import Category
from customer import Customer
from product import Product
from order import Order, OrderItem
import datetime
import config

class Model:
    def __init__(self, connection, conf):
        self._connection = connection
        self._controller = None
        self._view = None
        self._conf = conf

    def get_all_categories(self) -> list[Category]:
        categories = []
        cursor = self._connection.cursor()
        query = 'select * from shop.category'
        cursor.execute(query)
        for (id, name) in cursor:
            categories.append(Category(int(id), name))
        return categories
    
    def get_all_customers(self) -> list[Customer]:
        customers = []
        cursor = self._connection.cursor()
        query = 'select * from shop.customer'
        cursor.execute(query)
        for (id, first_name, last_name, email, city, street, postal_code) in cursor:
            customers.append(Customer(int(id), first_name, last_name, email, city, street, postal_code))
        return customers
    
    def get_all_products(self) -> list[Product]:
        products = []
        cursor = self._connection.cursor()
        query = 'select p.id, p.name, c.name category, p.price, p.in_stock from shop.product p inner join shop.category c on p.category_id = c.id'
        cursor.execute(query)
        for (id, name, category, price, in_stock) in cursor:
            products.append(Product(int(id), category, name, float(price), bool(in_stock)))
        return products

    def get_all_orders(self) -> list[Order]:
        orders:list[Order] = []
        cursor = self._connection.cursor()
        cursor.execute('select * from shop.order_items')
        for (id, fname, lname, date, payment, item_id, prod_name, prod_price, amount) in cursor:
            if len(orders) == 0 or id != orders[len(orders) - 1].get_id():
                orders.append(Order(int(id), fname, lname, date, payment))
            orders[len(orders) - 1].add_item(OrderItem(int(item_id), prod_name, float(prod_price), int(amount)))
        return orders
    
    def get_order_items(self):
        items:list[OrderItem] = []
        cursor = self._connection.cursor()
        cursor.execute('select * from shop.order_items where id = %s', (self._order,))
        for (id, fname, lname, date, payment, item_id, prod_name, prod_price, amount) in cursor:
            items.append(OrderItem(int(item_id), prod_name, float(prod_price), int(amount)))
        return items
    
    def new_category(self, category:Category):
        cursor = self._connection.cursor()
        cursor.execute('insert into shop.category(name) values(%s)', (category.get_name(),))
        cursor.execute('commit')

    def new_customer(self, customer:Customer):
        cursor = self._connection.cursor()
        cursor.execute('insert into shop.customer(first_name, last_name, email, city, street, postal_code) values(%s, %s, %s, %s, %s, %s)',
                       (customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_city(), customer.get_street(), customer.get_postal_code()))
        cursor.execute('commit')

    def new_product(self, categ_id, name, price, in_stock):
        cursor = self._connection.cursor()
        cursor.execute('insert into shop.product(name, category_id, price, in_stock) values(%s, %s, %s, %s)',
                       (name, categ_id, price, in_stock))
        cursor.execute('commit')

    def new_order(self, cust_id, date, payment):
        cursor = self._connection.cursor()
        cursor.execute('insert into shop.order_details(customer_id, order_date, payment) values(%s, %s, %s)',
                       (cust_id, date, payment))
        self._order = cursor.lastrowid

    def new_order_item(self, prod_id, amount):
        cursor = self._connection.cursor()
        cursor.execute('insert into shop.order_item(order_id, product_id, amount) values(%s, %s, %s)',
                       (self._order, prod_id, amount))
        
    def delete_order(self, order_id):
        cursor = self._connection.cursor()
        cursor.execute('delete from shop.order_item where order_id = %s', (order_id,))
        cursor.execute('delete from shop.order_details where id = %s', (order_id,))
        cursor.execute('commit')

    def delete_order_item(self, item_id):
        cursor = self._connection.cursor()
        cursor.execute('delete from shop.order_item where id = %s', (item_id,))
        cursor.execute('commit')
        
    def commit(self):
        cursor = self._connection.cursor()
        cursor.execute('commit')
        self._order = None

    def rollback(self):
        cursor = self._connection.cursor()
        cursor.execute('rollback')
        self._order = None

    def import_customer(self):
        cursor = self._connection.cursor()
        with open(self._conf['import']['zakaznik'], 'r') as file:
            for line in file:
                parsed = line.split(';')
                self.new_customer(Customer(0, parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], parsed[5]))
        cursor.execute('commit')
    
    def import_category(self):
        cursor = self._connection.cursor()
        with open(self._conf['import']['kategorie'], 'r') as file:
            for line in file:
                parsed = line.split(';')
                self.new_category(Category(0, parsed[0]))
        cursor.execute('commit')
        