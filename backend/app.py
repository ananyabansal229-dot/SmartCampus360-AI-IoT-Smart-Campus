
from pathlib import Path
import sqlite3

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "smartcampus.db"

app = FastAPI(
    title="Smart Campus 360 API",
    description="Prototype API for campus services and complaints.",
    version="1.0.0",
)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialise_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Received'
            )
        """)


initialise_database()


class ComplaintInput(BaseModel):
    category: str = Field(min_length=2, max_length=60)
    location: str = Field(min_length=2, max_length=120)
    description: str = Field(min_length=5, max_length=1000)


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(BASE_DIR / "frontend" / "index.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "project": "Smart Campus 360"}


@app.get("/api/summary")
def summary():
    with get_connection() as connection:
        total = connection.execute(
            "SELECT COUNT(*) FROM complaints"
        ).fetchone()[0]

        open_count = connection.execute(
            "SELECT COUNT(*) FROM complaints WHERE status != 'Resolved'"
        ).fetchone()[0]

    return {
        "campus": "Smart Campus 360 Demo Campus",
        "electricity_kwh": 1240,
        "water_litres": 8350,
        "waste_bins_alert": 2,
        "air_quality": "Sample reading",
        "total_complaints": total,
        "open_complaints": open_count,
        "data_note": "Illustrative values, not live sensor readings."
    }


@app.get("/api/complaints")
def list_complaints():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM complaints ORDER BY id DESC"
        ).fetchall()

    return [dict(row) for row in rows]


@app.post("/api/complaints", status_code=201)
def create_complaint(complaint: ComplaintInput):
    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO complaints
               (category, location, description)
               VALUES (?, ?, ?)""",
            (
                complaint.category.strip(),
                complaint.location.strip(),
                complaint.description.strip(),
            ),
        )
        complaint_id = cursor.lastrowid

    return {
        "message": "Complaint recorded successfully.",
        "id": complaint_id,
        "status": "Received",
    }


@app.patch("/api/complaints/{complaint_id}/resolve")
def resolve_complaint(complaint_id: int):
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE complaints SET status = 'Resolved' WHERE id = ?",
            (complaint_id,),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Complaint not found")

    return {"id": complaint_id, "status": "Resolved"}
