import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b"<h1>Awesome!</h1>", content_type='text/html')

def init():
    app = web.Application()
    app.router.add_route(method='get', path='/', handler=index)
    web.run_app(app, host='127.0.0.1', port=9000, access_log=logging.info('server started at http://127.0.0.1:9000...'))

init()
