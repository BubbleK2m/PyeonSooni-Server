from caspi import seven_eleven
from util.cstore_parser import CStoreParser


class SevenElevenParser(CStoreParser):
    def __init__(self):
        super(SevenElevenParser, self).__init__('7eleven')

    def get_products(self):
        return seven_eleven.get_products('7_select') + \
               seven_eleven.get_products('one_plus_one') + \
               seven_eleven.get_products('two_plus_one')

    def get_stores(self):
        return seven_eleven.get_stores('대전')
