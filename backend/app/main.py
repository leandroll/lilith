from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.chat import router as chat_router
from .routes.tts import router as tts_router
from .routes.state import router as state_router

app = FastAPI(title="Lilith API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api", tags=["chat"])
app.include_router(tts_router, prefix="/api", tags=["voice"])
app.include_router(state_router, prefix="/api", tags=["mind"])

@app.get("/")
def root():
    return {"hello": "Lilith", "docs": "/docs"}
