from flask import Flask, request, jsonify
import pymongo
import pickle
import numpy as np
import time

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["digital_dna"]
user_data = db["user_behavior"]

# Load trained fraud detection model
with open("app/models/digital_dna_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/collect_data', methods=['POST'])
def collect_data():
    data = request.json
    user_data.insert_one({**data, "timestamp": time.time()})
    return jsonify({"status": "success", "message": "User data recorded"}), 200

@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    data = request.json
    user_input = np.array([[data['typing_speed'], data['scroll_speed'], data['reaction_time']]])
    prediction = model.predict(user_input)
    
    if prediction[0] == 0:
        return jsonify({"status": "fraudulent", "message": "Fake Account Detected!"}), 403
    else:
        return jsonify({"status": "legitimate", "message": "User Verified"}), 200

if __name__ == '__main__':
    app.run(debug=True)
