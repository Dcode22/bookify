from .customer import Customer

class Customers:
    def __init__(self):
        self.customers_list = []
        self.total_customers = 0
        self.next_nustomer_id = 1

    def __str__(self):
        output=''
        for customer in self.customers_list:
            output += customer.__str__() + '\n'
        return output

    def update_total_customers(self):
        self.total_customers = len(self.customers_list)

    def update_next_customer_id(self):
        self.next_nustomer_id = self.total_customers + 1

    def add_customer(self, customer: 'Customer') -> None:
        self.customers_list.append(customer)
        self.update_total_customers()
        self.update_next_customer_id()

    def search_customer_by_id(self, customer_id: str) -> 'Customer':
        for customer in self.customers_list:
            if customer_id == customer.get_customer_id():
                return customer
        return None
    
    @classmethod
    def from_dict(cls, customers_json: list[dict]) -> 'Customers':
        customers = Customers()
        for customer_json in customers_json:
            customer = Customer.from_dict(customer_json)
            customers.add_customer(customer)
        return customers