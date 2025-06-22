import numpy as np
import pandas as pd

NRC_EMOTION_FILE_PATH = "sentiment_data/NRC-Emotion-Lexicon/OneFilePerEmotion/"
NRC_EMOTION_FILE_PATH_POSTFIX = "-NRC-Emotion-Lexicon.txt"
EMOTION_LIST = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]



class SentimentLexicon():


    def __init__(self):
        self.lexicon = []
        for emotion in EMOTION_LIST:
            self.lexicon.append(self.load_emotion_from_lexicon(emotion))



    def load_emotion_from_lexicon(self, emotion: str) -> dict[str, int]:
        return self.load_nrc_lexicon(NRC_EMOTION_FILE_PATH + emotion + NRC_EMOTION_FILE_PATH_POSTFIX)

    def load_nrc_lexicon(self, filepath: str) -> dict[str, int]:
        hashmap: dict[str, int] = {}

        with open(filepath, encoding='utf8') as file:
            for line in file:

                line = line.strip()
                line = line.split('\t')
                print(line)

                word = str(line[0])
                emotion_value = int(line[1])
                hashmap[word] = emotion_value

        return hashmap

    def get_lexicon_value(self, word: str, emotion_index) -> int:
        return self.lexicon