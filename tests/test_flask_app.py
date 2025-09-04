import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask_app import app

import json
from flask_app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"ACEest Fitness API is running" in resp.data

def test_add_and_view_workouts():
    client = app.test_client()

    # Add a workout
    resp = client.post("/add", json={"workout": "Pushups", "duration": 15})
    assert resp.status_code == 201

    # Fetch workouts list
    resp = client.get("/workouts")
    data = json.loads(resp.data)
    assert {"workout": "Pushups", "duration": 15} in data
