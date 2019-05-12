from sanic.views import HTTPMethodView
from sanic.response import json
from http import *
from datetime import datetime
from api.recharge.model import Recharge
from api.company.model import Company
from mongoengine import ValidationError
from mongoengine.fields import ObjectId
from api.utils.exception_handler import BadRequestException


class RechargeView(HTTPMethodView):
    async def get(self, request):
        if request.args.get('phoneNumber'):
            return await RechargeView.getRechargesByPhoneNumber(request, request.args.get('phoneNumber'))
        elif request.args.get('id'):
            return await RechargeView.getByRechargeId(request, request.args.get('id'))
        else:
            recharges = Recharge.objects()
            return json(Recharge.buildMany(recharges), status=HTTPStatus.OK)

    async def post(self, request):
        body = request.json
        recharge = Recharge()
        recharge.phoneNumber = body.get('phoneNumber')
        if not recharge.phoneNumber.isdigit():
            raise BadRequestException('Invalid phone number')
        if not ObjectId.is_valid(body.get('companyId')):
            raise BadRequestException('Invalid Company Id')
        if not Company.objects.with_id(body.get('companyId')):
            raise BadRequestException('Company not found')
        recharge.companyId = ObjectId(body.get('companyId'))
        company = Company.objects(id=ObjectId(recharge.companyId), products__match={'id': ObjectId(body.get('productId'))})
        if len(company) == 0:
            raise BadRequestException('This company does not have this product')
        recharge.productId = body.get('productId')
        recharge.value = body.get('value')
        recharge.createdAt = str(datetime.now())
        try:
            recharge.validate()
        except ValidationError as e:
            raise BadRequestException(e.to_dict())
        recharge.save()
        return json(Recharge.buildOne(recharge), status=HTTPStatus.CREATED)

    @staticmethod
    async def getByRechargeId(request, rechargeId):
        recharge = Recharge.objects(id=rechargeId)
        if len(recharge) == 0:
            return json({}, status=HTTPStatus.NO_CONTENT)
        return json(Recharge.buildOne(recharge[0]), status=HTTPStatus.OK)

    @staticmethod
    async def getRechargesByPhoneNumber(request, phoneNumber):
        recharges = Recharge.objects(phoneNumber=phoneNumber)
        print(recharges.to_json())
        if len(recharges) == 0:
            return json([], status=HTTPStatus.NO_CONTENT)
        return json(Recharge.buildMany(recharges), status=HTTPStatus.OK)
