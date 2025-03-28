import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("data/user_behavior_data.csv")

# Features: Typing Speed, Scroll Speed, Reaction Time
X = df[['typing_speed', 'scroll_speed', 'reaction_time']]
y = df['is_legitimate']  # 1 = Real User, 0 = Fake User

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
with open("app/models/digital_dna_model.pkl", "wb") as f:
    pickle.dump(model, f)
