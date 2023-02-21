from vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "MAC12", "address": "Lake1"}
    )
    assert response.status_code == 200
