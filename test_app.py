from app import app

def test_home():
    """Test the home route."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask!" in response.data

def test_add():
    """Test the /add/<a>/<b> route."""
    client = app.test_client()
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert b"2 * 3 = 6" in response.data