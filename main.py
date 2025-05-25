from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data.json") as f:
    student_data = json.load(f)
    print(f"Loaded {len(student_data)} students")

@app.get("/api")
def get_marks(name: list[str] = []):
    names = request.query_params.getlist("name")
    print("Query names:", names)
    name_to_marks = {student["name"]: student["marks"] for student in student_data}
    result = [name_to_marks.get(n) for n in names]
    print("Result:", result)
    return {"marks": result}
