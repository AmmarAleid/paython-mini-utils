import sys
from pathlib import Path

# Add the repository root folder to Python's import path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))