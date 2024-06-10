from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/json':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"message": "Hello, JSON!"}
            self.wfile.write(json.dumps(data).encode())
        elif path == '/xml':
            self.send_response(200)
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            data = "<message>Hello, XML!</message>"
            self.wfile.write(data.encode())
        elif path == '/csv':
            self.send_response(200)
            self.send_header("Content-type", "text/csv")
            self.end_headers()
            data = "message\nHello, CSV!"
            self.wfile.write(data.encode())
        elif path == '/html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
