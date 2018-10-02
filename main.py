from aiohttp import web
from routes import setup_routes
from settings import config
import aiohttp_jinja2
import jinja2

app = web.Application()
setup_routes(app)
app['config'] = config

aiohttp_jinja2.setup(
    app, loader=jinja2.PackageLoader('templates'))

web.run_app(app)
