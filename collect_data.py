from flask import Blueprint, request, jsonify
import time
from app.database.db_connection import db

collect_data_bp = Blueprint('collect_data', __name__)

@collect_data_bp.route('/collect_data', methods=['POST'])
def collect_data():
    data = request.json
    db["user_behavior"].insert_one({**data, "timestamp": time.time()})
    return jsonify({"status": "success", "message": "User data recorded"}), 200
