from Vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "AVALON2", "address": "Cornwall"}
    )
    assert response.status_code == 200
