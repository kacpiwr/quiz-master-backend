 Quiz API

A FastAPI-based RESTful API for managing quiz questions and sets.

## 📋 Features

- Create, read, and update quiz question sets
- JSON-based question storage
- RESTful endpoints for all CRUD operations
- CORS support for frontend integration
- SQL database integration with SQLModel

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- PostgreSQL (or SQLite for development)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastApiProject
Set up a virtual environment:
bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
bash
pip install fastapi uvicorn sqlmodel
🗄️ Database Setup
For SQLite (Development):
No additional setup required, will use SQLite by default
For PostgreSQL:
Create a new PostgreSQL database
Update the database connection string in your environment:
bash
export DATABASE_URL=postgresql://username:password@localhost:5432/quiz_db
Initialize the database:
bash
python -c "from database import create_db_and_tables; create_db_and_tables()"
🏃 Running the Application
Start the development server:

bash
uvicorn main:app --reload
The API will be available at http://localhost:8000

📚 API Documentation
Interactive API docs (Swagger UI): http://localhost:8000/docs
Alternative API docs (ReDoc): http://localhost:8000/redoc
🌐 API Endpoints
Method	Endpoint	Description	Request Body
POST	/quiz/	Create a new quiz set	{"title": "Quiz Title", "content": {...}}
GET	/quiz/	Get all quiz sets	-
GET	/quiz/{id}	Get a specific quiz set	-
PATCH	/quiz/{id}	Update a quiz set's title	{"title": "New Title"}
📝 Example Requests
Create a new quiz set
http
POST /quiz/
Content-Type: application/json

{
  "title": "General Knowledge",
  "content": {
    "questions": [
      {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
      }
    ]
  }
}
Get all quiz sets
http
GET /quiz/
Get a specific quiz set
http
GET /quiz/1
Update a quiz set's title
http
PATCH /quiz/1
Content-Type: application/json

{
  "title": "Updated Quiz Title"
}
🧪 Testing
You can test the API using the included 
test_main.http
 file with HTTP client tools like VS Code's REST Client extension.

🏗️ Project Structure
fastApiProject/
├── .venv/               # Virtual environment
├── __pycache__/         # Python cache files
├── database.py          # Database configuration
├── main.py              # Main application and API endpoints
├── models.py            # Data models and schemas
└── test_main.http       # API test requests
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
