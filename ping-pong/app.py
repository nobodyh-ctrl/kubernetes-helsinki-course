import os
import threading

from flask import Flask

app = Flask(__name__)

counter = 0
counter_lock = threading.Lock()


@app.get("/pingpong")
def pingpong():
    global counter
    with counter_lock:
        value = counter
        counter += 1

    return f"pong {value}", 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
