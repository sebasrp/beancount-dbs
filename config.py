import sys
from os import path
import beancount_dbs.dbs as dbs
# Add current path for testing.
sys.path.insert(0, path.join(path.dirname(__file__)))

from beancount.ingest import extract
from beancount_dbs import HangSengSavingsImporter

CONFIG = [
    dbs.Importer()
]