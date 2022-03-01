from types import *
import csv
# This is an instance attribute


class Phone:
    # Class Attributes --> Properties unique per instance, global
    # 20% discount in all phones
    pay_rate = 0.8
    get_all = []

    # In this case we made the quantity nullable
    # Specify the data type
    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        # assert type(price) is IntType, f"price {price} must be a number"
        assert price >= 0, f"price {price} must be a positive number"
        # assert type(quantity) is float or int, f"quantity {quantity} must be a number"
        assert quantity >= 0, f"Quantity {quantity} must be a positive number"
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions that executes after creating each element
        Phone.get_all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Class Method --> methods that we want to call not having an instance of an object. So the parameter is the class
    # Used to manipulate different structures of data to instantiate objects
    @classmethod
    def get_from_csv(cls):
        phones_file = open('phones.csv', 'r')
        reader = csv.DictReader(phones_file)
        items = list(reader)
        for item in items:
            Phone(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    # Static method --> do something related with the class but not something unique per instance
    # Receives regular parameters, nor classes or self
    @staticmethod
    def is_integer(number):
        return number.is_integer()

    # How to represent the items when printed
    def __repr__(self):
        return f"Item('{self.name}','{self.price}', '{self.quantity}')"

