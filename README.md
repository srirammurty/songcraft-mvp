# songcraft-mvp
Songcraft is a telugu song maker
# SongCraft-MVP

Mini MVP: Flask UI + wrappers to generate instrumental (MusicGen) and vocals (Bark).
Designed to run the heavy models on a cloud GPU (RunPod recommended).

## Quick summary
- Frontend: Flask templates + simple JS
- Model wrappers: `generate_music.py` (MusicGen), `generate_vocals.py` (Bark)
- Hosting: RunPod (GPU) for models; Flask served on same host for simplicity

## Files
- `app.py` - Flask app with endpoints
- `generate_music.py` - MusicGen wrapper
- `generate_vocals.py` - Bark wrapper
- `runpod_setup.sh` - bootstrap script for RunPod (Ubuntu)
- `templates/index.html` - UI
- `static/` - CSS/JS

## How to run (on RunPod / GPU host)
1. Create a RunPod instance (Ubuntu) with an RTX 4090 or similar.
2. SSH into instance.
3. Upload this repo or `git clone` it.
4. Run:
   ```bash
   chmod +x runpod_setup.sh
   ./runpod_setup.sh
   source venv/bin/activate
   # activate the venv inside the script, then:
   gunicorn -b 0.0.0.0:8080 app:app
