from sanic import Blueprint
from api.company.view import CompanyView

company_routes = Blueprint('company_routes', url_prefix='/CompanyProducts', strict_slashes=True)

company_routes.add_route(CompanyView.as_view(), '')