from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json
import threading

BASE_DIR = Path(__file__).resolve().parents[1]
MEM_DIR = BASE_DIR / "memory"
MEM_FILE = MEM_DIR / "chat_history.json"

_lock = threading.Lock()

def _ensure():
    MEM_DIR.mkdir(parents=True, exist_ok=True)
    if not MEM_FILE.exists():
        MEM_FILE.write_text("[]", encoding="utf-8")

def append(user: str, message: str, reply: str) -> None:
    _ensure()
    with _lock:
        data = json.loads(MEM_FILE.read_text(encoding="utf-8"))
        data.append({
            "ts": datetime.now(timezone.utc).isoformat(),
            "user": user,
            "message": message,
            "lilith": reply
        })
        # mantém histórico enxuto (últimos 500)
        data = data[-500:]
        MEM_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def last(n: int = 10) -> list[dict]:
    _ensure()
    with _lock:
        data = json.loads(MEM_FILE.read_text(encoding="utf-8"))
        return data[-n:]

def clear() -> None:
    _ensure()
    with _lock:
        MEM_FILE.write_text("[]", encoding="utf-8")
