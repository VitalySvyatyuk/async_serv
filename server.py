#!/usr/bin/env python3

# from http.server import BaseHTTPRequestHandler, HTTPServer

# Handler = BaseeHTTPRequestHandler

# server_address = ('127.0.0.1', 8081)

# # Handler.protocol_version = "HTTP/1.0"
# httpd = HTTPServer(server_address, Handler)
# print('running server...')
# httpd.serve_forever()










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

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Разложение на множители</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><form action='http://127.0.0.1:8081' method='POST'>", "utf-8"))
        self.wfile.write(bytes("<input type='text' name='number'>", "utf-8"))
        self.wfile.write(bytes("<input type='submit' value='Разложить'></form>", "utf-8"))
        self.wfile.write(bytes("<p>And you know what?.. This is POST!</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

 

def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, ServerRequestHandler)
    print('running server...')
    httpd.serve_forever()

def factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

run()