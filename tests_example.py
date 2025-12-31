"""
דוגמה לבדיקות עבור moods-backend
העתק את הקבצים האלה ל-moods-main/backend/tests/
"""

# דוגמה 1: בדיקת endpoint בסיסי (FastAPI/Flask)
# אם הבקאנד שלך משתמש ב-FastAPI:
"""
import pytest
from fastapi.testclient import TestClient
from app import app  # או מה ששם הקובץ הראשי שלך

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
"""

# דוגמה 2: בדיקת endpoint בסיסי (Flask):
"""
import pytest
from app import app  # או מה ששם הקובץ הראשי שלך

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
"""

# דוגמה 3: בדיקות פונקציות פשוטות:
"""
def test_basic_math():
    assert 1 + 1 == 2

def test_string_operations():
    text = "hello"
    assert text.upper() == "HELLO"
"""

