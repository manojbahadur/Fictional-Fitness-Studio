from app import create_app, db
from app.models import FitnessClass
from datetime import datetime

app = create_app()
app.app_context().push()

db.create_all()

classes = [
    FitnessClass(name='Yoga', datetime_ist=datetime(2025, 6, 5, 7, 0), instructor='Asha', available_slots=10),
    FitnessClass(name='Zumba', datetime_ist=datetime(2025, 6, 5, 8, 0), instructor='Vikram', available_slots=15),
    FitnessClass(name='Dance', datetime_ist=datetime(2025, 6, 6, 9, 0), instructor='Neha', available_slots=12),
]

db.session.bulk_save_objects(classes)
db.session.commit()
print("Seeded data.")