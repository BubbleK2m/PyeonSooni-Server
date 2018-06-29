from caspi import cu
from util.cstore_parser import CStoreParser


class CUParser(CStoreParser):
    def __init__(self):
        super(CUParser, self).__init__('cu')

    def get_products(self):
        return cu.get_products('pb') + \
               cu.get_products('plus')

    def get_stores(self):
        return cu.get_stores('대전광역시')
