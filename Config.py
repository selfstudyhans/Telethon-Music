import os

class Config(object):
    API_ID =22049318 int(os.environ.get("API_ID", "6213538"))
    API_HASH =f3f1ff073b35b28792c6c197b6474f82 os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN =8184535242:AAEbTs-57ac353KMApUmwaW97dtOBLNxUsM os.environ.get("BOT_TOKEN", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = @shauryapr_bot os.environ.get("BOT_USERNAME", "")
    SUPPORT =https://t.me/+K_o_uEDLAygxODI1 os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL =https://t.me/+RTvuyT5kaKY3ODA1 os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = 6695335986 int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
