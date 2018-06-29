from app.model.cstore import CstoreDocument
from app.model.product import ProductDocument


def paging_items(items, page_index=1, page_length=5):
    start_index = page_length * (page_index - 1)
    end_index = page_length * page_index

    return items[start_index:end_index]


def search_cstores(store_brand, store_name, store_address, target_lng, target_lat, target_radius):
    query = {}

    if store_name is not None:
        query['name__icontains'] = store_name

    if store_address is not None:
        query['address__icontains'] = store_address

    if store_brand is not None:
        query['brand'] = store_brand

    if target_lng is not None and target_lat is not None:
        query['location__near'] = [float(target_lng), float(target_lat)]

    if target_radius is not None:
        query['location__max_distance'] = target_radius

    result = CstoreDocument.objects(**query)
    return result


def search_products(product_brand, product_name, product_flag):
    query = {}

    if product_brand is not None:
        query['brand'] = product_brand

    if product_name is not None:
        query['name__icontains'] = product_name

    if product_flag is not None:
        product_flag = int(product_flag)

        if product_flag == 0:
            query['flag__exists'] = False

        elif product_flag == -1:
            query['flag__exists'] = True

        else:
            query['flag'] = product_flag

    result = ProductDocument.objects(**query)
    return result
