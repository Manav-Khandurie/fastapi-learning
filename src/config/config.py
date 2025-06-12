from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from src.utils.logger import logger


class Settings(BaseSettings):
    """
    Configuration settings for the application, including database and JWT settings.
    Inherits from BaseSettings to support environment variable loading.
    """

    database_url: str = "sqlite:///./data/test.db"  # Database connection URL
    public_key_path: str = "secrets/public.pem"  # Path to the public key file
    private_key_path: str = "secrets/private.pem"  # Path to the private key file
    reload: bool = True  # Flag to enable/disable auto-reload
    JWT_ALGORITHM: str = "RS256"  # JWT signing algorithm
    JWT_EXPIRATION_MINUTES: int = 60  # JWT expiration time in minutes
    JAEGER_HOST: str = "localhost"  # Jaeger host for tracing
    JAEGER_PORT: int = 6831  # Jaeger port for tracing
    JAEGER_OTLP_GRPC_ENDPOINT: str = "localhost:4317"  # OTLP gRPC endpoint for Jaeger
    JAEGER_OTLP_HTTP_ENDPOINT: str = (
        "http://localhost:4318/v1/traces"  # OTLP HTTP endpoint for Jaeger
    )
    JAEGER_MODE: str = "otlp-grpc"  # Mode for Jaeger (e.g., otlp-grpc)
    JAEGER_SERVICE_NAME: str = "fastapi-app"  # Service name for Jaeger

    @property
    def private_key(self):
        """
        Reads and returns the private key from the specified file path.
        """
        return Path(self.private_key_path).read_text()

    @property
    def public_key(self):
        """
        Reads and returns the public key from the specified file path.
        """
        return Path(self.public_key_path).read_text()

    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )  # Configuration for environment variable loading


settings = Settings()  # Instantiate the Settings class
logger.info(
    "⚙️ Application settings loaded"
)  # Log that the application settings have been loaded