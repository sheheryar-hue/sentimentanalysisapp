import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# 🌌 Gradient + grid + animated diagonal blur
st.markdown("""
    <style>
    .stApp {
        background: 
            linear-gradient(to bottom right, #1f1c2c, #3e2f2f),
            repeating-linear-gradient(
                0deg,
                rgba(0, 0, 0, 0.15) 0px,
                rgba(0, 0, 0, 0.15) 1px,
                transparent 1px,
                transparent 10px
            ),
            repeating-linear-gradient(
                90deg,
                rgba(0, 0, 0, 0.15) 0px,
                rgba(0, 0, 0, 0.15) 1px,
                transparent 1px,
                transparent 10px
            );
        background-blend-mode: overlay;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    .main-card {
        position: relative;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        overflow: hidden;
        margin-top: 30px;
    }

    .main-card::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.05) 0%,
            rgba(255, 255, 255, 0.2) 50%,
            rgba(255, 255, 255, 0.05) 100%
        );
        animation: moveLight 6s linear infinite;
        filter: blur(10px);
        pointer-events: none;
    }

    @keyframes moveLight {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    h1, h2, h3, h4, h5, h6, p, label, textarea, .css-10trblm, .css-1cpxqw2 {
        color: white !important;
    }

    .stTextArea textarea {
        background-color: #2e2e2e;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🧹 Text Cleaner
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 🌌 App UI inside glass panel
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("🌌 Sentiment Analysis App")
st.write("Enter your review below:")

user_input = st.text_area("📝 Your Review")

if st.button("🔍 Analyze"):
    cleaned = clean_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

if prediction == "positive":
        st.success("✅ Positive Sentiment 😊")
        st.markdown("""
            <audio autoplay>
              <source src="https://assets.mixkit.co/sfx/preview/mixkit-achievement-bell-600.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)
else:
        st.error("❌ Negative Sentiment 😞")
        st.markdown("""
            <audio autoplay>
              <source src="https://assets.mixkit.co/sfx/preview/mixkit-sad-game-over-trombone-471.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)




