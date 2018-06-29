from flasgger import Swagger
from flask import Flask

from app.doc import TEMPLATE
from app.model import Mongo
from app.view import Router
from config import Config


def create_app():
    instance = Flask(__name__)
    instance.config.from_object(Config)

    Swagger(template=TEMPLATE).init_app(instance)
    Router().init_app(instance)
    Mongo().init_app(instance)

    return instance


app = create_app()
