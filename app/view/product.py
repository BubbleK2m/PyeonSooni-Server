from flask import Blueprint, request
from flask_restful import Api, Resource
from flasgger import swag_from

from app.doc.product import PRODUCT_GET_SPEC
from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

api = Api(Blueprint('product-api', __name__))


@api.resource('/product')
class ProductResource(Resource):
    @swag_from(PRODUCT_GET_SPEC)
    def get(self):
        product_brand = request.args.get('product_brand')
        product_name = request.args.get('product_name')
        product_flag = request.args.get('product_flag')

        page_index = int(request.args.get('page_index', 1))
        page_length = int(request.args.get('page_length', 5))

        products = api_helper.search_products(product_brand, product_name, product_flag)
        products = api_helper.paging_items(products, page_index, page_length)

        product_dicts = mongo_helper.mongo_list_to_python_list(products)
        return response_helper.unicode_safe_json_respnose(product_dicts)
