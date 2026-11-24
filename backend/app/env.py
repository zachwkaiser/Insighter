# Reads API keys from the environment or backend/.env.
import os
from pathlib import Path

_ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


def api_key(name: str) -> str:
    """Return an API key from the environment, or from backend/.env."""
    from_environment = os.environ.get(name)
    if from_environment:
        return from_environment

    from_file = _value_from_env_file(name)
    if from_file:
        os.environ[name] = from_file
        return from_file

    raise RuntimeError(f"{name} is not set")


def _value_from_env_file(name: str) -> str | None:
    if not _ENV_FILE.is_file():
        return None

    for line in _ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        if key.strip() == name:
            return value.strip().strip('"').strip("'")

    return None
