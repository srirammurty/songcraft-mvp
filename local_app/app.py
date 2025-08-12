# local_app/app.py
# Minimal Flask UI that calls RunPod server
from flask import Flask, render_template, request, jsonify
import requests, os, json

app = Flask(__name__)
# change to your RunPod server URL (update after you run server on RunPod)
RUNPOD_API = os.environ.get("RUNPOD_API", "http://<RUNPOD_IP>:8000")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    body = request.json
    # forward request to RunPod server
    resp = requests.post(f"{RUNPOD_API}/api/generate", json=body, timeout=600)
    return jsonify(resp.json()), resp.status_code

@app.route("/download/<path:fname>")
def download(fname):
    # local proxy to download from runpod (optional)
    r = requests.get(f"{RUNPOD_API}/api/download/{fname}", stream=True)
    return (r.content, r.status_code, r.headers.items())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
