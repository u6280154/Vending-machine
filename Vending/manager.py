from Vending.database.machine import Machine
from Vending.database.product import Product
from Vending.db import db


class Manager:
    def __init__(self):
        self.db = db

    @staticmethod
    def find_machine(code=None):
        machine = {}
        if code:
            machine = Machine.query.filter_by(code=code).first()
        return machine

    @staticmethod
    def find_product(product_id=None):
        product = {}
        if product_id:
            product = Product.query.filter_by(product_id=product_id).first()
        return product

    def add_machine(self, code, address):
        new_machine = Machine(code=code, address=address)
        self.db.session.add(new_machine)
        self.db.session.commit()
        self.db.session.close()

    def delete_machine(self, machine_id):
        Product.query.filter_by(machine_id=machine_id).delete()
        Machine.query.filter_by(code=machine_id).delete()
        self.db.session.commit()
        self.db.session.close()

    def edit_machine(self, machine_id, address=None):
        if address:
            target_machine = Machine.query.filter_by(code=machine_id).first()
            target_machine.address = address
        self.db.session.commit()
        self.db.session.close()

    def add_product(self, machine_id, product_id, name, quantity, price):
        new_product = Product(
            machine_id=machine_id,
            product_id=product_id,
            name=name,
            quantity=quantity,
            price=price
        )
        self.db.session.add(new_product)
        self.db.session.commit()
        self.db.session.close()

    def delete_product(self, product_id):
        Product.query.filter_by(product_id=product_id).delete()
        self.db.session.commit()
        self.db.session.close()

    def edit_product(self, product_id, name=None, quantity=None, price=None):
        target_product = Product.query.filter_by(product_id=product_id).first()
        if name:
            target_product.name = name
        if quantity:
            target_product.quantity = quantity
        if price:
            target_product.price = price
        db.session.commit()
        self.db.session.close()
