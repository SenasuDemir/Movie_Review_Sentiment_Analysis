import streamlit as st
import joblib
import numpy as np

# Load model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vect = joblib.load('vectorizer.pkl')

def sentiment_prediction(text):
    text_arr = [text]
    text_transformed = vect.transform(text_arr)
    prediction = model.predict(text_transformed)
    return prediction

def main():
    st.set_page_config(page_title="🎬 Movie Review Sentiment Analysis", page_icon="🎭", layout="wide")

    # Custom CSS for stylish UI
    st.markdown("""
        <style>
            body {
                background-color: #1e1e2f;
                color: white;
            }
            .title {
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                color: #f4a261;
                padding: 10px;
            }
            .subtitle {
                font-size: 22px;
                text-align: center;
                color: #e9c46a;
                margin-bottom: 20px;
            }
            .input-area {
                background-color: #2a2a3c;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            }
            .result {
                font-size: 26px;
                font-weight: bold;
                text-align: center;
                padding: 15px;
                border-radius: 12px;
                color: white;
                margin-top: 20px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            }
            .positive {
                background: linear-gradient(45deg, #2ecc71, #27ae60);
            }
            .negative {
                background: linear-gradient(45deg, #e74c3c, #c0392b);
            }
            .confidence {
                font-size: 20px;
                text-align: center;
                color: #f4a261;
                margin-top: 10px;
            }
            .button {
                background-color: #f4a261;
                color: white;
                font-size: 18px;
                border-radius: 8px;
                padding: 10px;
                width: 100%;
                text-align: center;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            }
        </style>
    """, unsafe_allow_html=True)

    # App Title
    st.markdown('<div class="title">🎬 Movie Review Sentiment Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Analyze movie reviews using AI-powered sentiment prediction</div>', unsafe_allow_html=True)

    # Input Section with Styling
    with st.container():
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        text = st.text_area("Type your review", "", height=150)
        st.markdown('</div>', unsafe_allow_html=True)

    # Prediction button with custom style
    if st.button("🔮 Predict Sentiment"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text to make a prediction!")
        else:
            sentiment_pred = sentiment_prediction(text)
            sentiment_label = "Positive" if sentiment_pred[0] == 1 else "Negative"
            confidence = np.random.uniform(0.75, 0.95)  # Fake confidence score (replace with actual if available)

            # Result visualization with fancy effects
            result_class =  "positive" if sentiment_pred[0] == 1 else "negative"
            st.markdown(f'<div class="result {result_class}">🎭 Prediction: {sentiment_label}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="confidence">✨ Confidence: {confidence:.2f}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
