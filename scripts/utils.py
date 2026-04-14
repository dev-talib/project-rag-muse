import sys
import time
from functools import wraps

def fix_sqlite():
    """Swaps standard sqlite3 for pysqlite3 for Ubuntu 20.04 compatibility."""
    try:
        import pysqlite3
        sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
    except ImportError:
        pass

def track_time(func):
    """Measures how long Pixel takes to 'think'."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️  (Pixel thought for {end_time - start_time:.2f} seconds)")
        return result
    return wrapper