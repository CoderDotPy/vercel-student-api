from fastapi import FastAPI, Query
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
    data = json.load(f)
    student_data = data["students"]

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {student["name"]: student["marks"] for student in student_data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
