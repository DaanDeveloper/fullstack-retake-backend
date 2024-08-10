from fastapi import APIRouter
import database
from queries import r0986005_queries
from models import r0986005_models
from datetime import datetime

app = APIRouter()

@app.post("/submitContact")
def submit_contact_message(contact_message: r0986005_models.ContactMessage):
    query = r0986005_queries.insert_contact_message
    submitted_at = datetime.now() if not contact_message.submitted_at else contact_message.submitted_at
    success = database.execute_sql_query(query, (
        contact_message.name,
        contact_message.email,
        contact_message.subject,
        contact_message.message,
        submitted_at
    ))
    if isinstance(success, Exception):
        return {"error": str(success)}, 500

    return {"message": "Contact message submitted successfully"}
