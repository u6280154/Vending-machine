from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
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
    machine_id = db.Column(db.String(100))
    name = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

with app.app_context():
    db.create_all()
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/addMachine/', methods=['POST'])
def add_machine():
    if request.headers.get('Content-Type') == 'application/json':
        new_machine = Machine(code=request.json['code'],address=request.json['address'])
        db.session.add(new_machine)
        db.session.commit()
        return request.json

@app.route('/everyMachine/', methods=['GET'])
def all_machine():
    machines = Machine.query.all()
    machine_list = [{'id': i.id,'code': i.code,'address': i.address} for i in machines]
    return jsonify(machine_list)

if __name__ == '__main__':
    app.run(debug=True)