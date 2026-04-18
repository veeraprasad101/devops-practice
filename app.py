from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps System Monitoring App 🚀"

@app.route("/health")
def health():
    return jsonify({
        "uptime": os.popen("uptime").read(),
        "disk": os.popen("df -h").read(),
        "memory": os.popen("free -m").read()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
