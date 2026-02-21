# Re-export shim: canonical implementation lives in agp/config.py
from agp.config import build_config

__all__ = ["build_config"]
