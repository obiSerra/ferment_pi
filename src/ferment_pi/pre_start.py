"""Pre start application check."""
import logging

import alembic.command
from alembic.config import Config
from tenacity import retry, stop_after_attempt, wait_fixed

from ferment_pi.database import get_session

logger = logging.getLogger(__name__)

max_tries = 60 * 1
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
)
def init():
    """Connect to Database."""

    try:
        with get_session() as session:
            session.execute("SELECT 1")
    except Exception as e:
        logger.error("Error connecting to Database: {}".format(e))
        raise e


def migrate():
    """Database Migration."""
    config = Config('alembic.ini')
    alembic.command.upgrade(config, 'head')
    print("DONE")


def main():
    """Start the script to check if database connection is working."""
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.critical("Pre Start Application failed")
    migrate()
