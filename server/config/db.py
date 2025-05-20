from os import getenv

from dotenv import load_dotenv


def get_database_url() -> str:
    load_dotenv()
    user = getenv("POSTGRES_USER", "postgres")
    password = getenv("POSTGRES_PASSWORD", "")
    host = getenv("POSTGRES_HOST", "localhost")
    port = getenv("POSTGRES_PORT")
    db = getenv("POSTGRES_DB", "postgres")

    if port:
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
    else:
        return f"postgresql+asyncpg://{user}:{password}@{host}/{db}"


DATABASE_URL = get_database_url()
