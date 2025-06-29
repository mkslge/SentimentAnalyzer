from SentimentLexicon import SentimentLexicon
from Sentence import SentenceEvaluator

EMOTION_LIST = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]

neutral_sentence = "This is a random string"
angry_sentence = "I hate you"
anticipation_sentence = "I can't wait for the big day"
disgust_sentence = "maggot"
fear_sentence = "terror"
joy_sentence = "I personally think you are angelic"
sadness_sentence = "remove"
surprise_sentence = "suddenly"
trust_sentence = "I know I can count on you no matter what."

neutral_evaluator = SentenceEvaluator(neutral_sentence)
angry_evaluator = SentenceEvaluator(angry_sentence)
anticipation_evaluator = SentenceEvaluator(anticipation_sentence)
disgust_evaluator = SentenceEvaluator(disgust_sentence)
fear_evaluator = SentenceEvaluator(fear_sentence)
joy_evaluator = SentenceEvaluator(joy_sentence)
sadness_evaluator = SentenceEvaluator(sadness_sentence)
surprise_evaluator = SentenceEvaluator(surprise_sentence)
trust_evaluator = SentenceEvaluator(trust_sentence)

neutral_evaluation = neutral_evaluator.evaluate_sentiment()
angry_evaluation = angry_evaluator.evaluate_sentiment()
anticipation_evaluation = anticipation_evaluator.evaluate_sentiment()
disgust_evaluation = disgust_evaluator.evaluate_sentiment()
fear_evaluation = fear_evaluator.evaluate_sentiment()
joy_evaluation = joy_evaluator.evaluate_sentiment()
sadness_evaluation = sadness_evaluator.evaluate_sentiment()
surprise_evaluation = surprise_evaluator.evaluate_sentiment()
trust_evaluation = trust_evaluator.evaluate_sentiment()

if neutral_evaluation == "neutral":
    print("Neutral Test Passed!")
else:
    print(f"Neutral Test Failed, {neutral_evaluation} != neutral!")

if angry_evaluation == "anger":
    print("Angry Test Passed!")
else:
    print(f"Angry Test Failed, {angry_evaluation} != anger!")

if anticipation_evaluation == "anticipation":
    print("Anticipation Test Passed!")
else:
    print(f"Anticipation Test Failed, {anticipation_evaluation} != anticipation!")

if disgust_evaluation == "disgust":
    print("Disgust Test Passed!")
else:
    print(f"Disgust Test Failed, {disgust_evaluation} != disgust!")

if fear_evaluation == "fear":
    print("Fear Test Passed!")
else:
    print(f"Fear Test Failed, {fear_evaluation} != fear!")

if joy_evaluation == "joy":
    print("Joy Test Passed!")
else:
    print(f"Joy Test Failed, {joy_evaluation} != joy!")

if sadness_evaluation == "sadness":
    print("Sadness Test Passed!")
else:
    print(f"Sadness Test Failed, {sadness_evaluation} != sadness!")

if surprise_evaluation == "surprise":
    print("Surprise Test Passed!")
else:
    print(f"Surprise Test Failed, {surprise_evaluation} != surprise!")

if trust_evaluation == "trust":
    print("Trust Test Passed!")
else:
    print(f"Trust Test Failed, {trust_evaluation} != trust!")
