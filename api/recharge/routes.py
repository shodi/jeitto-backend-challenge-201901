from sanic import Blueprint
from api.recharge.view import RechargeView

recharge_routes = Blueprint('recharge_routes', url_prefix='/PhoneRecharges', strict_slashes=True)

recharge_routes.add_route(RechargeView.as_view(), '')
