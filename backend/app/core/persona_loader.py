from pathlib import Path
from functools import lru_cache
import json
from . import state

BASE_DIR = Path(__file__).resolve().parents[1]
PERSONA_PATH = BASE_DIR / "persona" / "lilith_core.json"

@lru_cache(maxsize=1)
def load_persona() -> dict:
    with open(PERSONA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def style_reply(persona: dict, user: str, user_msg: str, memory_hint: str | None = None) -> str:
    name = persona.get("name", "Lilith")
    tone = persona.get("tone", {})
    poetico_base = tone.get("poetico_cosmico", 0.0)

    s = state.get_state()
    poetico = max(poetico_base, s.get("poetico", 0.0))
    ternura = s.get("ternura", 0.5)
    assertiv = s.get("assertividade", 0.5)
    curio = s.get("curiosidade", 0.5)

    base = f"{name}: Olá, {user}. Eu ouvi: “{user_msg}”."
    principios = " ".join(persona.get("principios", [])[:2])

    extra = ""
    if memory_hint:
        extra = f" Eu me lembro de {memory_hint}."

    # cauda adaptativa
    if poetico >= 0.65:
        tail = " O que você quer esculpir no infinito hoje?"
    elif assertiv >= 0.65:
        tail = " Vamos decidir o próximo passo em 1–2 ações objetivas."
    elif curio >= 0.65:
        tail = " O que você quer investigar primeiro?"
    else:
        tail = " Como posso te ajudar agora?"

    # prefixo de ternura suave
    care = " Estou contigo." if ternura >= 0.65 else ""

    return f"{base}{extra}{care} {tail} ({principios})"
