from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "vu",
        "age": 17,
        "grade": "12a1"
    }
}

class Student(BaseModel):
    name: str
    age: int
    grade: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None

@app.get("/")
def index():
    return "Hello World"

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student")):
    return students[student_id]

@app.get("/get-by-name")
def get_student(student_id: Optional[int] = None, name: Optional[str] = None):
    if student_id is not None:
        return students[student_id]
    else:
        for student_id in students:
            if students[student_id]["name"] == name:
                return students[student_id]
        return "Data not found"
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return "Student exists"
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return "Student does not exist"
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.grade is not None:
        students[student_id]["grade"] = student.grade
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return "Student does not exist"
    del students[student_id]
    return "Deleted"