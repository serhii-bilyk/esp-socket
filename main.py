import socket
import network
import sys

from http_server.http_server import HttpServer
import http_server.utils

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
    
def post_handler(request):
    """ Handle POST request """
    post_data = server.parse_post_data(request)
    print("POST Data:", post_data)
    server.send("HTTP/1.0 200 OK\r\n")
    server.send("Content-Type: text/plain\r\n\r\n")
    server.send("POST Data received!")


server.add_route("/", index)
server.add_route("/stop", stop)
server.add_post_route("/save", post_handler)
server.add_route("/set_cookies", set_cookies)
server.add_route("/get_cookies", get_cookies)

server.start()
 