import pytest

from src.flask_app import create_app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('A9_OTLP_ENABLED', '0')
    return create_app().test_client()


def test_checkout_returns_paid_status(client):
    response = client.get('/checkout')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'paid'}


def test_checkout_error_returns_controlled_error(client):
    response = client.get('/checkout/error')

    assert response.status_code == 500
    assert response.get_json() == {'error': 'payment gateway timeout'}
