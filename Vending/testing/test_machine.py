from app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post("/addMachine/", json={
        "code": "Surtr",
        "address": "Scandinevia"
    })
    assert response.status_code == 400
