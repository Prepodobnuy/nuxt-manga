from io import StringIO
import sys
from functools import wraps
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)


def capture_output():
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            old_stdout, old_stderr = sys.stdout, sys.stderr
            out, err = StringIO(), StringIO()
            sys.stdout, sys.stderr = out, err

            try:
                result = func(*args, **kwargs)
                out_val, err_val = out.getvalue() or None, err.getvalue() or None

                if out_val:
                    logger.debug(f" \n{func.__code__}\n{out_val}")
                if err_val:
                    logger.error(f" \n{func.__code__}\n{err_val}")

                return result
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
                out.close()
                err.close()

        return wrapper

    return decorator


def error(s):
    print(s, file=sys.stderr)


def debug(s):
    print(s, file=sys.stdout)
