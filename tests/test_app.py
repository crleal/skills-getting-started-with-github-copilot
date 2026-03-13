from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    # Arrange
    expected_status = 200
    expected_response = {"message": "Hello World"}

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == expected_status
    assert response.json() == expected_response