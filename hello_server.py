from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")
def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Servidor rodando na porta 8080...")
    httpd.serve_forever()

run_server()
