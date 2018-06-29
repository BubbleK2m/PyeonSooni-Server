from mongoengine import *


class ProductDocument(Document):
    meta = {
        'collection': 'product'
    }

    brand = StringField(required=True)
    name = StringField(required=True)
    price = IntField()
    flag = IntField()
    image = StringField()
