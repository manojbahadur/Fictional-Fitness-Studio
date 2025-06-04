from flask import Blueprint, request, jsonify, current_app
from .models import FitnessClass, Booking
from . import db
from datetime import datetime
from pydantic import BaseModel, EmailStr, ValidationError
from pytz import timezone

main = Blueprint('main', __name__)

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

@main.route('/classes', methods=['GET'])
def get_classes():
    user_tz = request.args.get('timezone', 'Asia/Kolkata')
    try:
        tz = timezone(user_tz)
    except Exception:
        return jsonify({'error': 'Invalid timezone', 'status_code': '400'}), 400

    classes = FitnessClass.query.all()
    data = []
    for cls in classes:
        dt_local = timezone('Asia/Kolkata').localize(cls.datetime_ist).astimezone(tz)
        data.append({
            'id': cls.id,
            'name': cls.name,
            'datetime': dt_local.isoformat(),
            'instructor': cls.instructor,
            'available_slots': cls.available_slots
        })
    current_app.logger.info(f"Classes returned in timezone {user_tz}")
    return jsonify(data), 200

@main.route('/book', methods=['POST'])
def book_class():
    try:
        json_data = request.get_json(force=True)
        data = BookingRequest(**json_data)
    except ValidationError as ve:
        current_app.logger.warning(f"Validation error: {ve}")
        return jsonify({'error': ve.errors(), 'status_code': '422'}), 422
    except Exception as e:
        current_app.logger.error(f"Invalid request format: {e}")
        return jsonify({'error': 'Invalid request format', 'status_code': '400'}), 400

    cls = FitnessClass.query.get(data.class_id)
    if not cls:
        current_app.logger.warning(f"Class not found: ID {data.class_id}")
        return jsonify({'error': 'Class not found', 'status_code': '404'}), 404

    if cls.available_slots <= 0:
        current_app.logger.info(f"No slots left for class ID {data.class_id}")
        return jsonify({'error': 'No slots available', 'status_code': '400'}), 400

    existing = Booking.query.filter_by(class_id=data.class_id, client_email=data.client_email).first()
    if existing:
        current_app.logger.info(f"Duplicate booking attempt for class ID {data.class_id} by {data.client_email}")
        return jsonify({'error': 'You have already booked this class', 'status_code': '409'}), 409

    try:
        booking = Booking(
            class_id=data.class_id,
            client_name=data.client_name,
            client_email=data.client_email
        )
        cls.available_slots -= 1
        db.session.add(booking)
        db.session.commit()

        current_app.logger.info(f"Booking successful for {data.client_email} in class ID {data.class_id}")
        return jsonify({'message': 'Booking successful'}), 201
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Database error during booking: {e}")
        return jsonify({'error': 'Could not process booking', 'status_code': '500'}), 500

@main.route('/bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    
    if not email:
        current_app.logger.warning("Missing email in /bookings request")
        return jsonify({'error': 'Email is required', 'status_code': '400'}), 400

    try:
        bookings = Booking.query.filter_by(client_email=email).all()

        if not bookings:
            current_app.logger.info(f"No bookings found for {email}")
            return jsonify({'message': 'No bookings found for this email.', 'status_code': '404'}), 404

        data = []
        for b in bookings:
            data.append({
                'id': b.id,
                'class_id': b.class_id,
                'client_name': b.client_name,
                'client_email': b.client_email,
                'booking_time': b.booking_time.isoformat()
            })

        current_app.logger.info(f"Returned bookings for {email}")
        return jsonify(data), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching bookings for {email}: {e}")
        return jsonify({'error': 'Internal server error', 'status_code': '500'}), 500