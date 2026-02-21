# Re-export shim: canonical implementation lives in agp/plot.py
from agp.plot import build_agp_profile, generate_agp_plot

__all__ = ["build_agp_profile", "generate_agp_plot"]
