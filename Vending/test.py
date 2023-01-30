from typing import ByteString
from app_legacy import app
from flask import json


def test_add_machine():
    response = app.test_client().post(
        '/addMachine/',
        data=json.dumps({'code': 'TLALOC1101', 'address': 'MUIC Waterfall'}),
        content_type='application/json'
    )
    
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['code'] == 'TLALOC1101'
    
    