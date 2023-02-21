from flask.testing import FlaskClient


def test_get_all_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.get("/everyMachine/")
    assert response.status_code == 200


def test_add_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.post(
        "/addMachine/", json={"code": "MAC1234", "address": "Lake134"}
    )
    assert response.status_code == 200
