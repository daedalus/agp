# Re-export shim: canonical implementation lives in agp/report.py
from agp.report import create_report_header, print_clinical_summary

__all__ = ["create_report_header", "print_clinical_summary"]
