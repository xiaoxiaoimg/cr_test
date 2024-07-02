from flask import Blueprint, request, jsonify
from app.models import create_user
from errors.exceptions import ValidationError

main_route = Blueprint("main", __name__)


@main_route.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        user = create_user(data["username"], data["password"])
        return jsonify({"message": "User created successfully"}), 201
    except ValidationError as e:
        pass
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400
