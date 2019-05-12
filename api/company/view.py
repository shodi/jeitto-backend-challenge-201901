from sanic.views import HTTPMethodView
from sanic.response import json
from http import *
from mongoengine import ValidationError
from mongoengine.fields import ObjectId
from api.company.model import Company
from api.company.product.model import Product
from api.utils.exception_handler import BadRequestException


class CompanyView(HTTPMethodView):
    async def get(self, request):
        if request.args.get('companyId'):
            return await CompanyView.getCompanyById(request, request.args.get('companyId'))
        if request.args.get('productId'):
            return await CompanyView.getCompanyByProductId(request, request.args.get('productId'))
        if request.args.get('companyName'):
            return await CompanyView.getCompanyByName(request, request.args.get('companyName'))
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

    @staticmethod
    async def getCompanyById(request, companyId):
        company = Company.objects(id=companyId)
        return json(Company.buildOne(company[0]), status=HTTPStatus.OK)

    @staticmethod
    async def getCompanyByProductId(request, productId):
        company = Company.objects(products__match={'id': ObjectId(productId)})
        return json(Company.buildOne(company[0]), status=HTTPStatus.OK)

    @staticmethod
    async def getCompanyByName(request, companyName):
        companies = Company.objects(name=companyName)
        return json(Company.buildMany(companies), status=HTTPStatus.OK)
