from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO
from gtts import gTTS

router = APIRouter()

class TTSIn(BaseModel):
    text: str

@router.post("/tts")
def tts(body: TTSIn):
    # gTTS com sotaque pt-BR (tld com.br)
    tts = gTTS(text=body.text, lang="pt", tld="com.br")
    buf = BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    # retorna MP3 como streaming (para o navegador tocar)
    return StreamingResponse(buf, media_type="audio/mpeg")
