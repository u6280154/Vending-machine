from flask.testing import FlaskClient


def test_get_all_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.get("/everyMachine/")
    assert response.status_code == 200


def test_add_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.post(
        "/addMachine/", json={"code": "MAC12345", "address": "Lake1345"}
    )
    response1 = client.post(
        "/addMachine/", json={"code": "MAC123456", "address": "Lake13456"}
    )
    assert response.status_code == 200
    assert response1.status_code == 200


def test_delete_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.delete("/deleteMachine/", json={"machine_id": "MAC12345"})
    assert response.status_code == 200


def test_edit_machine(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.put(
        "/editMachine/", json={"machine_id": "MAC123456", "address": "Void"}
    )
    assert response.status_code == 200
