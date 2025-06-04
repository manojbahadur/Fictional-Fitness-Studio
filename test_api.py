import pytest
from app import create_app, db
from app.models import FitnessClass

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    with app.app_context():
        db.create_all()
        cls = FitnessClass(name="Test Yoga", datetime_ist="2025-06-05T07:00:00", instructor="Test", available_slots=3)
        db.session.add(cls)
        db.session.commit()
    return app.test_client()

def test_get_classes(client):
    response = client.get('/classes')
    assert response.status_code == 200
    assert b'Test Yoga' in response.data

def test_book_success(client):
    payload = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    res = client.post('/book', json=payload)
    assert res.status_code == 201

def test_overbooking(client):
    for i in range(3):
        client.post('/book', json={
            "class_id": 1,
            "client_name": f"User {i}",
            "client_email": f"user{i}@example.com"
        })
    res = client.post('/book', json={
        "class_id": 1,
        "client_name": "Overflow",
        "client_email": "overflow@example.com"
    })
    assert res.status_code == 400
