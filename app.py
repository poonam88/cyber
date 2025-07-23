
import streamlit as st
import pickle
import pandas as pd
from file_watcher import tail_file

st.title("🔐 Real-Time Log Anomaly Detector")

# Load the model
model = pickle.load(open("trained_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

st.success("✅ Model loaded successfully!")

# --- Real-Time Log Simulation ---
st.subheader("📡 Real-Time Log Simulation")

enable_realtime = st.checkbox("Enable Real-Time Log Monitoring")

if enable_realtime:
    st.info("Watching logs from `logs_stream.txt`...")
    log_display = st.empty()
    pred_display = st.empty()

    pos = 0
    while True:
        new_logs, pos = tail_file("logs_stream.txt", last_position=pos)
        if new_logs:
            for log in new_logs:
                log_display.text(f"New log: {log.strip()}")
                vect_log = vectorizer.transform([log])
                pred = model.predict(vect_log)[0]
                pred_display.success(f"Prediction: {pred}")
        time.sleep(2)

