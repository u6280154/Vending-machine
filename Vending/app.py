from flask import Flask
from api.machine_route import machine_controller
from api.product_route import product_controller
from db import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(machine_controller)
    app.register_blueprint(product_controller) 
    return app

if __name__ == '__main__': 
    app = create_app()
    app.run(debug=True) 
    