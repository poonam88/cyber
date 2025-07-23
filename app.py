
import streamlit as st
import pandas as pd
import pickle
import os
import requests

st.title("🚨 Cyber Alert Detection AI")

# Load model and vectorizer
model_path = "cyber_alert_model.pkl"
vectorizer_path = "vectorizer.pkl"

model, vectorizer = None, None

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    st.success("✅ Model loaded successfully")
else:
    st.error("❌ Model files not found!")

# Prediction function
def predict_alerts(texts):
    X = vectorizer.transform(texts)
    return model.predict(X)

# Choose source
source = st.radio("Select input type", ["Upload File", "Fetch from API"])

if source == "Upload File":
    uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            logs = df["log"].dropna().astype(str)
        else:
            logs = pd.Series(uploaded_file.read().decode("utf-8").splitlines())

        predictions = predict_alerts(logs)
        results = pd.DataFrame({"log": logs, "prediction": predictions})
        st.dataframe(results)
        st.download_button("Download Predictions", results.to_csv(index=False), "predictions.csv")

elif source == "Fetch from API":
    api_url = st.text_input("Enter API URL", "http://localhost:5001/get-logs")
    if st.button("Fetch Logs"):
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                logs = pd.Series(response.json()["logs"])
                predictions = predict_alerts(logs)
                results = pd.DataFrame({"log": logs, "prediction": predictions})
                st.dataframe(results)
            else:
                st.error("Failed to fetch logs.")
        except Exception as e:
            st.error(f"Error: {e}")
