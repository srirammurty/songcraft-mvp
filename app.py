# app.py
from flask import Flask, request, jsonify, render_template, send_file
import threading, subprocess, uuid, os, time

app = Flask(__name__)
JOBS = {}

def run_job(cmd, job_id):
    JOBS[job_id] = {"status":"running","started":time.time()}
    try:
        proc = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out = proc.stdout.strip().splitlines()[-1]
        JOBS[job_id].update({"status":"done","out_file":out})
    except subprocess.CalledProcessError as e:
        JOBS[job_id].update({"status":"error","error": e.stderr})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate/instrumental", methods=["POST"])
def generate_instrumental():
    data = request.json or {}
    prompt = data.get("prompt", "Tollywood upbeat, tabla and flute")
    duration = int(data.get("duration", 20))
    job_id = uuid.uuid4().hex
    cmd = f"python3 generate_music.py \"{prompt}\" {duration}"
    thread = threading.Thread(target=run_job, args=(cmd, job_id))
    thread.start()
    return jsonify({"job_id": job_id}), 202

@app.route("/api/generate/vocals", methods=["POST"])
def generate_vocals():
    data = request.json or {}
    text = data.get("text", "నా ప్రేమ పాట")
    job_id = uuid.uuid4().hex
    cmd = f"python3 generate_vocals.py \"{text}\""
    thread = threading.Thread(target=run_job, args=(cmd, job_id))
    thread.start()
    return jsonify({"job_id": job_id}), 202

@app.route("/api/job/<job_id>")
def job_status(job_id):
    return jsonify(JOBS.get(job_id, {"status":"unknown"}))

@app.route("/download/<job_id>")
def download(job_id):
    job = JOBS.get(job_id)
    if not job or job.get("status") != "done":
        return "not ready", 404
    return send_file(job["out_file"], as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
