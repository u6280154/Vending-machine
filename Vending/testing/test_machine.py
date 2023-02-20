from Vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "MICTLAN9", "address": "Xilbalba"}
    )
    assert response.status_code == 200
