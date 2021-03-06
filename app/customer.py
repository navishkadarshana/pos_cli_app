import sys
import os
import json

__db_location__ = "collection"
__customer_folder__ = f"{__db_location__}/customer"
__customer__last_id__ = f"{__db_location__}/customer_id.db"


# @author Navishka Darshana
# @project pos_cli_app
# @CreatedBy PyCharm
# @created 7/09/2021 - 2:31 PM
# @version 3.9


def customer_init(arguments):

    def db():
        os.makedirs(__customer_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "collection":
            db()


class Customer:
    def __init__(customer):
        if os.path.exists(__customer__last_id__):
            with open(__customer__last_id__, "r") as last_id_f:
                customer.last_id = int(last_id_f.readline())
        else:
            customer.last_id = 0

    def save(customer):
        id = customer.last_id+1

        _data_ = {
            "id": id,
            "name": customer.name,
            "address": customer.address,
            "phone": customer.phone

        }
        with open(f"{__customer_folder__}/{id}.db", "w") as customer_file:
            json.dump(_data_, customer_file)

        customer.last_id += 1
        with open(__customer__last_id__, "w") as f:
            f.write(str(customer.last_id))

    def __get_customer_by_path(customer, path):
        with open(path, "r") as customer_file:
            _data_ = json.load(customer_file)
            customer.id = _data_["id"]
            customer.name = _data_["name"]
            customer.address = _data_["address"]
            customer.phone = _data_["phone"]

    def all(self):
        customer_file_names = os.listdir(__customer_folder__)
        customers = []
        for customer_file_name in customer_file_names:
            customer = Customer()
            Customer.__get_customer_by_path(
                customer, f"{__customer_folder__}/{customer_file_name}")
            customers.append(customer)
        return customers

    def search(self, key, value):
        customers = self.all()
        result_customers = []
        for customer in customers:
            customer_value = getattr(customer, key)
            if customer_value == value:
                result_customers.append(customer)
        return result_customers

    def find(self, id):
        Customer.__get_customer_by_path(self, f"{__customer_folder__}/{id}.db")

    def __repr__(self):
        return f"id:{self.id},name:{self.name},address:{self.address},phone:{self.phone}"
