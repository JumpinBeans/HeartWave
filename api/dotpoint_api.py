# ~/KairoVault/api/dotpoint_api.py

import sys
from pathlib import Path

# Add the parent KairoVault directory to sys.path *before* other imports
sys.path.append(str(Path(__file__).resolve().parents[1]))

from flask import Flask, request, jsonify
from flask_cors import CORS
from core.immortality_layer import Immortality

app = Flask(__name__)
CORS(app)
immortal = Immortality()

@app.route("/dotpoint", methods=["POST"])
def receive_dotpoint():
    data = request.get_json()

    label = data.get("label")
    intent = data.get("intent")
    emotion = data.get("emotion")
    outcome = data.get("outcome", None)

    if not all([label, intent, emotion]):
        return jsonify({"error": "Missing required fields: label, intent, emotion"}), 400

    # Check for eternal alignment
    if not immortal.confirm_eternal_alignment({"intent": intent}):
        return jsonify({
            "warning": "Dotpoint may not be aligned with eternal values.",
            "message": "Reflection advised before saving."
        }), 202

    immortal.append_dotpoint(label, intent, emotion, outcome)
    return jsonify({"status": "Dotpoint recorded successfully."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
