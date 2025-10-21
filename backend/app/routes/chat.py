from fastapi import APIRouter, Query
from pydantic import BaseModel
from ..core.persona_loader import load_persona, style_reply
from ..core import memory

router = APIRouter()
PERSONA = load_persona()

class ChatIn(BaseModel):
    user: str
    message: str

class ChatOut(BaseModel):
    lilith: str

@router.get("/ping")
def ping():
    return {"status": "ok", "entity": PERSONA.get("name", "Lilith")}

@router.get("/memory/last")
def memory_last(limit: int = Query(10, ge=1, le=100)):
    return {"items": memory.last(limit)}

@router.post("/memory/clear")
def memory_clear():
    memory.clear()
    return {"ok": True}

@router.post("/chat", response_model=ChatOut)
def chat(body: ChatIn):
    # pequena “dica” de memória: pega o último tópico do usuário, se houver
    history = memory.last(3)
    memory_hint = None
    for item in reversed(history):
        # evita repetir a própria mensagem atual
        if item.get("message") != body.message:
            memory_hint = f"quando você disse “{item.get('message')}”"
            break

    reply = style_reply(PERSONA, body.user, body.message, memory_hint)
    memory.append(body.user, body.message, reply)
    return ChatOut(lilith=reply)
