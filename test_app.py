import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Health Check ──────────────────────────────────────────────


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


# ── Addition ──────────────────────────────────────────────────


def test_add(client):
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 5
    assert data["operation"] == "addition"


def test_add_negative_numbers(client):
    response = client.post("/add", json={"a": -5, "b": -3})
    assert response.status_code == 200
    assert response.get_json()["result"] == -8


def test_add_floats(client):
    response = client.post("/add", json={"a": 1.5, "b": 2.5})
    assert response.status_code == 200
    assert response.get_json()["result"] == 4.0


# ── Subtraction ───────────────────────────────────────────────


def test_subtract(client):
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 6
    assert data["operation"] == "subtraction"


def test_subtract_negative_result(client):
    response = client.post("/subtract", json={"a": 3, "b": 10})
    assert response.status_code == 200
    assert response.get_json()["result"] == -7


# ── Multiplication ────────────────────────────────────────────


def test_multiply(client):
    response = client.post("/multiply", json={"a": 4, "b": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 20
    assert data["operation"] == "multiplication"


def test_multiply_by_zero(client):
    response = client.post("/multiply", json={"a": 99, "b": 0})
    assert response.status_code == 200
    assert response.get_json()["result"] == 0


# ── Division ──────────────────────────────────────────────────


def test_divide(client):
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 5.0
    assert data["operation"] == "division"


def test_divide_by_zero(client):
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Division by zero is not allowed"


def test_divide_float_result(client):
    response = client.post("/divide", json={"a": 7, "b": 2})
    assert response.status_code == 200
    assert response.get_json()["result"] == 3.5


# ── Error Handling ────────────────────────────────────────────


def test_missing_field_a(client):
    response = client.post("/add", json={"b": 3})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_missing_field_b(client):
    response = client.post("/add", json={"a": 3})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_missing_json_body(client):
    response = client.post("/add", content_type="application/json")
    assert response.status_code == 400
