import os

from dotenv import load_dotenv

load_dotenv()

ALLOWED_TABLES = os.getenv("ALLOWED_TABLES", "7")
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:4200,http://127.0.0.1:4200")


def allowed_tables_list() -> list[int]:
    return [int(value.strip()) for value in ALLOWED_TABLES.split(",") if value.strip()]


def cors_origins_list() -> list[str]:
    return [origin.strip() for origin in BACKEND_CORS_ORIGINS.split(",") if origin.strip()]
