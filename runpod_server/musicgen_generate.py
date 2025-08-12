#!/usr/bin/env python3
"""
musicgen_generate.py
Simple MusicGen (AudioCraft) wrapper.

Usage:
  python3 musicgen_generate.py "Tollywood upbeat, tabla and flute" 20 /path/to/out.wav

Notes:
- This script expects audiocraft (MusicGen) and a compatible torch installed.
- Run on GPU for reasonable speed.
"""
import sys
import os
import uuid
import time
import traceback

def log(*a, **k):
    print("[musicgen]", *a, **k, flush=True)

def ensure_dir(p):
    d = os.path.dirname(p)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def main():
    try:
        prompt = sys.argv[1] if len(sys.argv) > 1 else "Tollywood upbeat, tabla and flute"
        duration = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        out_path = sys.argv[3] if len(sys.argv) > 3 else f"outputs/{uuid.uuid4().hex}_music.wav"

        ensure_dir(out_path)
        log("Prompt:", prompt)
        log("Duration:", duration, "sec")
        log("Output:", out_path)

        # Import here so that errors are visible at runtime
        from audiocraft.models import MusicGen
        from audiocraft.data.audio import audio_write
        import torch

        log("Torch version:", torch.__version__, "CUDA available:", torch.cuda.is_available())
        t0 = time.time()

        # load model (small is faster & cheaper)
        log("Loading MusicGen model (this may take a minute on first run)...")
        model = MusicGen.get_pretrained("small")   # small -> faster dev
        sr = getattr(model, "sample_rate", 32000)
        log("Model sample_rate:", sr)

        model.set_generation_params(duration=duration)  # seconds
        log("Generating...")
        wavs = model.generate([prompt])  # returns numpy array (n, L)
        wav = wavs[0]
        log("Generation done. Writing audio...")
        audio_write(out_path, wav, sr)
        t1 = time.time()
        log(f"Wrote {out_path} (took {t1-t0:.1f}s)")
        print(out_path)
    except Exception as e:
        log("ERROR:", str(e))
        traceback.print_exc()
        sys.exit(2)

if __name__ == "__main__":
    main()
