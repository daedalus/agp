# Re-export shim: canonical implementation lives in agp/cli.py
from agp.cli import build_parser, parse_args

__all__ = ["build_parser", "parse_args"]
