import socket
import network
import sys

from http_server.http_server import HttpServer
from http_server.utils import get_request_post_params

server = HttpServer()


def index(request):
    print("Request received")
    server.send_html('./public/index.html')


def stop(request):
    print("Stopping server")
    server.stop()
    
def post_handler(request):
    """ Handle POST request """   
    post_data = get_request_post_params(request)
    print(post_data)
    server.send("HTTP/1.0 200 OK\r\n")
    server.send("Content-Type: text/plain\r\n\r\n")
    server.send("POST Data received!")


server.add_route("/", index)
server.add_route("/stop", stop)
server.add_post_route("/save", post_handler)


server.start()
 