import pytest
from AISEN import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """Test GET request for the index page."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"AI-Powered Sentiment Analyzer" in response.data

def test_sentiment_analysis(client):
    """Test POST request with a sample review."""
    response = client.post("/", data={"review": "I love this movie!"})
    assert response.status_code == 200
    # Expect a "Positive" result
    assert b"Positive" in response.data
