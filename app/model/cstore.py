from mongoengine import *


class CstoreDocument(Document):
    meta = {
        'collection': 'cstore'
    }

    brand = StringField(required=True)
    name = StringField(required=True)
    address = StringField()
    location = PointField()
    tel = StringField()
