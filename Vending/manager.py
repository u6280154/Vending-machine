from database.machine import Machine
from database.product import Product
from db import db

class Manager:
    def __init__(self):
        self.db = db
        
    def add_machine(self,code,address):
        new_machine = Machine(code=code,address=address)
        self.db.session.add(new_machine)
        self.db.session.commit()
        self.db.session.close()
        
    def delete_machine(self,machine_id):
        Product.query.filter_by(machine_id=machine_id).delete()
        Machine.query.filter_by(code=machine_id).delete()
        self.db.session.commit()
        self.db.session.close()
        
    def edit_machine(self,machine_id,address):
        target_machine = Machine.query.filter_by(code=machine_id).first()
        target_machine.address = address
        self.db.session.commit()
        self.db.session.close()
        
    def add_product(self,machine_id,product_id,name,quantity,price):
        new_product = Product(machine_id=machine_id,
                              product_id=product_id,
                              name=name,
                              quantity=quantity,
                              price=price)
        self.db.session.add(new_product)
        self.db.session.commit()
        self.db.session.close()
        
    def delete_product(self,product_id):
        Product.query.filter_by(product_id=product_id).delete()
        self.db.session.commit()
        self.db.session.close()
        
    def edit_product(self,product_id,name,quantity,price):
        target_product = Product.query.filter_by(product_id=product_id).first()
        target_product.name = name
        target_product.quantity = quantity
        target_product.price = price
        db.session.commit()
        
        
        
        
    