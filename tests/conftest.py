import main
import pytest


@pytest.fixture()
def app():
    app = main.app
    return app.test_client()
