import sys
import time
from typing import Callable, Any

def fix_sqlite() -> None:
    """Redirects sqlite3 to pysqlite3 for Ubuntu 20.04 compatibility."""
    try:
        __import__('pysqlite3')
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    except ImportError:
        pass

def track_time(func: Callable) -> Callable:
    """Decorator to measure how long the AI takes to think."""
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  (Thought for {end - start:.2f} seconds)")
        return result
    return wrapper