#!/usr/bin/python3

class Invoice:
    """A simple invoice class"""

    def __init__(self, part_number, part_description, quantity, price):
        """Initializes an instance of an invoice"""
        self.part_number = part_number
        self.part_description = part_description
        self.quantity = quantity
        self.price = price

    @property
    def part_number(self):
        """getter for part_number"""
        return self.__part_number

    @part_number.setter
    def part_number(self, value):
        """setter for part_number"""
        self.__part_number = value

    @property
    def part_description(self):
        """getter for part_description"""
        return self.__part_description

    @part_description.setter
    def part_description(self, value):
        """Setter for part_description"""
        self.__part_description = value

    @property
    def quantity(self):
        """getter for quantity"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        """setter for part description"""
        self.__quantity = 0 if value < 0 else value

    @property
    def price(self):
        """Getter for price"""
        return self.__price

    @price.setter
    def price(self, value):
        """setter for price"""
        self.__price = 0.0 if value < 0 else value

    def get_invoice_amount(self):
        """Calculates the invoice amount"""
        return self.__quantity * self.__price

my_invoice = Invoice(56, "Nice part", -67, 23)
print(my_invoice.get_invoice_amount())
