# Core Django Project with Email Scheduler & User Auth

This repository contains a Django backend with user registration, email OTP verification, JWT authentication, profile picture upload, and a Celery-powered scheduled email system.

---

## Table of Contents

- [Features](#features)  
- [Setup Instructions](#setup-instructions)  
  - [Backend Setup](#backend-setup)  
  - [Optional Frontend](#optional-frontend)  
- [Running the Project](#running-the-project)  
- [Celery Configuration](#celery-configuration)  
- [API Usage & Testing](#api-usage--testing)  
- [Environment Variables](#environment-variables)  

---

## Features

- Custom user model with email authentication  
- User registration with email OTP verification  
- JWT-based login/logout with token blacklisting  
- Profile picture upload to AWS S3  
- Schedule emails with recipients, subject, body, and sending time  
- Celery + Redis for asynchronous task processing  
- Periodic Celery Beat scheduler to send pending scheduled emails  
- Brute-force protection with django-axes  
- CORS support for frontend integration  

---

## Setup Instructions

### Backend Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>


2 .Create and activate a virtual environment

python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows



3. Install dependencies

pip install -r requirements.txt



4. Set up environment variables

Create a .env file in the project root and add:

DEBUG=False
ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1

SECRET_KEY=your-django-secret-key

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password

AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-s3-bucket
AWS_S3_REGION_NAME=your-aws-region

DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379/0



5.Run migrations

python manage.py migrate

6. Create a superuser (optional)
python manage.py createsuperuser


7.Run the development server

python manage.py runserver



Optional Frontend
The backend supports CORS for all origins by default.

You can connect any frontend (e.g., React) to the backend API at /api/.




Running the Project

Start the Django development server:

python manage.py runserver
Start Redis (make sure Redis server is running on your machine at the default port)

Run Celery Beat scheduler to trigger periodic tasks:

celery -A core beat -l info
Run Celery worker to process tasks:

celery -A core worker -l info --pool=solo
Note: Keep Celery Beat and Worker running in separate terminal windows.


Celery Configuration
Broker: Redis (default URL redis://localhost:6379/0)

Task scheduler runs every minute to send pending scheduled emails

Tasks retry on failure up to 3 times



API Usage & Testing
Use tools like Postman or cURL to test the API.

User Endpoints
POST /api/auth/register/ — Register a user (email, password, optional profile picture)

POST /api/auth/verify-otp/ — Verify OTP sent to email

POST /api/auth/login/ — Login and get JWT tokens

POST /api/auth/logout/ — Logout and blacklist refresh token

GET /api/auth/protected/ — Test protected endpoint (requires Bearer token)

PUT /api/auth/update-profile-picture/ — Update profile picture (requires auth)

Email Scheduler Endpoints
POST /emails/schedule/ — Schedule an email (recipients, subject, body, scheduled_time)

GET /emails/schedule/all/ — List all scheduled emails

GET /emails/schedule/<id>/ — Retrieve a scheduled email

PUT/PATCH /emails/schedule/<id>/ — Update a scheduled email

DELETE /emails/schedule/<id>/ — Delete a scheduled email




Environment Variables
Make sure to set the following environment variables for email sending, database, AWS S3 storage, and Celery broker.

| Variable                  | Description                       |
| ------------------------- | --------------------------------- |
| `DEBUG`                   | Enable or disable debug mode      |
| `ALLOWED_HOSTS`           | Comma-separated hostnames         |
| `SECRET_KEY`              | Django secret key                 |
| `EMAIL_HOST_USER`         | Gmail username for SMTP           |
| `EMAIL_HOST_PASSWORD`     | Gmail app password or token       |
| `AWS_ACCESS_KEY_ID`       | AWS S3 access key                 |
| `AWS_SECRET_ACCESS_KEY`   | AWS S3 secret key                 |
| `AWS_STORAGE_BUCKET_NAME` | AWS S3 bucket for media files     |
| `AWS_S3_REGION_NAME`      | AWS S3 region                     |
| `DB_NAME`                 | Postgres database name            |
| `DB_USER`                 | Postgres username                 |
| `DB_PASSWORD`             | Postgres password                 |
| `DB_HOST`                 | Postgres host (usually localhost) |
| `DB_PORT`                 | Postgres port (usually 5432)      |
| `CELERY_BROKER_URL`       | Redis URL for Celery broker       |




Notes

Ensure Redis is installed and running locally for Celery to work.

For production, consider using HTTPS and setting secure cookies.

You can configure CORS_ALLOWED_ORIGINS in settings.py as needed.

