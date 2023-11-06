import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

filenames = os.listdir("diary")
analyzer = SentimentIntensityAnalyzer()
pos = []
neg = []
for filename in filenames
    with open(f"diary/{filename}") as file:
        lines = file.read()
    scores = analyzer.polarity_scores(lines)
    pos.append(scores['pos'])
    neg.append(scores['neg'])


