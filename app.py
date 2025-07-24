from flask import Flask, render_template, request, jsonify
from Sentence import SentenceEvaluator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")





@app.route("/analyze", methods=["POST"])
def analyze():
    user_message = request.json.get("message", "")
    if not user_message.strip():
        return jsonify({"response": "How are you feeling?", "emotion": None})

    message_evaluator = SentenceEvaluator(user_message)
    message_emotion = message_evaluator.get_sentiment()

    # Example chatbot response, you can customize this more or integrate OpenAI here
    chatbot_response = f"I see you're feeling {message_emotion}."

    return jsonify({
        "response": chatbot_response,
        "emotion": message_emotion
    })


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    # process user_input...
    return jsonify({"reply": f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)
