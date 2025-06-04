# Fitness Booking API

A Flask-based backend for managing fitness class bookings.

# 🧘‍♀️ Fitness Studio Booking API

This is a Flask-based backend system that enables booking, viewing, and managing fitness classes such as Yoga, Zumba, and HIIT. It demonstrates core backend skills including REST API design, validation, logging, error handling, timezone management, and basic testing.

---

## 🚀 Features

- ✅ View all upcoming classes
- ✅ Book a class if slots are available
- ✅ View all bookings for a user by email
- ✅ Slot decrement logic on booking
- ✅ Duplicate booking prevention
- ✅ Timezone-aware class timings
- ✅ Validation with Pydantic
- ✅ Logging to `info.log` and `error.log` with line numbers
- ✅ Docker support for easy deployment
- ✅ Unit tests using Pytest

---

## 📦 Folder Structure
fitness_booking_api/
├── app/
│ ├── init.py # Flask factory & DB init
│ ├── models.py # SQLAlchemy models
│ ├── routes.py # API endpoints
│ ├── utils.py # helper
│ └── logger.py # Logger setup
├── logs/ # Rotating log files
├── seed_data.py # Populates DB with sample classes
├── main.py # Entry point
├── requirements.txt
├── .gitignore
└── README.md

## Endpoints

- `GET /classes?timezone={TIMEZONE}`
- `POST /book`
- `GET /bookings?email={EMAIL_ID}`

## Swagger Endpoint - API Documentation

- `/docs`

## Setup

```bash
pip install -r requirements.txt
python seed_data.py
python main.py
```


## Loom Video

Record a short Loom walkthrough of how the project works.