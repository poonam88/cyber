import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ✅ Sample training data (you can replace this with your own CSV or dataset)
data = {
    "log": [
        "Failed login attempt from IP 192.168.1.1",
        "New user created: admin",
        "User admin attempted to escalate privileges",
        "System rebooted successfully",
        "Unauthorized access to database detected",
        "Backup completed",
        "Multiple failed login attempts from IP 10.0.0.5",
        "Virus detected in uploaded file",
        "Disk space checked",
        "Firewall rules updated"
    ],
    "label": [
        1, 1, 1, 0, 1, 0, 1, 1, 0, 0  # 1 = alert, 0 = normal
    ]
}

# ✅ Create a DataFrame
df = pd.DataFrame(data)

# ✅ Vectorize the log messages
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["log"])
y = df["label"]

# ✅ Train a simple Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# ✅ Save the model
with open("cyber_alert_model.pkl", "wb") as f:
    pickle.dump(model, f)

# ✅ Save the vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully.")
