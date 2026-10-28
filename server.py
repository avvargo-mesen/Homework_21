from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("contacts.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        print("Получено:", post_data)
        # Отправляем ответ, чтобы браузер не завис
        self.send_response(200)
        self.end_headers()

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()