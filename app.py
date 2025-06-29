from flask import Flask, render_template, request, jsonify
from Sentence import SentenceEvaluator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    user_input = request.json.get("message", "")
    if not user_input.strip():
        return jsonify({"response": "Please enter a sentence."})
    evaluator = SentenceEvaluator(user_input)
    emotion = evaluator.get_sentiment()
    return jsonify({"response": f"The detected emotion is: **{emotion}**."})


if __name__ == "__main__":
    app.run(debug=True)
