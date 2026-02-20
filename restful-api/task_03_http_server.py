#!/usr/bin/python3
"""
Docstring for task_03_http_server.py
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Underclass(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Docstring for do_Get
        """
        if self.path == "/":
            message = "Hello this is a simple API!"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))
            return
        elif self.path == "/data":
            self.send_response(200)
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            data_serialize = json.dumps(data).encode(encoding="utf-8")

            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data_serialize.encode("utf-8"))
            return
        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Ok".encode("utf-8"))
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers
        self.wfile.write("Endpoint not found")



def run(server_class=HTTPServer, handler_class=Underclass):
    """
    Docstring for run
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()