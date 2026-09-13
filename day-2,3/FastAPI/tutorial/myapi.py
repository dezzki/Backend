from fastapi import FastAPI, Path #basic fast Api 
from typing import Optional # Optional querry in GET method
from pydantic import BaseModel # Create Class template

app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":"19",
        "year":"year 12"
    },
    2:{
        "name":"john2",
        "age":"188",
        "year":"year 2"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year : str

class Update_student(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


@app.get("/")
def index():
    result = []
    for i in students:
        result.append(students[i])
    return result

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the Student you want", gt=0, lt=10)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_by_name(*, student_id: int, name : Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student Already Created"}

    students[student_id] = student.model_dump()
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Update_student):
    if student_id not in students:
        return {"Error": "Student Does Not exist"}

    if student.name != None:
        students[student_id]["name"] = student.name
        
    if student.age != None:
        students[student_id]["age"] = student.age

    if student.year != None:
        students[student_id]["year"] = student.year

    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Does Not exist"}

    del students[student_id]
    return {"Message": "Student Deleted Successfully"}