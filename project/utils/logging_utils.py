import logging
import os
from logging.handlers import RotatingFileHandler


def get_logger(name: str = __name__, level: int = logging.INFO, *, log_dir: str | None = None):
    """Create and return a configured logger.

    - Adds a StreamHandler (console) and a RotatingFileHandler (if `log_dir` is provided or default).
    - Idempotent: calling multiple times for same `name` won't add duplicate handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # File handler (rotating)
    try:
        if log_dir is None:
            # default to a `logs` directory next to this file
            here = os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(os.path.dirname(here), "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"{name.replace('.', '_')}.log")
        fh = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
        fh.setLevel(level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    except Exception:
        # Fail gracefully if file logging isn't possible
        logger.debug("Could not create file handler for logger '%s'", name, exc_info=True)

    return logger
