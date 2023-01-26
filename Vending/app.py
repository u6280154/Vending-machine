from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Machine(db.Model):
    __tablename__ = 'Machine'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), unique=True)
    
class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    machine_id = db.Column(db.String(100),db.ForeignKey('Machine.code'))
    product_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer, unique=True)
    price = db.Column(db.Float, unique=True)
    
with app.app_context():
    db.create_all()
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/addMachine/', methods=['POST'])
def add_machine():
    new_machine = Machine(code=request.json['code'],address=request.json['address'])
    db.session.add(new_machine)
    db.session.commit()
    return request.json

@app.route('/everyMachine/', methods=['GET'])
def all_machine():
    machines = Machine.query.all()
    machine_list = [{'id': i.id,
                     'code': i.code,
                     'address': i.address} for i in machines]
    return jsonify(machine_list)

@app.route('/deleteMachine/', methods=['DELETE'])
def delete_machine():
    Product.query.filter_by(machine_id=request.json['machine_id']).delete()
    Machine.query.filter_by(code=request.json['machine_id']).delete()
    db.session.commit()
    return request.json
              
@app.route('/addProduct/', methods=['POST'])
def add_product():
    new_product = Product(machine_id=request.json['machine_id'],
                          product_id=request.json['product_id'],
                          name=request.json['name'],
                          quantity=request.json['quantity'],
                          price=request.json['price'])
    db.session.add(new_product)
    db.session.commit()
    return request.json
    
@app.route('/everyProduct/', methods=['GET'])
def all_product():
    producters = Product.query.all()
    product_list = [{'id': i.id,
                     'machine_id': i.machine_id,
                     'product_id': i.product_id,
                     'name': i.name,
                     'quantity': i.quantity,
                     'price': i.price} for i in producters]
    return jsonify(product_list)

@app.route('/deleteProduct/', methods=['DELETE'])
def delete_product():
    Product.query.filter_by(product_id=request.json['product_id']).delete()
    db.session.commit()
    return request.json

@app.route('/deleteAllProduct/', methods=['DELETE'])
def delete_all_product():
    Product.query.filter_by(machine_id=request.json['machine_id']).delete()
    db.session.commit()
    return request.json

@app.route('/editMachine/', methods=['PUT'])
def modify_machine():
    target_machine = Machine.query.filter_by(code=request.json['machine_id']).first()
    target_machine.address =  request.json['address']
    db.session.commit()
    return request.json
     

@app.route('/editProduct/', methods=['PUT'])
def modify_product():
    target_product = Product.query.filter_by(product_id=request.json['product_id']).first()
    target_product.name = request.json['name']
    target_product.quantity = request.json['quantity']
    target_product.price = request.json['price']
    db.session.commit()
    return request.json

@app.route('/stockIncrement/', methods=['PUT'])
def increment():
    target_product = Product.query.filter_by(product_id=request.json['product_id']).first()
    target_product.quantity += 1
    db.session.commit()
    return request.json

@app.route('/stockDecrement/', methods=['PUT'])
def decrement():
    target_product = Product.query.filter_by(product_id=request.json['product_id']).first()
    target_product.quantity -= 1
    db.session.commit()
    return request.json

@app.route('/stockIncrement_By/', methods=['PUT'])
def increment_by():
    target_product = Product.query.filter_by(product_id=request.json['product_id']).first()
    target_product.quantity += request.json['value']
    db.session.commit()
    return request.json

@app.route('/stockDecrement_By/', methods=['PUT'])
def decrement_by():
    target_product = Product.query.filter_by(product_id=request.json['product_id']).first()
    target_product.quantity -= request.json['value']
    db.session.commit()
    return request.json
     
if __name__ == '__main__':
    app.run(debug=True)