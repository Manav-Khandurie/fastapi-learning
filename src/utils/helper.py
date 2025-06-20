import uvicorn

from src.config.config import settings
from src.utils.logger import logger


def run_server() -> None:
    """Starts the Uvicorn server on port 8000.

    This function initializes and runs the Uvicorn server,
    using the application defined in 'src.main:app'. It logs
    the server start and handles any exceptions that may occur
    during the startup process.
    """
    logger.info("🚀 Starting Uvicorn server on port 8000")
    try:
        # Run the Uvicorn server with specified parameters
        uvicorn.run("src.main:app", port=8000, reload=settings.reload, workers=4)
    except Exception as e:
        # Log any exceptions that occur during server startup
        logger.exception(f"❌ Failed to start server: {e}")