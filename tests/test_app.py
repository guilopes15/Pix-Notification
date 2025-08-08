from fastapi.testclient import TestClient
from src.pix_notification.app import app

client = TestClient(app)


def test_send_message():
    response = client.post('/send', json={'message': 'Test'})

    assert response.status_code == 200
    assert response.json() == {'message': 'OK'}
    