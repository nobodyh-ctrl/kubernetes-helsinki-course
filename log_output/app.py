import secrets
import string
import time
from datetime import datetime, timezone

ALPHABET = string.ascii_letters + string.digits


def generate_id(length: int = 12) -> str:
    """Generate a random string once, at startup."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main() -> None:
    identifier = generate_id()

    while True:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"{timestamp} {identifier}", flush=True)
        time.sleep(5)


if __name__ == "__main__":
    main()
