# Re-export shim: canonical implementation lives in agp/data.py
from agp.data import load_and_preprocess

__all__ = ["load_and_preprocess"]
