import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# Create an instance of the socket server and specify the handler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()