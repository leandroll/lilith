from fastapi import APIRouter
from pydantic import BaseModel
from ..core import state

router = APIRouter()

class SetStateIn(BaseModel):
    curiosidade: float | None = None
    ternura: float | None = None
    assertividade: float | None = None
    poetico: float | None = None

@router.get("/state")
def get_state():
    return {"state": state.get_state()}

@router.post("/state")
def set_state(body: SetStateIn):
    data = {k: v for k, v in body.model_dump().items() if v is not None}
    updated = state.set_state(data)
    return {"state": updated}
