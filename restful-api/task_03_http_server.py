#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Underclass(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode(encoding="utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_error(404, "Not Found", "No {}".format(self.path))



def run(server_class=HTTPServer, handler_class=Underclass):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()