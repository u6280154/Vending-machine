from Vending.app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post(
        "/addMachine/", json={"code": "MICTLAN1", "address": "Tlalocan"}
    )
    assert response.status_code == 200
