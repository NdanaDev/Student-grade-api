# Student Grade API — Project Report

**Date:** March 22, 2026
**Project:** Student Grade API
**Language/Framework:** Python / Flask

---

## 1. Overview

The Student Grade API is a lightweight RESTful web service built with Python and Flask. It provides endpoints to manage student grade records, allowing clients to retrieve all students, look up a specific student by ID, and add new students. The API also integrates Swagger UI via Flasgger, enabling interactive, browser-based documentation and testing.

---

## 2. Project Structure

```
student-grade-api/
├── app.py              # Main application file containing all routes and logic
└── requirements.txt    # Python package dependencies
```

---

## 3. Technology Stack

| Component        | Technology         | Version  |
|------------------|--------------------|----------|
| Language         | Python             | 3.x      |
| Web Framework    | Flask              | 3.1.3    |
| API Docs         | Flasgger (Swagger) | —        |
| WSGI Toolkit     | Werkzeug           | 3.1.6    |
| Templating       | Jinja2             | 3.1.6    |

---

## 4. API Endpoints

### `GET /`
**Health Check**
Returns a simple message confirming the API is running.

- **Response 200:** `{ "message": "Student Grades API is running" }`

---

### `GET /students`
**Get All Students**
Returns the full list of student records currently in memory.

- **Response 200:** JSON array of student objects

**Example response:**
```json
[
  { "id": 1, "name": "Alice", "course": "Math", "grade": 90 },
  { "id": 2, "name": "Bob",   "course": "Science", "grade": 85 }
]
```

---

### `POST /students`
**Add a New Student**
Accepts a JSON body and appends a new student record to the in-memory list.

**Required fields:**
| Field    | Type    | Example   |
|----------|---------|-----------|
| `name`   | string  | "Charlie" |
| `course` | string  | "History" |
| `grade`  | integer | 88        |

- **Response 201:** The newly created student object (including auto-assigned `id`)
- **Response 400:** Validation error (missing fields, non-JSON body, or non-integer grade)

**Validation rules enforced:**
- Request body must be valid JSON
- All three fields (`name`, `course`, `grade`) must be present
- `grade` must be an integer

---

### `GET /students/<id>`
**Get a Student by ID**
Looks up and returns a single student record by their integer ID.

- **Response 200:** The matching student object
- **Response 404:** `{ "error": "Student not found" }`

---

## 5. Data Storage

Data is stored **in-memory** as a Python list of dictionaries. The application ships with two pre-seeded records:

```python
students = [
    {"id": 1, "name": "Alice",  "course": "Math",    "grade": 90},
    {"id": 2, "name": "Bob",    "course": "Science",  "grade": 85}
]
```

> **Note:** Because storage is in-memory only, all data added at runtime is lost when the server restarts. A future improvement would be to integrate a persistent database (e.g., SQLite, PostgreSQL).

---

## 6. API Documentation

The project uses **Flasgger** to auto-generate a Swagger UI from inline YAML docstrings on each route. When the server is running, the interactive documentation is accessible at:

```
http://127.0.0.1:5000/apidocs
```

This allows developers and testers to explore and call each endpoint directly from a browser without needing an external tool like Postman.

---

## 7. Running the Project

**Install dependencies:**
```bash
pip install -r requirements.txt
pip install flasgger
```

**Start the server:**
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000` with debug mode enabled.

---

## 8. Limitations & Potential Improvements

| Limitation                          | Suggested Improvement                              |
|-------------------------------------|----------------------------------------------------|
| In-memory data storage              | Integrate a database (SQLite, PostgreSQL)          |
| No data persistence across restarts | Use an ORM such as SQLAlchemy                      |
| No update or delete endpoints       | Add `PUT /students/<id>` and `DELETE /students/<id>` |
| ID assignment can produce duplicates on deletion | Use UUID or auto-increment from a DB     |
| No input sanitization on string fields | Add length/type validation for `name` and `course` |
| Duplicate import statements in `app.py` | Clean up redundant `from flask import` lines    |
| Debug mode enabled in production   | Use an environment variable to control debug mode  |

---

## 9. Conclusion

The Student Grade API is a functional and well-structured beginner-to-intermediate Flask project. It demonstrates core REST API concepts including route handling, JSON request/response cycles, input validation, and auto-generated API documentation with Swagger. With a persistent database and a few additional endpoints, it could serve as a solid foundation for a full student records management system.
