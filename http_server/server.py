from http.server import BaseHTTPRequestHandler, HTTPServer
import time



host = "localhost"
port = 8080

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open('website/index.html')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f.read(), 'utf-8'))
            f.close()
            return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


if __name__ == "__main__":        
    webServer = HTTPServer((host, port), Server)
    print(f'Server started. Listening on: http://{host}:{port}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")