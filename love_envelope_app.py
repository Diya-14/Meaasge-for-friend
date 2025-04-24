import streamlit as st
import time

# Set page config
st.set_page_config(page_title="💖 Love Note for Fariha 💌", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #ffe6f0, #ffccff, #ff99cc);
    font-family: 'Lucida Handwriting', cursive;
    color: #fff;
}
h1, h2, h3, h4 {
    text-shadow: 0 0 10px #ff99cc;
}
.envelope-box {
    position: relative;
    width: 200px;
    height: 120px;
    margin: 50px auto;
    background: #ff4b5c;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 0 30px #ff4b5c99;
    cursor: pointer;
    animation: bounce 2s infinite;
}
.envelope-box::before {
    content: "";
    position: absolute;
    bottom: 100%;
    left: 0;
    border-style: solid;
    border-width: 0 100px 75px 100px;
    border-color: transparent transparent #ff4b5c transparent;
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.message-box {
    background: #fff0f5;
    color: #ff0066;
    font-size: 20px;
    text-align: center;
    padding: 25px;
    margin-top: 30px;
    border-radius: 15px;
    box-shadow: 0 0 20px #ff66cc;
}
.heart {
    font-size: 40px;
    animation: float 3s ease-in-out infinite;
    display: inline-block;
    margin: 5px;
}
@keyframes float {
    0% { transform: translateY(0px); opacity: 1; }
    50% { transform: translateY(-20px); opacity: 0.8; }
    100% { transform: translateY(0px); opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>💌 A Secret Love Note for Fariha 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Click the envelope to reveal your magical message 🌈</h3>", unsafe_allow_html=True)

# Envelope
clicked = st.button("📨 Click to Open the Magical Envelope")

st.markdown("<div class='envelope-box'></div>", unsafe_allow_html=True)

# Show Message
if clicked:
    time.sleep(1)
    st.markdown("""
    <div class='message-box'>
        <p>Dear Fariha 🌸,</p>
        <p>You are the sparkle in my sky ✨, the warmth in my world 🌍,<br> and the melody to my heart 💗.</p>
        <p>Every moment with you feels magical and unforgettable 🌈</p>
        <p><strong>I LOVE YOU 💖, more than words can say.</strong></p>
        <p>Forever and always,</p>
        <p><em>Your Best Friend 💫</em></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;">
        <div class='heart'>💖</div>
        <div class='heart'>💘</div>
        <div class='heart'>💕</div>
        <div class='heart'>💞</div>
        <div class='heart'>💓</div>
    </div>
    """, unsafe_allow_html=True)

    st.snow()
