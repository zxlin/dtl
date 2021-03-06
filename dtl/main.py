import os
import logging

from dotenv import load_dotenv

from dtl.bot import LeagueBot

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    load_dotenv()
    debug = os.getenv("ENV") == "development"
    token = os.getenv("BOT_TOKEN")

    logging.basicConfig(level=logging.INFO)

    bot = LeagueBot(debug)
    logger.info("Starting bot!")
    bot.run(token)
