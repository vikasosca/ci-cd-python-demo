from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"CI/CD running using flask" in response.data  # or your actual message
