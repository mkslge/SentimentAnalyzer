from SentimentLexicon import SentimentLexicon

DEFAULT_SENTIMENT_VALUE = 0 #not sure what to put this as rn

ANGER_INDEX = 0
ANTICIPATION_INDEX = 1
DISGUST_INDEX = 2
FEAR_INDEX = 3
JOY_INDEX = 4
SADNESS_INDEX = 5
SURPRISE_INDEX = 6
TRUST_INDEX = 7

EMOTION_LIST = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]
lexicon = SentimentLexicon()


class SentimentVector():

    def __init__(self, word):
        self.word_vector = []
        for emotion in EMOTION_LIST:
            if word in lexicon[emotion]:
                self.word_vector.append(lexicon[emotion][word])
            else:
                self.word_vector.append(DEFAULT_SENTIMENT_VALUE)


    def get_sentiment_vector(self):
        return self.word_vector


    def get_anger_value(self):
        return self.word_vector[ANGER_INDEX]

    def get_anticipation_value(self):
        return self.word_vector[ANTICIPATION_INDEX]

    def get_disgust_value(self):
        return self.word_vector[DISGUST_INDEX]

    def get_fear_value(self):
        return self.word_vector[FEAR_INDEX]

    def get_joy_value(self):
        return self.word_vector[JOY_INDEX]

    def get_sadness_value(self):
        return self.word_vector[SADNESS_INDEX]

    def get_surprise_value(self):
        return self.word_vector[SURPRISE_INDEX]

    def get_trust_value(self):
        return self.word_vector[TRUST_INDEX]