from flask.testing import FlaskClient


def test_add_product(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.post(
        "/addProduct/",
        json={
            "machine_id": "MAC123456",
            "product_id": "L",
            "name": "Reo",
            "quantity": 1,
            "price": 16.8,
        },
    )
    response1 = client.post(
        "/addProduct/",
        json={
            "machine_id": "MAC123456",
            "product_id": "L1",
            "name": "OP",
            "quantity": 12,
            "price": 12.9,
        },
    )
    assert response.status_code == 200
    assert response1.status_code == 200


def test_all_product(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.get("/everyProduct/")
    assert response.status_code == 200


def test_delete_product(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.delete("/deleteProduct/", json={"product_id": "L"})
    assert response.status_code == 200


def test_edit_product(client: FlaskClient) -> None:
    """High level support for doing this and that."""
    response = client.put(
        "/editProduct/",
        json={"product_id": "L1", "name": "OP", "quantity": 10, "price": 11.1},
    )
    assert response.status_code == 200
