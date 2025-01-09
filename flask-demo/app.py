from flask import Flask, request, jsonify

app = Flask(__name__)

# Serve the HTML file
@app.route("/")
def home():
    return app.send_static_file("index.html")

# API route
@app.route("/api", methods=["GET", "POST"])
@app.route("/api/", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        return jsonify({"message": "Use POST to send a message."})

    if request.method == "POST":
        print(f"Headers: {request.headers}")
        print(f"Body: {request.data}")
        data = request.json
        return jsonify({"response": f"You said: {data.get('message', '')}"})
    
        if not request.is_json:
         return jsonify({"error": "Request must be JSON"}), 400

        data = request.json
        message = data.get("message", "")
        return jsonify({"response": f"You said: {message}"})

if __name__ == "__main__":
    app.run(debug=True,port=5000)
