from sanic.views import HTTPMethodView
from sanic.response import json
from http import *
from mongoengine import ValidationError
from api.company.model import Company
from api.company.product.model import Product
from api.utils.exception_handler import BadRequestException


class CompanyView(HTTPMethodView):
    async def get(self, request):
        response = Company.buildMany(Company.objects())
        return json(response, status=HTTPStatus.OK)

    async def post(self, request):
        body = request.json
        company = Company()
        company.name = body.get('name')
        company.products = []
        for product in body.get('products', []):
            prod = Product()
            prod.name = product.get('name')
            prod.value = product.get('value')
            company.products.append(prod)
        try:
            company.validate()
        except ValidationError as e:
            raise BadRequestException(e.to_dict())
        company.save()
        return json(Company.buildOne(company), status=HTTPStatus.CREATED)