from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":"19",
        "class":"year 12"
    },
    2:{
        "name":"john2",
        "age":"188",
        "class":"year 2"
    }
}

@app.get("/")
def index():
    return {"name" : "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the Student you want", gt=0, lt=3)):
    return students[student_id]