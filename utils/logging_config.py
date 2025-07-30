import logging
import warnings
import os
from typing import Optional

def setup_logging(level: str = "INFO", log_file: Optional[str] = None):
    """
    Setup logging configuration to show only custom logs.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file to write logs to
    """
    # Suppress specific warnings
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="smolagents")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="httpx")
    warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="litellm")
    
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file) if log_file else logging.NullHandler()
        ]
    )
    
    # Suppress third-party library logs
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("litellm").setLevel(logging.WARNING)
    logging.getLogger("smolagents").setLevel(logging.WARNING)
    logging.getLogger("pydantic").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    
    # Set environment variables to suppress additional warnings
    os.environ["PYTHONWARNINGS"] = "ignore"
    os.environ["LITELLM_LOG"] = "ERROR"

def get_logger(name: str) -> logging.Logger:
    """Get a logger for the specified module."""
    return logging.getLogger(name)
