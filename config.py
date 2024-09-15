# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "23185038"
    API_HASH = "019e63043383f3b5e7c89c2431ec23dc"
    #TOKEN = ":"
    TOKEN = os.environ.get("TOKEN", "7162644889:AAH2KXiepZgT0NeqfnCzb9D8BpXccYcVyLs")
    MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["1280494242"])
