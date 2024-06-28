from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.routes import main_route

    app.register_blueprint(main_route)
    return app
