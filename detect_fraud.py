from flask import Blueprint, request, jsonify
import numpy as np
import pickle

detect_fraud_bp = Blueprint('detect_fraud', __name__)

# Load trained fraud detection model
with open("app/models/digital_dna_model.pkl", "rb") as f:
    model = pickle.load(f)

@detect_fraud_bp.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    data = request.json
    user_input = np.array([[data['typing_speed'], data['scroll_speed'], data['reaction_time']]])
    prediction = model.predict(user_input)

    if prediction[0] == 0:
        return jsonify({"status": "fraudulent", "message": "Fake Account Detected!"}), 403
    else:
        return jsonify({"status": "legitimate", "message": "User Verified"}), 200
