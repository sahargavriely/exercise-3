import http.server
import re


class Website:
    paths = dict()

    def route(self, path):
        def collect(f):
            self.paths[f'{path}$'] = f
        return collect

    def run(self, address):
        paths = self.paths
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                for path, f in paths.items():
                    if re.match(path, self.path):
                        status_code, res = f(*[arg for arg in re.match(path, self.path).groups()])
                        self.send_response(status_code)
                        self.send_header('Content-Type', 'text/html')
                        self.end_headers()
                        self.wfile.write(res.encode())
                        break
                else:
                    self.send_response(404)
                    self.end_headers()

        httpd = http.server.HTTPServer(address, Handler)
        httpd.serve_forever()
