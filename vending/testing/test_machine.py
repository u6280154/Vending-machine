
def test_get_all_machine(app):
    response = app.test_client().get(
        "/everyMachine/"
    )
    assert response.status_code == 200


def test_add_machine(app):
    response = app.test_client().post(
        "/addMachine/", json={"code": "MAC123", "address": "Lake13"}
    )
    assert response.status_code == 200
