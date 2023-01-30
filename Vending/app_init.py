from flask import Flask
from API.machine_route import machine_controller
from API.product_route import product_controller
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(machine_controller)
    app.register_blueprint(product_controller)   
    app.run(debug=True) 
    