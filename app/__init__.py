from flask import Flask

from database import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)
