#!/usr/bin/env python3

import asyncio
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
 

class ServerRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Разложение на множители</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><form action='http://127.0.0.1:8081' method='POST'>", "utf-8"))
        self.wfile.write(bytes("<input type='text' name='number'>", "utf-8"))
        self.wfile.write(bytes("<input type='submit' value='Разложить'></form>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):

        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))
        try:
            value = int(post_data['number'][0])
        except:
            value = "Введённое значение должно быть натуральным числом"

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Разложение на множители</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><form action='http://127.0.0.1:8081' method='POST'>", "utf-8"))
        self.wfile.write(bytes("<input type='text' name='number'>", "utf-8"))
        self.wfile.write(bytes("<input type='submit' value='Разложить'></form>", "utf-8"))
        self.wfile.write(bytes("<p>{}</p>".format(factor(value)), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, ServerRequestHandler)
    print('running server...')
    httpd.serve_forever()

async def factor(val):
    if isinstance(val, int):
        Ans = []
        d = 2
        n = val
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        multipliers = ""
        for an in Ans:
            multipliers += str(an) + " * "
        val = (str(val) + " = " + multipliers).rstrip("* ")
    return await val

run()