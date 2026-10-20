import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def index() -> str:
    return "Todo application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
