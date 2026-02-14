from .logger import get_logger

# package-level logger for `from src.ML_Project import logger`
logger = get_logger("ML_Project")

__all__ = ["logger", "get_logger"]

