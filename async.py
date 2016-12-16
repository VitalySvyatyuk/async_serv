import datetime
import socketserver
 
class ServerRequestHandler(socketserver.StreamRequestHandler):
 
    def handle(self):
        try:
            print("Connection from: {}".format(self.client_address))
            request_msg = self.rfile.readline(1024)
            self.wfile.write('''HTTP/1.0 200 Ok
 
    Hello world {}'''.format(datetime.datetime.now()))
            self.wfile.flush()
        except Exception as ex:
            print('e', ex)
 
def simple_tcp_server():
    tcp_server = socketserver.ThreadingTCPServer(
        ("0.0.0.0", 8081),
        RequestHandlerClass=ServerRequestHandler,
        bind_and_activate=False)
 
    tcp_server.allow_reuse_address = True
    tcp_server.server_bind()
    tcp_server.server_activate()
 
    tcp_server.serve_forever()
 
if __name__ == "__main__":
    simple_tcp_server()