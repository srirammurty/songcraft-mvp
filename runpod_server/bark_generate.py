#!/usr/bin/env python3
"""
bark_generate.py
Simple Bark wrapper.

Usage:
  python3 bark_generate.py "Telugu lyrics here" /path/to/out.wav

Notes:
- Requires the Bark repo installed (git+https://github.com/suno-ai/bark.git)
- Bark will download model assets on first run (several GB). Run on GPU if available.
"""
import sys
import os
import uuid
import time
import traceback

def log(*a, **k):
    print("[bark]", *a, **k, flush=True)

def ensure_dir(p):
    d = os.path.dirname(p)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def main():
    try:
        text = sys.argv[1] if len(sys.argv) > 1 else "నా ప్రేమ పాట"
        out_path = sys.argv[2] if len(sys.argv) > 2 else f"outputs/{uuid.uuid4().hex}_vocals.wav"

        ensure_dir(out_path)
        log("Text:", text)
        log("Output:", out_path)

        # Import Bark API (preload_models + generate_audio)
        # API surface may vary by bark version; this uses the common helpers.
        from bark import SAMPLE_RATE, generate_audio, preload_models
        import numpy as np
        import soundfile as sf

        log("Preloading Bark models (if not already cached)...")
        preload_models()   # this downloads model weights the first time

        t0 = time.time()
        log("Generating audio from text (Bark)...")
        audio_array = generate_audio(text, temp=0.7)  # float32 numpy array (mono)
        if isinstance(audio_array, list):
            # sometimes returns list of arrays
            audio_array = np.concatenate(audio_array, axis=0)

        # Bark returns float32 in range [-1,1] typically
        log("Writing file...")
        sf.write(out_path, audio_array, SAMPLE_RATE, subtype="PCM_16")
        t1 = time.time()
        log(f"Wrote {out_path} (took {t1-t0:.1f}s)")
        print(out_path)
    except Exception as e:
        log("ERROR:", str(e))
        traceback.print_exc()
        sys.exit(2)

if __name__ == "__main__":
    main()
