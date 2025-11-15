Quiz API

A FastAPI-based RESTful API for managing quiz questions and sets.

📋 Features

Create, read, and update quiz question sets

JSON-based question storage

RESTful endpoints for all CRUD operations

CORS support for frontend integration

SQL database integration with SQLModel

🚀 Getting Started
Prerequisites

Python 3.8+

pip

PostgreSQL (or SQLite for development)

🛠️ Installation
1. Clone the repository

git clone <repository-url>
cd fastApiProject

2. Set up a virtual environment

python -m venv .venv
source .venv/bin/activate
(Windows: .venv\Scripts\activate)

3. Install dependencies

pip install fastapi uvicorn sqlmodel

🗄️ Database Setup
SQLite (Development)

No additional setup required.

PostgreSQL

Create a PostgreSQL database

Set DATABASE_URL:
export DATABASE_URL=postgresql://username:password@localhost:5432/quiz_db

Initialize the database:
python -c "from database import create_db_and_tables; create_db_and_tables()"

🏃 Running the Application

uvicorn main:app --reload

API runs on: http://localhost:8000
