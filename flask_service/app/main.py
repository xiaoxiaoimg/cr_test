from flask import Blueprint

main_route = Blueprint("main", __name__)


@main_route.route("/")
def index():
    return "Welcome to the API!"
