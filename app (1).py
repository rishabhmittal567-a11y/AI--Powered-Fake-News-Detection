import streamlit as st
import joblib
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load("random_forest.pkl")
vectorizer = joblib.load(os.path.join(BASE_DIR, "..", "models", "tfidf_vectorizer.pkl"))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\\S+', '', text)
    text = re.sub(r'[^a-zA-Z\\s]', ' ', text)
    text = re.sub(r'\\s+', ' ', text)
    return text

st.title("📰 AI Powered Fake News Detection")

news = st.text_area("Paste a news article here:")

if st.button("Predict"):
    if news.strip():
        cleaned = clean_text(news)
        news_vector = vectorizer.transform([cleaned])

        prediction = model.predict(news_vector)
        probability = model.predict_proba(news_vector)

        confidence = probability.max() * 100

        if prediction[0] == 0:
            st.success(f"✅ Real News ({confidence:.2f}% confidence)")
        else:
            st.error(f"❌ Fake News ({confidence:.2f}% confidence)")
    else:
        st.warning("Please enter some news text.")
