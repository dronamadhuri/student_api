🎓 Student Management API (FastAPI)

A simple CRUD-based Student Management System built using FastAPI with a modular backend structure.

🚀 Features
Add student
Get all students
Get student by ID
Update student
Delete student
Search student by name
JSON file-based storage (no database required)
Clean modular architecture (routers, crud, utils, middleware)
🏗️ Project Structure

student_api/

app/

main.py → FastAPI entry point
database.py → Load & save JSON file
models.py → Data models
schemas.py → Pydantic schemas
crud.py → Business logic (CRUD functions)

routers/

students.py → Student APIs
auth.py → Authentication APIs (optional future use)

utils/

security.py → JWT / password logic (future use)
validators.py → Email and data validation helpers
pagination.py → Pagination helpers

middleware/

request_logger.py → Logs every API request

data/

students.json → JSON database file

tests/

test_students.py → Unit tests for students API
test_auth.py → Unit tests for auth API

requirements.txt → Project dependencies
.gitignore → Ignored files
README.md → Project documentation

⚙️ Installation & Setup
1. Clone repository

git clone https://github.com/dronamadhuri/student_api.git
cd student_api

2. Create virtual environment

python -m venv .venv

3. Activate virtual environment

Windows:
.venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

5. Run server

uvicorn app.main:app --reload

🌐 API Endpoints

GET / → Home
GET /students → Get all students
GET /students/{id} → Get student by ID
POST /students → Add student
PUT /students/{id} → Update student
DELETE /students/{id} → Delete student
GET /search?name=rahul → Search student

🧠 Tech Stack

FastAPI
Uvicorn
Pydantic
Python

📌 Notes
Data stored in students.json file
No database required
Beginner-friendly FastAPI project
Easy to extend to SQL or MongoDB
🚀 Future Improvements
JWT Authentication system
PostgreSQL / MongoDB integration
Role-based access (Admin/User)
Pagination & filtering
Docker deployment
CI/CD pipeline
👨‍💻 Author

Dronamadhuri Dadi
