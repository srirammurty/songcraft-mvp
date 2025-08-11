# generate_vocals.py
import os, uuid, sys
from scipy.io.wavfile import write as write_wav
from bark import SAMPLE_RATE, generate_audio, preload_models

def init_bark():
    preload_models()

def generate_vocals(text: str, out_dir="outputs"):
    init_bark()
    # bark's generate_audio returns float32 numpy array
    audio_array = generate_audio(text)
    os.makedirs(out_dir, exist_ok=True)
    fname = os.path.join(out_dir, f"{uuid.uuid4().hex}_vocals.wav")
    write_wav(fname, SAMPLE_RATE, audio_array)
    return fname

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "నా ప్రేమ పాట"
    out = generate_vocals(text)
    print(out)
