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
    student_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    name_to_marks = {student["name"]: student["marks"] for student in student_data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
