import pytest


@pytest.fixture
def client():
    from app import create_app
    app=create_app()
    #app.config['TESTING'] = True
    return True