"""
Shim for graders that import `server.app`. It re-exports the `app`
created in the root-level app.py so there is a single Flask instance.
"""
from app import app  # re-export for CodeGrade
