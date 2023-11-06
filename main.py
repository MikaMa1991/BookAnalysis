import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
import plotly.express as px

filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()
pos = []
neg = []
dates = []

for filepath in filepaths:
    with open(filepath) as file:
        lines = file.read()
    scores = analyzer.polarity_scores(lines)
    pos.append(scores['pos'])
    neg.append(scores['neg'])
    dates.append(filepath.strip(".txt").strip("diary/"))

st.title("Diary Tone")
st.subheader("Positivity")
fig = px.line(x = dates, y=pos, labels = {"x": "Date", "y":"Positivity"})
st.plotly_chart(fig)
st.subheader("Negativity")
fig = px.line(x = dates, y=neg, labels = {"x": "Date", "y":"Negativity"})
st.plotly_chart(fig)

