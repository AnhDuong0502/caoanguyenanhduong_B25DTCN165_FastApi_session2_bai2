from fastapi import FastAPI

app = FastAPI()
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students[student_id - 1]
