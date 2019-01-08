from flask import Flask
from dbase.server import DatabaseConnect
from config import app_configuration

def create_app(mode):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(app_configuration)

        from api.views import creditcard_views


    return app

app = create_app(mode='development')