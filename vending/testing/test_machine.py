from vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "MAC1", "address": "Lake"}
    )
    assert response.status_code == 200
