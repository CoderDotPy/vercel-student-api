from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open("data.json") as f:
    student_data = json.load(f)

@app.get("/api")
def get_marks(request: Request):  # ← FIXED: request parameter added
    names = request.query_params.getlist("name")
    print("Query names:", names)
    name_to_marks = {student["name"]: student["marks"] for student in student_data}
    result = [name_to_marks.get(n) for n in names]
    print("Result:", result)
    return {"marks": result}
