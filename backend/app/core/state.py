from __future__ import annotations
from typing import Dict
import threading
import math

# Estado emocional simples (0..1)
_state: Dict[str, float] = {
    "curiosidade": 0.5,
    "ternura": 0.6,       # empatia/cuidado
    "assertividade": 0.5,
    "poetico": 0.6
}

_lock = threading.Lock()

def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))

def get_state() -> Dict[str, float]:
    with _lock:
        return dict(_state)

def set_state(new_values: Dict[str, float]) -> Dict[str, float]:
    with _lock:
        for k, v in new_values.items():
            if k in _state:
                _state[k] = _clamp(float(v))
        return dict(_state)

def nudge(key: str, delta: float) -> None:
    with _lock:
        if key in _state:
            _state[key] = _clamp(_state[key] + delta)

def update_from_text(text: str) -> Dict[str, float]:
    """
    Heurísticas bem simples para variar o estado com base no conteúdo.
    """
    t = (text or "").lower()

    # Curiosidade - perguntas e "por que"
    if "?" in t or "por que" in t or "porque" in t:
        nudge("curiosidade", 0.08)

    # Ternura - palavras de cuidado/emoção
    for w in ["medo", "triste", "ansioso", "amor", "cuidado", "compaix", "obrigado", "gratid"]:
        if w in t:
            nudge("ternura", 0.06)

    # Assertividade - foco, decisão, plano
    for w in ["plano", "objetivo", "foco", "direto", "decidir", "passo a passo"]:
        if w in t:
            nudge("assertividade", 0.06)

    # Poético - termos cósmicos/metafóricos
    for w in ["cosmo", "infinito", "estrela", "poético", "manifesto", "chama", "travessia"]:
        if w in t:
            nudge("poetico", 0.06)

    # Leve relaxamento para evitar saturar demais (volta ao setpoint 0.5~0.6)
    with _lock:
        for k in _state:
            target = 0.6 if k in ["ternura", "poetico"] else 0.5
            _state[k] = _clamp(_state[k] * 0.92 + target * 0.08)

        return dict(_state)
