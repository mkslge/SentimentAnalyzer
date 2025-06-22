from SentimentLexicon import SentimentLexicon
from SentimentVector import SentimentVector

EMOTION_LIST = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]


class SentenceEvaluator:

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.tokenize()
        self.word_vectors = self.get_word_vectors()
        self.sentiment_vectors_sum = self.sum_sentiment_vectors()
        self.sentiment = self.evaluate_sentiment()

    def tokenize(self):
        return self.sentence.split()

    def get_word_vectors(self):
        word_vectors = []
        for word in self.words:
            word_vectors.append(SentimentVector(word))

        return word_vectors

    def sum_sentiment_vectors(self):
        self.sentiment_vectors_sum = {0,0,0,0,0,0,0,0}
        for word_vector in self.word_vectors:
            idx = 0
            for sentiment_value in word_vector.sentiment_values:
                sentiment_value[idx] += sentiment_value
        return self.sentiment_vectors_sum


    def evaluate_sentiment(self):
        max_sentiment_value = 0
        max_idx = 0
        idx = 0
        for sentiment_value in self.sentiment_vectors_sum:
            if max_sentiment_value < sentiment_value:
                max_sentiment_value = sentiment_value
                max_idx = idx
            idx += 1

        return "neutral" if max_sentiment_value == 0 else EMOTION_LIST[max_idx]

    def get_sentiment(self):
        return self.sentiment