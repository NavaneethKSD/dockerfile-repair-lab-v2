"""incident-api: a small Flask service for DevOps Foundation LU 4.2.

Run locally without Docker:  pip install -r requirements.txt && python app.py
The app code is correct. Only the Docker packaging is broken.
"""
import os

from flask import Flask, jsonify

from src.incidents import list_incidents, open_count

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/incidents")
def incidents():
    return jsonify(incidents=list_incidents(), open=open_count())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"incident-api listening on 0.0.0.0:{port}", flush=True)
    app.run(host="0.0.0.0", port=port)
