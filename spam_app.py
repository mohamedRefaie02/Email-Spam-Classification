

import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("Model.pkl", "rb"))
vectorizer = pickle.load(open("Victorize.pkl", "rb"))

# App UI
st.set_page_config(page_title="Email Spam Classifier", page_icon="📧")
st.title("📧 Email Spam Classifier")
st.write("Type or paste your email message below to check if it's **SPAM** or **NOT SPAM**.")

# Input field
email_text = st.text_area("✉️ Email Message", height=200)

# Button
if st.button("Check Spam"):
    if not email_text.strip():
        st.warning("Please enter an email message.")
    else:
        # Vectorize input and predict
        transformed_text = vectorizer.transform([email_text])
        prediction = model.predict(transformed_text)

        # Display result
        if prediction[0] == 1:
            st.error("🚫 This email **is SPAM**.")
        else:
            st.success("✅ This email **is NOT SPAM**.")
