from fastapi.testclient import TestClient

from pwncore import app

client = TestClient(app)


def test_login():
    # Send a GET response to the specified endpoint
    #response = client.get("/api/team/login")

    # Evaluate the response against expected values
    #assert response.status_code == 200
    #assert response.json() == {"status": True}

    #resp2 = client.get("/api/team/update/test/1")
    #assert resp2.json() == {"status":True}

    #resp3 = client.get("/api/team/get/current_points")
    #assert resp3.json() == {"status":2}

    resp4 = client.get("/api/team/members/update")
    assert resp4.json() == {"status":True}
