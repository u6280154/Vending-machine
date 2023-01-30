from flask import Blueprint, request, jsonify, render_template
from manager import Manager
from database.machine import Machine

machine_controller = Blueprint("machine_controller",__name__)

@machine_controller.route('/addMachine/', methods=['POST'])
def add_machine():
    code = request.json['code']
    address = request.json['address']
    manager = Manager()
    manager.add_machine(code=code,address=address)
    return request.json

@machine_controller.route('/everyMachine/', methods=['GET'])
def all_machine():
    machines = Machine.query.all()
    machine_list = [{'id': i.id,
                     'code': i.code,
                     'address': i.address} for i in machines]
    return jsonify(machine_list)

@machine_controller.route('/deleteMachine/', methods=['DELETE'])
def delete_machine():
    machine_id =  request.json['machine_id']
    manager = Manager()
    manager.delete_machine(machine_id=machine_id)
    return request.json

@machine_controller.route('/editMachine/', methods=['PUT'])
def edit_machine():
    machine_id =  request.json['machine_id']
    address =  request.json['address']
    manager = Manager()
    manager.edit_machine(machine_id=machine_id,address=address)
    return request.json