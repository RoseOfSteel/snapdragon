"""
Store important paths.
"""
import os
from pathlib import Path

# Path to this specific file (so we can always access the project root directory)
root_path = os.path.dirname(os.path.realpath(__file__))

# Path to the database file
db_path = root_path + '\snapdragon.db'
