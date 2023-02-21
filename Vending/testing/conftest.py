import pytest
from flask import Flask
from flask.testing import FlaskClient

from vending.app import create_app


@pytest.fixture()
def app() -> Flask:
    """High level support for doing this and that."""
    return create_app()


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    """High level support for doing this and that."""
    return app.test_client()
