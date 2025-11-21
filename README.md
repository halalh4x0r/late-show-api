# Late Show API

A Flask RESTful API for managing a late-night TV show domain with episodes, guests, and appearances. This project demonstrates full backend API development using Flask, SQLAlchemy, and Flask-RESTful, including database relationships, validations, and testing.

# Table of Contents

Features

Tech Stack

Project Structure

Setup Instructions

Database Setup & Seeding

API Endpoints

Running Tests

License

# Features

Manage Episodes of a late-night TV show.

Manage Guests who appear on episodes.

Manage Appearances linking Guests to Episodes with ratings.

Validations for ratings (1–5) to maintain data integrity.

Cascade deletes to maintain database consistency.

JSON serialization for clean API responses.

Fully tested with pytest.

# Tech Stack

Python 3.10+

Flask 2.3

Flask-RESTful

SQLAlchemy

SQLite (default, can be switched to other databases)

Flask-Migrate (database migrations)

pytest (unit & integration testing)

# Project Structure
late-show-api/
├── server/
│   ├── app.py             # Flask application & routes
│   ├── models.py          # Database models
│   ├── seed.py            # Seed database with sample data
│   └── testing/           # Pytest tests
│       ├── conftest.py
│       ├── models_test.py
│       └── app_test.py
├── env/                   # Python virtual environment
├── migrations/            # Database migration files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

## Setup Instructions

Clone the repository:

git clone <your-repo-url>
cd late-show-api


Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate    # Linux/macOS
# env\Scripts\activate    # Windows


# Install dependencies:

pip install -r requirements.txt

Database Setup & Seeding

Set environment variable for Flask:

export FLASK_APP=server/app.py


Initialize and migrate the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


Seed the database with sample data:

python server/seed.py

API Endpoints
Episodes

GET /episodes – Get all episodes

GET /episodes/<id> – Get a single episode with its appearances

DELETE /episodes/<id> – Delete an episode and its appearances

Guests

GET /guests – Get all guests

Appearances

POST /appearances – Create a new appearance

# Sample JSON for creating an appearance:

{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}

# Running Tests

All tests use pytest. Make sure your virtual environment is active.

pytest -x


models_test.py – Tests database relationships, validations, and cascade deletes.

app_test.py – Tests all API endpoints for success and failure cases.

# Notes

The project uses SQLite by default. To switch databases, update the URI in app.py.

Ensure Werkzeug version is compatible (Werkzeug==2.3.7) to avoid Flask test client errors.

# License

MIT License © 2025