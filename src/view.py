from menu import Menu, Option
from customer import Customer
from category import Category
from product import Product
from order import Order, OrderItem
import form

class View:
    def __init__(self) -> None:
        self._model = None
        self._controller = None
        self.message:str = None

    def reset(self):
        self.message = None
        self.print_menu = True
        self.print_hello = False
        self.print_select_menu = False
        self.print_insert_menu = False
        self.print_order_menu = False
        self.print_categories = False
        self.print_customers = False
        self.print_products = False
        self.print_orders = False
        self.new_category_form = False
        self.new_customer_form = False
        self.new_product_form = False
        self.new_order_form = False
        self.new_order_item_form = False
        self.delete_order_form = False
        self.update_order_form = False
        self.delete_item_form = False

    def update(self):
        print('\n' * 10)
        if self.print_categories: self.categories()
        if self.print_customers: self.customers()
        if self.print_products: self.products()
        if self.print_orders: self.orders()
        if self.new_category_form: self.new_category()
        if self.new_customer_form: self.new_customer()
        if self.new_product_form: self.new_product()
        if self.new_order_form: self.new_order()
        if self.new_order_item_form: self.new_order_item()
        if self.delete_order_form: self.delete_order()
        if self.update_order_form: self.update_order()
        if self.delete_item_form: self.delete_order_item()
        print('\n' * 2)
        if self.message is not None: self.display_message()
        if self.print_order_menu: self.new_order_menu()
        if self.print_menu: self.main_menu()
        if self.print_select_menu: self.select_menu()
        if self.print_insert_menu: self.insert_menu()

    def main_menu(self):
        menu = Menu('Hlavni menu')
        menu.add_opt('vypsat zaznamy', self._controller.show_select_menu)
        menu.add_opt('vytvorit zaznam', self._controller.show_insert_menu)
        menu.add_opt('smazat objednavku', self._controller.show_delete_order)
        menu.add_opt('upravit objednavku', self._controller.show_update_order)
        menu.add_opt('importovat zakazniky', self._controller.import_customer)
        menu.add_opt('importovat kategorie', self._controller.import_category)
        menu.add_opt('ukoncit', self._controller.stop)
        menu.input_message = 'Vyberte jednu z moznosti: '
        print(str(menu))
        menu.user_input()

    def select_menu(self):
        menu = Menu('Vypsat zaznamy')
        menu.add_opt('kategorie', self._controller.show_categories)
        menu.add_opt('zakaznici', self._controller.show_customers)
        menu.add_opt('produkty', self._controller.show_products)
        menu.add_opt('objednavky', self._controller.show_orders)
        menu.add_opt('zpet', self._controller.show_main_menu)
        menu.input_message = 'Vyberte tabulku: '
        print(str(menu))
        menu.user_input()

    def insert_menu(self):
        menu = Menu('Vytvorit zaznam')
        menu.add_opt('kategorie', self._controller.show_new_category_form)
        menu.add_opt('zakaznik', self._controller.show_new_customer_form)
        menu.add_opt('produkt', self._controller.show_new_product_form)
        menu.add_opt('objednavka', self._controller.show_new_order_form)
        menu.add_opt('zpet', self._controller.show_main_menu)
        menu.input_message = 'Vyberte tabulku: '
        print(str(menu))
        menu.user_input()

    def new_order_menu(self):
        menu = Menu('Nova objednavka')
        menu.add_opt('pridat polozku', self._controller.new_order_item)
        menu.add_opt('smazat polozku', self._controller.delete_order_item)
        menu.add_opt('ulozit', self._controller.new_order_commit)
        menu.add_opt('zrusit', self._controller.new_order_rollback)
        menu.input_message = 'Vyberte moznost: '
        print(str(menu))
        menu.user_input()

    def display_message(self):
        print(self.message)

    def categories(self):
        categories:list[Category] = self._model.get_all_categories()
        print('Kategorie(nazev):')
        for i in range(len(categories)):
            print('{num}. {name}'.format(num=i + 1, name=categories[i].get_name()))

    def customers(self):
        customers:list[Customer] = self._model.get_all_customers()
        print('Zakaznici(jmeno; email; adresa):')
        for i in range(len(customers)):
            print('{num}. {jmeno} {prijmeni}; {email}; {street}, {city} {pcode}'.format(
                num = i + 1,
                jmeno = customers[i].get_first_name(),
                prijmeni = customers[i].get_last_name(),
                email = customers[i].get_email(),
                street = customers[i].get_street(),
                city = customers[i].get_city(),
                pcode = customers[i].get_postal_code()
            ))
    def products(self):
        products:list[Product] = self._model.get_all_products()
        print('Produkty(nazev; kategorie; cena; skladem)')
        for i in range(len(products)):
            print('{num}. {name}; {categ}; {price}Kc; {in_stock}'.format(
                num = i + 1,
                name = products[i].get_name(),
                categ = products[i].get_category(),
                price = products[i].get_price(),
                in_stock = products[i].get_in_stock()
            ))

    def orders(self):
        orders:list[Order] = self._model.get_all_orders()
        print('Objednavky(cislo; zakaznik; datum; zpusob platby)')
        for i in range(len(orders)):
            print('{num}. {fname} {lname}; {date}; {payment}'.format(
                num = i + 1,
                fname = orders[i].get_cust_fname(),
                lname = orders[i].get_cust_lname(),
                date = orders[i].get_order_date(),
                payment = orders[i].get_payment()
            ))
            for item in orders[i].get_items():
                print('\t - {name} {price}Kc {amount}x'.format(
                    name = item.get_prod_name(),
                    price = item.get_prod_price(),
                    amount = item.get_amount()
                ))
            print()

    def new_category(self):
        new_category_form = form.Form('Nova kategorie')
        new_category_form.add_input(form.StringInput('Nazev kategorie', 1, 32))
        values = new_category_form.run()
        self._model.new_category(Category(0, values[0]))

    def new_customer(self):
        new_customer_form = form.Form('Novy zakaznik')
        new_customer_form.add_input(form.StringInput('Jmeno', 1, 32))
        new_customer_form.add_input(form.StringInput('Prijmeni', 1, 32))
        new_customer_form.add_input(form.StringInput('Email', 1, 64))
        new_customer_form.add_input(form.StringInput('Mesto', 1, 64))
        new_customer_form.add_input(form.StringInput('Ulice', 1, 64))
        new_customer_form.add_input(form.StringInput('PSC', 1, 5))
        values = new_customer_form.run()
        self._model.new_customer(Customer(0, values[0], values[1], values[2], values[3], values[4], values[5]))

    def new_product(self):
        categories:list[Category] = self._model.get_all_categories()
        new_product_form = form.Form('Novy produkt')
        new_product_form.add_input(form.StringInput('Nazev', 1, 32))
        new_product_form.add_input(form.SelectInput('Kategorie', categories, lambda item: item._name))
        new_product_form.add_input(form.FloatInput('Cena', 1, 99999.99))
        new_product_form.add_input(form.BoolInput('Skladem'))
        values = new_product_form.run()
        self._model.new_product(values[1].get_id(), values[0], values[2], values[3])

    def new_order(self):
        customers:list[Customer] = self._model.get_all_customers()
        new_customer_form = form.Form('Nova objednavka')
        new_customer_form.add_input(form.SelectInput('Zakaznik', customers, lambda item: '{fname} {lname}'.format(fname=item.get_first_name(), lname=item.get_last_name())))
        new_customer_form.add_input(form.DatetimeInput('Datum objednavky'))
        new_customer_form.add_input(form.SelectInput('Zpusob platby', ('kreditni karta', 'hotovost'), lambda item: item))
        values = new_customer_form.run()
        self._model.new_order(values[0].get_id(), values[1], values[2])

    def new_order_item(self):
        products:list[Product] = self._model.get_all_products()
        new_order_item = form.Form('Nova polozka')
        new_order_item.add_input(form.SelectInput('Produkt', products, lambda item: '{name} {price}Kc'.format(name=item.get_name(), price=item.get_price())))
        new_order_item.add_input(form.IntInnput('Mnozstvi', 1, 20))
        values = new_order_item.run()
        self._model.new_order_item(values[0].get_id(), values[1])

    def delete_order_item(self):
        items = self._model.get_order_items()
        delete_item_form = form.Form('Smazat polozku')
        delete_item_form.add_input(form.SelectInput('Polozka', items, lambda item: '{name} {price}Kc {amount}x'.format(
            name=item.get_prod_name(),
            price=item.get_prod_price(),
            amount=item.get_amount()
        )))
        values = delete_item_form.run()
        self._model.delete_order_item(values[0].get_id())

    def delete_order(self):
        orders:list[Order] = self._model.get_all_orders()
        delete_order_form = form.Form('Smazat objednavku')
        delete_order_form.add_input(form.SelectInput('Vyberte objednavku', orders, lambda item: '{fname} {lname}; {date}; {payment}'.format(
                fname = item.get_cust_fname(),
                lname = item.get_cust_lname(),
                date = item.get_order_date(),
                payment = item.get_payment()
            )))
        values = delete_order_form.run()
        self._model.delete_order(values[0].get_id())

    def update_order(self):
        orders:list[Order] = self._model.get_all_orders()
        update_order_form = form.Form('Upravit objednavku')
        update_order_form.add_input(form.SelectInput('Vyberte objednavku', orders, lambda item: '{fname} {lname}; {date}; {payment}'.format(
                fname = item.get_cust_fname(),
                lname = item.get_cust_lname(),
                date = item.get_order_date(),
                payment = item.get_payment()
            )))
        values = update_order_form.run()
        self._model._order = values[0].get_id()