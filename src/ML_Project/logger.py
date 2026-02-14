import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(name: str = __name__, level: int = logging.INFO, log_dir: str = "logs", log_file: str = "app.log") -> logging.Logger:
    """Create and return a configured logger.

    - Adds a stream handler and a rotating file handler.
    - Safe to call multiple times; will not add duplicate handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    # ensure log directory exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    fmt = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s")

    sh = logging.StreamHandler()
    sh.setLevel(level)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    fh = RotatingFileHandler(
        filename=str(log_path / log_file), maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    fh.setLevel(level)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger


if __name__ == "__main__":
    lg = get_logger("ML_Project.logger")
    lg.info("Logger initialized successfully")
