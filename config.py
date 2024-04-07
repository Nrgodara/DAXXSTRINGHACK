# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "23185038"
    API_HASH = "019e63043383f3b5e7c89c2431ec23dc"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    #MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    MONGO_URL = "mongodb+srv://mrmahendrji:Mahendra321@cluster0.miaccbn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["1280494242"])
