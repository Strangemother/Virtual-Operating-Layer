"""A simple dest caller to enact the correct headers to import the database files.
as a crud api
"""
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = os.path.join(BASE_DIR, 'header')
sys.path.append(HEADER)
import dev
