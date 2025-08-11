# generate_music.py
# Lightweight wrapper for MusicGen (audiocraft)
import os, uuid, sys
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

MODEL = None

def init_model():
    global MODEL
    if MODEL is None:
        # choose "small" for faster & cheaper runs
        MODEL = MusicGen.get_pretrained("small")
    return MODEL

def generate_instrumental(prompt: str, duration: int = 20, out_dir="outputs"):
    model = init_model()
    model.set_generation_params(duration=duration)
    wavs = model.generate([prompt])
    os.makedirs(out_dir, exist_ok=True)
    fname = os.path.join(out_dir, f"{uuid.uuid4().hex}_music.wav")
    audio_write(fname, wavs[0], model.sample_rate)
    return fname

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Tollywood upbeat, tabla and flute, female vocals, tempo 100"
    dur = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    out = generate_instrumental(prompt, duration=dur)
    print(out)
