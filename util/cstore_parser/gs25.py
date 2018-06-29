from caspi import gs25
from util.cstore_parser import CStoreParser


class GS25Parser(CStoreParser):
    def __init__(self):
        super(GS25Parser, self).__init__('gs25')

    def get_products(self):
        return gs25.get_products('fresh_food') + \
               gs25.get_products('different_service') + \
               gs25.get_products('one_plus_one') +\
               gs25.get_products('two_plus_one')

    def get_stores(self):
        return gs25.get_stores(30)
