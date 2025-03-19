import socket
import network
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'http_server'))

from http_server import HttpServer
import utils

server = HttpServer()


def index(request):
    print("Request received")
    server.send_html('./public/index.html')


def stop(request):
    print("Stopping server")
    server.stop()


def set_cookies(request):
    cookies_header = utils.create_cookie("name", "value", expires="Sat, 01-Jan-2030 00:00:00 GMT")
    utils.send_response(server, "OK", extend_headers=[cookies_header])


def get_cookies(request):
    cookies = utils.get_cookies(request)
    utils.send_response(server, str(cookies))


server.add_route("/", index)
server.add_route("/stop", stop)
server.add_route("/set_cookies", set_cookies)
server.add_route("/get_cookies", get_cookies)

server.start()
 