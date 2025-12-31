# מדריך להוספת בדיקות ל-moods-backend

## מבנה התיקיות המומלץ

```
moods-main/backend/
├── app.py (או main.py - הקובץ הראשי)
├── requirements.txt
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_health.py
    └── test_api.py (אופציונלי)
```

## שלב 1: יצירת תיקיית tests

```bash
cd moods-main/backend
mkdir tests
touch tests/__init__.py
```

## שלב 2: קובץ conftest.py (FastAPI)

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app import app  # שנה ל-app.py שלך

@pytest.fixture
def client():
    return TestClient(app)
```

## שלב 3: קובץ conftest.py (Flask)

```python
# tests/conftest.py
import pytest
from app import app  # שנה ל-app.py שלך

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
```

## שלב 4: בדיקת health endpoint

```python
# tests/test_health.py
def test_health_endpoint(client):
    """בדיקה בסיסית של health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json() if hasattr(response, 'get_json') else response.json()
    assert "status" in data or "ok" in str(data).lower()
```

## שלב 5: עדכון requirements.txt

הוסף ל-`moods-main/backend/requirements.txt`:
```
pytest>=7.0.0
pytest-cov>=4.0.0  # אופציונלי - לכיסוי קוד
```

## שלב 6: הרצת בדיקות מקומית

```bash
cd moods-main/backend
pytest tests/
```

## הערות

- אם אין לך endpoint `/health`, תוכל ליצור אחד פשוט או לבדוק endpoint אחר
- הבדיקות יעברו גם אם אין בדיקות (pytest יחזיר 0)
- אחרי שתוסיף בדיקות, ה-CI יעבור עליהן אוטומטית

