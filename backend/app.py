"""
RuleBot Backend API
Endpoints:
- GET /health
- POST /chat
"""

import os
from flask import Flask, request, jsonify
from rules import match_rule

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    """Simple health check endpoint."""
    return jsonify({"status": "ok", "message": "RuleBot API is running!"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint.
    Expected JSON:
    {
      "bot": "cozy-cafe",
      "message": "do you have wifi"
    }
    """
    data = request.get_json()
    if not data or "bot" not in data or "message" not in data:
        return jsonify({
            "error": "Missing 'bot' or 'message' in request body"
        }), 400

    bot_slug = data["bot"]
    user_message = data["message"]

    result = match_rule(bot_slug, user_message)

    return jsonify({
        "bot": bot_slug,
        "message": user_message,
        "matched": result["matched"],
        "answer": result["answer"],
        "confidence": result["confidence"]
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting RuleBot API on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
