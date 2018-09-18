from flask import current_app as app
from flask import Blueprint, jsonify, request
import uuid
import json
from ...main import db
from ..models.product import Product
# from ...main import file_storage_object
import serpy
from ..services.product_service import create_product, get_product
from ..utils.view import get_payload

product_api = Blueprint('product_api', __name__)


@product_api.route('/product', methods=['GET', 'POST'])
@product_api.route('/product/<int:role_id>', methods=['GET', 'POST'])
def return_all_products(role_id=None):
    # file_storage_object.put()
    # class UserSchemaNoPassword(serpy.Serializer):
    #     mongo_id = serpy.StrField()
    #     product_id = serpy.IntField()
    # u=UserSchemaNoPassword(p, many=True).data
    # for key in request.files:
    #     print(request.files.get(key))
    #     # image_id=file_storage_object.put(request.files.get(key))
    #     # print(image_id)
    # print(p[0].product_id, p[0].mongo_id)
    # print(request.args)
    # create_product(json_dict=request.data)
    return get_payload()
