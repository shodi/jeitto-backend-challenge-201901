from mongoengine import EmbeddedDocument
from mongoengine.fields import ObjectId, StringField, DecimalField, ObjectIdField


class Product(EmbeddedDocument):
    id = ObjectIdField(required=True, default=ObjectId, db_field='_id')
    name = StringField(required=True)
    value = DecimalField(required=True)

    @staticmethod
    def buildOne(product):
        return {
            'id': str(product.id),
            'name': product.name,
            'value': product.value
        }

    @staticmethod
    def buildMany(products):
        return list(map(lambda product: Product.buildOne(product), products))