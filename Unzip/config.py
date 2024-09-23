import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7589637467:AAEq_48MmI__NKt6akMzVXwwa-QTXT9HoYc")
    API_ID = int(os.environ.get("API_ID", 14681595))
    API_HASH = os.environ.get("API_HASH", "a86730aab5c59953c424abb4396d32d5")
    
    
