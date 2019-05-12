from mongoengine import Document
from mongoengine.fields import ObjectIdField, StringField, DecimalField


class Recharge(Document):
    companyId = ObjectIdField(required=True)
    productId = ObjectIdField(required=True)
    createdAt = StringField(required=True)
    phoneNumber = StringField(required=True)
    value = DecimalField(required=True)

    @staticmethod
    def buildOne(recharge):
        return {
            'id': str(recharge.id),
            'createdAt': recharge.createdAt,
            'companyId': str(recharge.companyId),
            'productId': str(recharge.productId),
            'phoneNumber': recharge.phoneNumber,
            'value': recharge.value
        }

    @staticmethod
    def buildMany(recharges):
        return list(map(lambda recharge: Recharge.buildOne(recharge), recharges))
