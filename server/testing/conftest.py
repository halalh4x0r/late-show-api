import pytest
from server.app import app, db

@pytest.fixture(scope="session")
def test_app():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(test_app):
    return test_app.test_client()

@pytest.fixture
def session(test_app):
    with test_app.app_context():
        yield db.session
