from flask import Flask, jsonify, request
from flask import Flask, jsonify

from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

students = [
    {"id": 1, "name": "Alice", "course": "Math", "grade": 90},
    {"id": 2, "name": "Bob", "course": "Science", "grade": 85}
]

@app.route("/")
def home():
    """
    Health check
    ---
    responses:
      200:
        description: API is running
    """
    return jsonify({"message": "Student Grades API is running"})

@app.route("/students", methods=["GET"])
def get_students():
    """
    Get all students
    ---
    responses:
      200:
        description: A list of students
    """
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    """
    Add a new student
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - course
            - grade
          properties:
            name:
              type: string
              example: Charlie
            course:
              type: string
              example: History
            grade:
              type: integer
              example: 88
    responses:
      201:
        description: Student created successfully
      400:
        description: Invalid input
    """
    data = request.get_json()

    # check if request body exists
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # validation
    if "name" not in data or "course" not in data or "grade" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(data["grade"], int):
        return jsonify({"error": "Grade must be a number"}), 400

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"],
        "grade": data["grade"]
    }

    students.append(new_student)

    return jsonify(new_student), 201

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    """
    Get a student by ID
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The student ID
    responses:
      200:
        description: A single student
      404:
        description: Student not found
    """
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)