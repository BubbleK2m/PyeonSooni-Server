from flask import Blueprint, request
from flask_restful import Api, Resource
from flasgger import swag_from

from app.doc.cstore import CSTORE_GET_SPEC
from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

api = Api(Blueprint('store-api', __name__))


@api.resource('/store')
class CStoreResource(Resource):
    @swag_from(CSTORE_GET_SPEC)
    def get(self):
        store_brand = request.args.get('store_brand')
        store_name = request.args.get('store_name')
        store_address = request.args.get('store_address')

        target_lng = request.args.get('target_lng')
        target_lat = request.args.get('target_lat')
        search_radius = request.args.get('search_radius')

        page_index = int(request.args.get('page_index', 1))
        page_length = int(request.args.get('page_length', 5))

        stores = api_helper.search_cstores(store_brand,
                                           store_name,
                                           store_address,
                                           target_lat,
                                           target_lng,
                                           search_radius)

        stores = api_helper.paging_items(stores, page_index, page_length)
        store_dicts = mongo_helper.mongo_list_to_python_list(stores)

        return response_helper.unicode_safe_json_respnose(store_dicts)
