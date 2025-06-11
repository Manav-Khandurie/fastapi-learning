# app/logger.py

import sys
from datetime import datetime
from pathlib import Path

from loguru import logger

# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Log file name with timestamp
log_file = LOG_DIR / f"fastapi_{datetime.now().strftime('%Y-%m-%d')}.log"

# Clear existing handlers (especially default one)
logger.remove()

# Add stdout and file sinks
logger.add(sys.stdout, level="INFO", format="{time} | {level} | {message}")
logger.add(
    log_file,
    rotation="00:00",  # Daily log rotation
    retention="7 days",  # Retain for 7 days
    compression="zip",  # Compress old logs
    level="DEBUG",  # File gets more verbose logs
    format="{time} | {level} | {name}:{function}:{line} - {message}",
)

# class InterceptHandler(logging.Handler):
#     """Custom logging handler to intercept log records and forward them to loguru."""
#     def emit(self, record):
#         """Emit a log record."""
#         level = (
#             logger.level(record.levelname).name
#             if record.levelname in logger._core.levels
#             else record.levelno
#         )
#         logger.log(level, record.getMessage())

# logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)