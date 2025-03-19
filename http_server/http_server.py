import re
import socket
import sys
import io


class HttpServer(object):

    def __init__(self, host="0.0.0.0", port=80):
        """ Constructor """
        self._host = host
        self._port = port
        self._routes = []
        self._connect = None
        self._on_request_handler = None
        self._on_not_found_handler = None
        self._on_error_handler = None
        self._sock = None

    def start(self):
        """ Start server """
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self._host, self._port))
        self._sock.listen(1)
        print("Server start")
        while True:
            if self._sock is None:
                break
            try:
                self._connect, address = self._sock.accept()
                request = self.get_request()
                if len(request) == 0:
                    self._connect.close()
                    continue
                if self._on_request_handler:
                    if not self._on_request_handler(request, address):
                        continue
                route = self.find_route(request)
                if route:
                    route["handler"](request)
                else:
                    self._route_not_found(request)
            except Exception as e:
                self._internal_error(e)
            finally:
                self._connect.close()

    def stop(self):
        """ Stop the server """
        self._connect.close()
        self._sock.close()
        self._sock = None
        print("Server stop")

    def add_route(self, path, handler, method="GET"):
        """ Add new route  """
        self._routes.append(
            {"path": path, "handler": handler, "method": method})

    def send(self, data):
        """ Send data to client """
        if self._connect is None:
            raise Exception("Can't send response, no connection instance")
        self._connect.sendall(data.encode())

    def find_route(self, request):
        """ Find route """
        lines = request.split("\r\n")
        method = re.search("^([A-Z]+)", lines[0]).group(1)
        path = re.search("^[A-Z]+\\s+(/[-a-zA-Z0-9_.]*)", lines[0]).group(1)
        for route in self._routes:
            if method != route["method"]:
                continue
            if path == route["path"]:
                return route
            else:
                match = re.search("^" + route["path"] + "$", path)
                if match:
                    print(method, path, route["path"])
                    return route

    def get_request(self, buffer_length=4096):
        """ Return request body """
        request = str(self._connect.recv(buffer_length), "utf8")
        return request

    def on_request(self, handler):
        """ Set request handler """
        self._on_request_handler = handler

    def on_not_found(self, handler):
        """ Set not found handler """
        self._on_not_found_handler = handler

    def on_error(self, handler):
        """ Set error handler """
        self._on_error_handler = handler

    def _route_not_found(self, request):
        """ Route not found handler """
        if self._on_not_found_handler:
            self._on_not_found_handler(request)
        else:
            """ Default not found handler """
            self.send("HTTP/1.0 404 Not Found\r\n")
            self.send("Content-Type: text/plain\r\n\r\n")
            self.send("Not found")

    def _internal_error(self, error):
        """ Internal error handler """
        if self._on_error_handler:
            self._on_error_handler(error)
        else:
            """ Default internal error handler """
            if "print_exception" in dir(sys):
                output = io.StringIO()
                sys.print_exception(error, output)
                str_error = output.getvalue()
                output.close()
            else:
                str_error = str(error)
            self.send("HTTP/1.0 500 Internal Server Error\r\n")
            self.send("Content-Type: text/plain\r\n\r\n")
            self.send("Error: " + str_error)
            print(str_error)
            
    def send_html(self, file_path):
        """ Send HTML file to client """
        try:
            with open(file_path, "r") as html_file:
                html_content = html_file.read()

            self.send("HTTP/1.0 200 OK\r\n")
            self.send("Content-Type: text/html\r\n\r\n")
            self.send(html_content)

        except Exception as e:
            self._internal_error(e)

    def parse_post_data(self, request):
        """ Handles POST requests and parses the body """
        lines = request.split("\r\n")
        # Parse headers (simple version)
        headers = {line.split(":")[0]: line.split(":")[1].strip() for line in lines if ":" in line}
        print("start to parse post data")
        # Get the content length
        content_length = int(headers.get("Content-Length", 0))
        print(content_length)
        # Read the POST body if there is one
        body = ""
        if content_length > 0:
            try:
                body = self._connect.recv(1024)
            except Exception as e:
                print("Error reading POST body", e)
                
        print(body)
        # Assuming it's form data or JSON, you can process the body here
        return body  # Return the body for now, further processing can be added

    def add_post_route(self, path, handler):
        """ Add new route for POST method """
        self.add_route(path, handler, method="POST")