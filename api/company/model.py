from mongoengine import Document
from mongoengine.fields import StringField, EmbeddedDocumentListField, ListField
from api.company.product.model import Product


class Company(Document):
    name = StringField(required=True, unique=True)
    products = EmbeddedDocumentListField(Product, default=list)

    @staticmethod
    def buildOne(company):
        return {
            'id': str(company.id),
            'name': company.name,
            'products': Product.buildMany(company.products)
        }
    
    @staticmethod
    def buildMany(companies):
        return list(map(lambda company: Company.buildOne(company), companies))