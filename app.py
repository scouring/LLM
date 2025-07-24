from flask import Flask, request, jsonify
from model import generate_response

app = Flask(__name__)

@app.route("/")
def index():
    return "LLM CPU Flask API is running."

@app.route("/generate", methods = ["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400
    
    print(f"Received prompt: {prompt}")
    output = generate_response(prompt)

    return jsonify({
        "prompt": prompt,
        "response": output
    })

if __name__ == "__main__":
    app.run(debug = True)
                      
                      