from app.model.cstore import CstoreDocument
from app.model.product import ProductDocument

from util.cstore_parser.cu import CUParser
from util.cstore_parser.gs25 import GS25Parser
from util.cstore_parser.seven_eleven import SevenElevenParser

from multiprocessing import Process

if __name__ == '__main__':
    # Drop all Collections
    CstoreDocument.drop_collection()
    ProductDocument.drop_collection()

    # Generate CU, GS25, 7Eleven Parsers
    cu = CUParser()
    gs25 = GS25Parser()
    seven_eleven = SevenElevenParser()

    # Generate Parsing Processes List
    procs = [
        Process(target=cu.parse),
        Process(target=gs25.parse),
        Process(target=seven_eleven.parse)
    ]

    # Start all Process for Parsing
    for p in procs:
        p.start()

    # Wait all Process was Finished
    for p in procs:
        p.join()


