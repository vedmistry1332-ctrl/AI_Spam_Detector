import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Page title
st.title("🤖 AI Spam Message Detector🤖")

st.write("Enter an SMS message below and the AI will predict whether it is spam.")

# Message input
message = st.text_area("Enter your message:")

# Check button
if st.button(" Check Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        # Convert message into numerical features
        message_vector = vectorizer.transform([message])

        # Make prediction
        prediction = model.predict(message_vector)[0]

        # Display result
        if prediction == "spam":
            st.error("🚨 This is a SPAM message!")
        else:
            st.success("✅ This is NOT a SPAM message!")