from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from src.utils.logger import logger


class Settings(BaseSettings):
    """
    Configuration settings for the application, including database and JWT settings.
    """
    database_url: str = "sqlite:///./data/test.db"
    public_key_path: str = "secrets/public.pem"
    private_key_path: str = "secrets/private.pem"
    reload: bool = True
    JWT_ALGORITHM: str = "RS256"
    JWT_EXPIRATION_MINUTES: int = 60
    JAEGER_HOST: str = "localhost"
    JAEGER_PORT: int = 6831
    JAEGER_OTLP_GRPC_ENDPOINT: str = "localhost:4317"
    JAEGER_OTLP_HTTP_ENDPOINT: str = "http://localhost:4318/v1/traces"
    JAEGER_MODE: str = "otlp-grpc"
    JAEGER_SERVICE_NAME: str = "fastapi-app"

    @property
    def private_key(self):
        """
        Reads and returns the private key from the specified path.
        """
        return Path(self.private_key_path).read_text()

    @property
    def public_key(self):
        """
        Reads and returns the public key from the specified path.
        """
        return Path(self.public_key_path).read_text()

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
logger.info("⚙️ Application settings loaded")