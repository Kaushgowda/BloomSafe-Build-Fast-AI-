import sys
import os

# Add the project root to Python's import path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from backend import H

# Vercel Python entrypoint
handler = H