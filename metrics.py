# Re-export shim: canonical implementation lives in agp/metrics.py
from agp.metrics import (
    compute_mage,
    compute_modd,
    compute_adrr,
    compute_conga,
    compute_risk_indices,
    compute_gri,
    compute_all_metrics,
)

__all__ = [
    "compute_mage",
    "compute_modd",
    "compute_adrr",
    "compute_conga",
    "compute_risk_indices",
    "compute_gri",
    "compute_all_metrics",
]
