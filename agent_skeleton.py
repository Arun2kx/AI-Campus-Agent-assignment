from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any

app = FastAPI(title="AI Campus Agent")

# --- Models ---
class UserMessage(BaseModel):
    user_id: str
    text: str

class IntentResponse(BaseModel):
    intent: str
    confidence: float
    entities: Dict[str, Any] = {}

class AvailabilityQuery(BaseModel):
    resource_id: str
    start_iso: str
    end_iso: str

class BookingRequest(BaseModel):
    user_id: str
    resource_id: str
    start_iso: str
    end_iso: str
    purpose: Optional[str]

# --- Placeholder NLU (to be replaced with real model) ---
def simple_intent_classifier(text: str) -> IntentResponse:
    text_low = text.lower()
    if "book" in text_low or "reserve" in text_low:
        return IntentResponse(intent="booking", confidence=0.95)
    if "event" in text_low or "what's on" in text_low:
        return IntentResponse(intent="events", confidence=0.9)
    if "facility" in text_low or "room" in text_low:
        return IntentResponse(intent="facilities", confidence=0.9)
    return IntentResponse(intent="unknown", confidence=0.6)

# --- Endpoints ---
@app.post("/parse_intent", response_model=IntentResponse)
async def parse_intent(msg: UserMessage):
    # call to NLU pipeline (embedding + classifier + entity extraction)
    intent = simple_intent_classifier(msg.text)
    return intent

@app.post("/check_availability")
async def check_availability(q: AvailabilityQuery):
    # Adapter would query campus booking system or DB
    # Here we return a mock response
    return {"resource_id": q.resource_id, "start": q.start_iso, "end": q.end_iso, "available": True}

@app.post("/request_booking")
async def request_booking(req: BookingRequest):
    # Orchestrator path:
    # 1) parse intent & entities
    # 2) check availability via adapter
    # 3) validate constraints
    # 4) ask for confirmation (not implemented here)
    # 5) on confirmation, execute booking transaction

    # Simulate pre-check
    availability = True
    if not availability:
        raise HTTPException(status_code=409, detail="Resource not available")

    # IMPORTANT: must confirm with user BEFORE performing booking
    return {"status": "pending_confirmation", "message": "Please confirm booking to proceed"}

@app.post("/confirm_booking")
async def confirm_booking(req: BookingRequest, confirm: bool = True):
    # In production: verify user identity, permissions, re-check availability and constraints atomically
    if not confirm:
        return {"status": "cancelled"}
    # perform transactional booking (mock)
    booking_id = "BK-123456"
    # emit notification events, store audit log, return booking id
    return {"status": "booked", "booking_id": booking_id}

# Minimal run instructions:
# uvicorn agent_skeleton:app --reload --host 0.0.0.0 --port 8000
