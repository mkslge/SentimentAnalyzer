from flask import Flask, render_template, request, jsonify
from Sentence import SentenceEvaluator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")





@app.route("/analyze", methods=["POST"])
def analyze():
    user_message = request.json.get("message", "")
    if not user_message.strip():
        return jsonify({"response": "How are you feeling?"})

    message_evaluator = SentenceEvaluator(user_message)
    message_emotion = message_evaluator.get_sentiment()
    return jsonify({"response": f"I see you're feeling {message_emotion}"})


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    # process user_input...
    return jsonify({"reply": f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)
