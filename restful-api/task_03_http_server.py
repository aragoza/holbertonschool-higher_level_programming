#!!/usr/bin/python3

import http.server

module = http.server.BaseHTTPRequestHandler

class underclass(module):
    def do_GET(self):
        self