from app.model.cstore import CstoreDocument
from app.model.product import ProductDocument

from util import google_maps_helper
from pprint import pprint


class CStoreParser:
    """
        Constructor and Parser
        Entry Point
    """

    def __init__(self, brand):
        self.brand = brand

    def parse(self):
        self.parse_products(self.get_products())
        self.parse_stores(self.get_stores())

    """
        Methods to Get 
        Products and Stores
        in CStore Brand
    """

    def get_products(self):
        pass

    def get_stores(self):
        pass

    """
        Methods to Parse and Save
        Products and Stores Data
        in CStore Brand
    """

    def parse_products(self, products):
        print('[info] parse {} products was started'.format(self.brand))

        for p in products:
            product = ProductDocument(brand=self.brand, name=p['name'],
                                      price=int(p.get('price')))

            product_flag = p.get('flag')
            product.flag = int(product_flag[0]) if product_flag else None

            product.image = p.get('image')
            product.save()

        print('[info] parse {} products was finished'.format(self.brand))

    def parse_stores(self, stores):
        print('[info] parse {} stores was started'.format(self.brand))

        for s in stores:
            store = CstoreDocument(brand=self.brand, name=s['name'])
            store.address = s.get('address')

            if store.address is not None:
                location_data = google_maps_helper.get_location_data_from_address(store.address)

                if location_data is not None:
                    store.location = [location_data['lng'], location_data['lat']]

            store.tel = s.get('tel')
            store.save()

        print('[info] parse {} stores was finished'.format(self.brand))
