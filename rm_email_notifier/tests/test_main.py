import pytest
from fastapi.testclient import TestClient

from rm_email_notifier.main import app


@pytest.fixture
def profile_data():
    return {
        "text": "Old Kant Road is a hub of activity...",
        "metadata": {
            "url": "https://www.rm.co.uk/properties/151624097",
            "price": "£1,595 pcm",
            "location": "8 Hendre Road London SE1",
            "summary": "1 bedroom apartment",
        }
    }


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_profiles(mocker, client, profile_data):
    mock_send = mocker.patch("rm_email_notifier.main.email.send")

    response = client.post("/api/v1/profiles", data=profile_data)

    assert response.status_code == 201
    mock_send.assert_called_once_with(profile_data)
