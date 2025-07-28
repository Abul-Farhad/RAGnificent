import yaml
from pathlib import Path
import os

# Updated: Store config in user's home directory (cross-platform)
CONFIG_DIR = Path.home() / ".ragnificentai"
CONFIG_PATH = CONFIG_DIR / "config.yaml"

def save_config(config: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)

def load_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f) or {}
    return {}