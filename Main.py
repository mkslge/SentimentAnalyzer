import numpy as np
import pandas as pd

from SentimentLexicon import SentimentLexicon
from Sentence import SentenceEvaluator

sentiment = SentimentLexicon()


sentence = "I am very angelic"
sentence_evaluator = SentenceEvaluator(sentence)
print(sentence_evaluator.get_sentiment())

