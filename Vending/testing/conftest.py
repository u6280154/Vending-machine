import pytest
from vending.app import create_app


@pytest.fixture()
def app():
    return create_app()
