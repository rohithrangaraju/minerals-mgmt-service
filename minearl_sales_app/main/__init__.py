from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_bcrypt import Bcrypt
import gridfs
from .config import config_by_name
from mongoengine import connect
from ..main.exceptions import ExceptionHandlers
# from .models.product import Product

db = connect('product')
file_storage_object = gridfs.GridFS(db.product)
flask_bcrypt = Bcrypt()


def register_blueprints(app):
    from minearl_sales_app.main.blueprints.api_product import product_api
    app.register_blueprint(product_api)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    # db.init_app(app)
    flask_bcrypt.init_app(app)
    register_blueprints(app)
    ExceptionHandlers.register_all(app)

    return app
