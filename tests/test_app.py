import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities))
    email = "testuser@mergington.edu"

    # Sign up
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup.status_code in (200, 400)  # 400 if already signed up

    # Unregister
    unregister = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister.status_code in (200, 404)  # 404 if not found
