from http.server import BaseHTTPRequestHandler
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from backend import H


class handler(H):
    pass