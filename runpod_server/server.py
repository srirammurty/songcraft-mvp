# runpod_server/server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_pipeline import generate_instrumental, generate_vocals, mix_files
import os, shutil

app = FastAPI()

class GenRequest(BaseModel):
    lyrics: str
    style: str = "tollywood upbeat"
    duration: int = 20

@app.post("/api/generate")
def generate(req: GenRequest):
    try:
        # 1) Generate instrumental from style prompt
        music_path = generate_instrumental(req.style + " " + "instrumental", duration=req.duration)
        # 2) Generate vocals from lyrics
        vocals_path = generate_vocals(req.lyrics)
        # 3) Mix
        mix_path = mix_files(music_path, vocals_path)
        fname = os.path.basename(mix_path)
        return {"status":"done", "file": fname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/download/{fname}")
def download(fname: str):
    path = os.path.join(os.path.dirname(__file__), "outputs", fname)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="file not found")
    from fastapi.responses import FileResponse
    return FileResponse(path, media_type="audio/wav", filename=fname)
