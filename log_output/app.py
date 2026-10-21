import os
import secrets
import string
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ALPHABET = string.ascii_letters + string.digits
IDENTIFIER = "".join(secrets.choice(ALPHABET) for _ in range(12))


def current_status() -> tuple[str, str]:
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return timestamp, IDENTIFIER


class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path not in ("/", "/status"):
            self.send_error(404)
            return

        timestamp, identifier = current_status()
        body = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Log output</title>
  </head>
  <body>
    <main>
      <h1>Log output</h1>
      <p><strong>Timestamp:</strong> {timestamp}</p>
      <p><strong>Random string:</strong> {identifier}</p>
    </main>
  </body>
</html>
"""
        payload = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        pass


def log_output() -> None:
    while True:
        timestamp, identifier = current_status()
        print(f"{timestamp} {identifier}", flush=True)
        time.sleep(5)


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), StatusHandler)
    print(f"Server started in port {port}", flush=True)
    threading.Thread(target=log_output, daemon=True).start()
    server.serve_forever()


if __name__ == "__main__":
    main()
