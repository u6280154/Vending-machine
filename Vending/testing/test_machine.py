from app import create_app


def test_machine():
    app = create_app()
    response = app.test_client().post("/addMachine/", json={
        "code": "OORT_CLOUD",
        "address": "Xibalba"
    })
    assert response.status_code == 400
