#!/usr/bin/env bash
# run on the RunPod instance after models installed
# activate your venv first
# source venv/bin/activate
uvicorn server:app --host 0.0.0.0 --port 8000 --workers 1
