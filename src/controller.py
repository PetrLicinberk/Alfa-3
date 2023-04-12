class Controller:
    def __init__(self) -> None:
        self._model = None
        self._view = None
    
    def run(self):
        self.show_main_menu()

    def stop(self):
        self._view.reset()
        self._view.message = 'Program ukoncen.'
        self._view.print_menu = False
        self._view.update()

    def show_main_menu(self):
        self._view.reset()
        self._view.update()

    def show_select_menu(self):
        self._view.reset()
        self._view.print_select_menu = True
        self._view.print_menu = False
        self._view.update()
    
    def show_categories(self):
        self._view.reset()
        self._view.print_select_menu = True
        self._view.print_menu = False
        self._view.print_categories = True
        self._view.update()

    def show_customers(self):
        self._view.reset()
        self._view.print_select_menu = True
        self._view.print_menu = False
        self._view.print_customers = True
        self._view.update()

    def show_products(self):
        self._view.reset()
        self._view.print_select_menu = True
        self._view.print_menu = False
        self._view.print_products = True
        self._view.update()

    def show_orders(self):
        self._view.reset()
        self._view.print_select_menu = True
        self._view.print_menu = False
        self._view.print_orders = True
        self._view.update()

    def show_insert_menu(self):
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.update()

    def show_new_category_form(self):
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.new_category_form = True
        self._view.update()

    def show_new_customer_form(self):
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.new_customer_form = True
        self._view.update()

    def show_new_product_form(self):
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.new_product_form = True
        self._view.update()

    def show_new_order_form(self):
        self._view.reset()
        self._view.print_order_menu = True
        self._view.print_menu = False
        self._view.new_order_form = True
        self._view.update()

    def new_order_item(self):
        self._view.reset()
        self._view.print_order_menu = True
        self._view.print_menu = False
        self._view.new_order_item_form = True
        self._view.update()

    def new_order_commit(self):
        self._model.commit()
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.message = 'Zmeny byly provedeny.'
        self._view.update()

    def new_order_rollback(self):
        self._model.rollback()
        self._view.reset()
        self._view.print_insert_menu = True
        self._view.print_menu = False
        self._view.message = 'Nebyly provedeny zadne zmeny.'
        self._view.update()

    def show_delete_order(self):
        self._view.reset()
        self._view.print_menu = True
        self._view.delete_order_form = True
        self._view.update()

    def show_update_order(self):
        self._view.reset()
        self._view.print_menu = False
        self._view.update_order_form = True
        self._view.print_order_menu = True
        self._view.update()

    def delete_order_item(self):
        self._view.reset()
        self._view.print_menu = False
        self._view.delete_item_form = True
        self._view.print_order_menu = True
        self._view.update()

    def import_customer(self):
        self._model.import_customer()
        self._view.reset()
        self._view.update()

    def import_category(self):
        self._model.import_category()
        self._view.reset()
        self._view.update()