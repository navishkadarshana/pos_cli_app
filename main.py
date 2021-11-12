import sys
from app.item import Item, item_init
from app.customer import Customer, customer_init
from app.order import Order, order_init
from pprint import pprint

# @author Navishka Darshana
# @project pos_cli_app
# @CreatedBy PyCharm
# @created 4/09/2021 - 6:23 PM
# version 3.9


__db_location__ = "collection"
__session_file__ = f"{__db_location__}/session.db"


# Customer

def customer_add(name, address, phone):
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.phone = phone
    customer.save()


def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)


def customer_find(id):
    customer = Customer()
    customer.find(id)
    print(customer.id, customer.name, customer.address, customer.phone)


def customer_search(key, value):
    customer = Customer()
    results = customer.search(key, value)
    pprint(results)

# Order


def item_add(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()


def item_all():
    item = Item()
    items = item.all()
    pprint(items)


def item_find(id):
    item = Item()
    item.find(id)
    print(item.id, item.name, item.price, item.selling_price)


def item_search(key, value):
    item = Item()
    results = item.search(key, value)
    pprint(results)

# User


def login(username):
    f = open(__session_file__, "w")
    f.write(username)
    f.close()


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def get_user():
    username = __get_logged_user()
    print(username)

# Order


def order_place(customer_id, item_id, item_price, quantity):
    order = Order()
    order.customerId = customer_id
    order.itemId = item_id
    order.itemPrice = item_price
    order.itemQty = quantity
    order.itemTotal = int(item_price) * int(quantity)
    order.save()


def order_all():
    order = Order()
    orders = order.all()
    pprint(orders)


def order_view(id):
    order = Order()
    order.find(id)
    print(order)


def order_search(key, value):
    order = Order()
    results = order.search(key, value)
    pprint(results)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    item_init(arguments)
    customer_init(arguments)
    order_init(arguments)

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "login":
            login(*params)
        elif command == "get":
            get_user()
    elif section == "customer":
        if command == "add":
            customer_add(*params)
        elif command == "all":
            customer_all()
        elif command == "find":
            customer_find(*params)
        elif command == "search":
            customer_search(*params)
    elif section == "item":
        if command == "add":
            item_add(*params)
        elif command == "all":
            item_all()
        elif command == "find":
            item_find(*params)
        elif command == "search":
            item_search(*params)
    elif section == "order":
        if command == "place":
            order_place(*params)
        elif command == "all":
            order_all()
        elif command == "view":
            order_view(*params)
        elif command == "search":
            order_search(*params)
