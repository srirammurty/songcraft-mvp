# runpod_server/model_pipeline.py
# Simplified wrapper functions: instrument (MusicGen) + vocals (Bark)
import os, uuid, subprocess
from typing import Tuple

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
OUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

def generate_instrumental(prompt: str, duration:int=20) -> str:
    """
    Calls the MusicGen wrapper script (assumes musicgen installed and model accessible).
    Returns path to generated .wav
    """
    out = os.path.join(OUT_DIR, f"{uuid.uuid4().hex}_music.wav")
    # call a script `musicgen_generate.py` or use CLI; here we shell out to a helper
    cmd = f"python3 -u musicgen_generate.py \"{prompt}\" {duration} \"{out}\""
    subprocess.run(cmd, shell=True, check=True)
    return out

def generate_vocals(lyrics: str) -> str:
    out = os.path.join(OUT_DIR, f"{uuid.uuid4().hex}_vocals.wav")
    cmd = f"python3 -u bark_generate.py \"{lyrics}\" \"{out}\""
    subprocess.run(cmd, shell=True, check=True)
    return out

def mix_files(music_path: str, vocals_path: str) -> str:
    # very simple mixing using ffmpeg (music lower volume, vocals louder)
    out = os.path.join(OUT_DIR, f"{uuid.uuid4().hex}_mix.wav")
    cmd = f"ffmpeg -y -i \"{music_path}\" -i \"{vocals_path}\" -filter_complex \"[0:a]volume=0.8[a0];[1:a]volume=1.2[a1];[a0][a1]amix=inputs=2:duration=longest\" \"{out}\""
    subprocess.run(cmd, shell=True, check=True)
    return out
