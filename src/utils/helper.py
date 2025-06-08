import uvicorn

from src.config.config import settings
from src.utils.logger import logger


def run_server() -> None:
    """Starts the Uvicorn server with specified settings.

    This function initializes and runs the Uvicorn server, 
    logging the server's start and handling any exceptions that may occur.
    """
    logger.info("🚀 Starting Uvicorn server on port 8000")
    try:
        # Run the Uvicorn server with the specified app and settings
        uvicorn.run("src.main:app", port=8000, reload=settings.reload, workers=4)
    except Exception as e:
        logger.exception(f"❌ Failed to start server: {e}")