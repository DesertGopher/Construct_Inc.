from pydantic import BaseSettings
from pathlib import Path
import os


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str


CONF_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(os.path.abspath(CONF_DIR / 'config' / '.env'))

settings = Settings(
    _env_file=os.path.abspath(CONF_DIR / 'config' / '.env'),
    _env_file_encoding='utf-8',
)


# DB_USER = settings.DB_USER
# DB_PASSWORD = settings.DB_PASSWORD
# DB_HOST = settings.DB_HOST
# DB_NAME = settings.DB_NAME
# DB_PORT = settings.DB_PORT