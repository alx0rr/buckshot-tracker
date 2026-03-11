
import http.server
import socket
import os
import sys


def load_html():
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "buckshot-tracker.html")
    with open(path, "rb") as f:
        return f.read()

HTML_BYTES = load_html()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "unavailable"

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(HTML_BYTES)))
        self.end_headers()
        self.wfile.write(HTML_BYTES)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    port = get_free_port()
    local_ip = get_local_ip()
    local_url   = f"http://localhost:{port}"
    network_url = f"http://{local_ip}:{port}"

    pad = lambda s, w: s + " " * (w - len(s))
    w = max(len(local_url), len(network_url)) + 4
    line = "═" * (w + 2)

    def row(text):
        return f"  ║ {pad(text, w)} ║"


    print(f"  ╔{line}╗")
    print(row("BUCKSHOT TRACKER  —  SERVER"))
    print(f"  ╚{line}╝")

    print(f"  Local:    {local_url}")
    print(f"  Network:  {network_url}")

    print(f"  ╔{line}╗")
    print(row("  Ctrl+C to stop"))
    print(f"  ╚{line}╝")

    with http.server.HTTPServer(("", port), Handler) as httpd:
        try:httpd.serve_forever()
        except KeyboardInterrupt:print("\n  Server stopped.")