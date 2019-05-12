from sanic import Sanic
from sanic.response import json
from sanic.exceptions import SanicException
from sanic_openapi import swagger_blueprint
from api.company.routes import company_routes
from api.recharge.routes import recharge_routes
from mongoengine import connect
from api.utils.exception_handler import handle_exception

app = Sanic(__name__)

connect('jeitto')

@app.route('/')
async def root(request):
    return json({}, status=200)

app.blueprint(swagger_blueprint)
app.blueprint(company_routes)
app.blueprint(recharge_routes)
app.error_handler.add(SanicException, handle_exception)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)