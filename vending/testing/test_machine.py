from vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "AVALON7", "address": "Lake District"}
    )
    assert response.status_code == 200
