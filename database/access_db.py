# (c) @AbirHasan2005

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from database.database import Database

db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
