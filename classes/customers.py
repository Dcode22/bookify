from customer import Customer
import db_functions

class Customers:
    def __init__(self):
        self.customers_list = []
        self.total_customers = 0
        self.next_nustomer_id = 1


    def fetch_customers_from_database(self):
        self.customers_list = db_functions.fetch_customers_from_database()
        self.update_total_customers()
        self.update_next_customer_id()


    def update_total_customers(self):
        self.total_customers = len(self.customers_list)

    def update_next_customer_id(self):
        self.next_nustomer_id = self.total_customers + 1