from flask import globals
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


def init_app(app):
    with app.app_context():

        cred = credentials.Certificate({
            "type": "service_account",
            "private_key_id": os.environ['DB_PRIVATE_KEY_ID'],
            "private_key": os.environ['DB_PRIVATE_KEY'].replace("\\n", "\n"),
            "client_email": str(os.environ['DB_CLIENT_EMAIL']),
            "client_id": str(os.environ['DB_CLIENT_ID']),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
        })
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.environ['DATABASE_URL']
        })

        globals.db = db.reference('/')
