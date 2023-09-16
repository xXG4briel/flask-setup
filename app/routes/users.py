# from app.models.users import User
from flask import Blueprint, jsonify, request
from app.utils.date import get_current_date
import uuid

bp = Blueprint('users', __name__, url_prefix="/users")

users = {}  # Usando um dicionário para manter o controle dos usuários

@bp.route("/", methods=["GET"])
def index():
    return jsonify({ "users": [user for user in users.values()] })


@bp.route("/<string:user_id>", methods=["GET"])
def show(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id])


@bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user_id = str(uuid.uuid4())  # Gere um UUID único
    users[user_id] = {"name": data["name"], "id": user_id, "created_at": get_current_date(), "updated_at": get_current_date()}

    return jsonify({"user_id": user_id}), 201

@bp.route("/<string:user_id>", methods=["PUT"])
def update(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    users[user_id]["name"] = data["name"]
    users[user_id]["updated_at"] = get_current_date()
    
    return jsonify({"message": "User updated successfully"})

@bp.route("/<string:user_id>", methods=["DELETE"])
def destroy(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"})
