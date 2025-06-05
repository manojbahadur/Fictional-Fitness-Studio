# Fitness Booking API

A Flask-based backend for managing fitness class bookings.

# 🧘‍♀️ Fitness Studio Booking API

This is a Flask-based backend system that enables booking, viewing, and managing fitness classes such as Yoga, Zumba, and HIIT. It demonstrates core backend skills including REST API design, validation, logging, error handling, timezone management, and Swagger UI documentationc.

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
- ✅ Swagger UI with live documentation and request validation

---

## 📦 Folder Structure
fitness_booking_api/<br>
├── app/<br>
│ ├── init.py # Flask factory & DB init<br>
│ ├── models.py # SQLAlchemy models<br>
│ ├── routes.py # API endpoints<br>
│ ├── utils.py # helper<br>
│ └── logger.py # Logger setup<br>
├── logs/ # Rotating log files<br>
├── seed_data.py # Populates DB with sample classes<br>
├── main.py # Entry point<br>
├── requirements.txt<br>
├── .gitignore<br>
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

[Record a short Loom walkthrough of how the project works.](https://www.loom.com/share/4d2f672ce9d64ba398d2bd0b062b0a50?sid=38a799e1-1faa-4403-94f9-ebcef4b3cb14)
