"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f'{os.getcwd()}/Himawari/{config}', 'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Himawari"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID=9429810 ##api id from my.telegram.org
    APP_ID=9429810 #same as API_ID
    API_HASH="06007846a1793a9883596434b299d0ed" ##api hash from my.telegram.org
    APP_HASH="06007846a1793a9883596434b299d0ed" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL="mongodb+srv://Mongo_Db_Bot:@cluster0.hct06fi.mongodb.net/?retryWrites=true&w=majority
" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://meowhisswswuj7.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="xlXk5IE4LsdK7O-PqT6NHUOAtljPoKGS@mouse.db.elephantsql.com" #postgres sql database link
    REDIS_URL="redis://default:CkBvvgB6WTZdNauXBXF6ILvtDTJv7hZA@redis-16130.c212.ap-south-1-1.ec2.cloud.redislabs.com:16130/Akash-free-db
" #redis database url from redislabs.com
    TOKEN="5783163434:AAHmvt9e455Zji7ii8IFNTDnMAdmcuaXL-Q" #bot token from @BotFather
    DEV_USERS=[5298587903] #developers id
    DRAGONS=[] #sudo users id
    DEMONS=[] #support user ids
    TIGERS=[] #commas for multiple ids
    WOLVES=[] #commas for multiple ids 
    DONATION_LINK="" #u can change with yours
    EVENT_LOGS=-1001427087906 #channel id for gban logs
    JOIN_LOGGER=-1001427087906  #log channel/group id
    OWNER_ID=1611359278 #owner id in integer
    ERROR_LOGS=-1001427087906 #support group id
    BOT_ID =5783163434  #id of bot in integer value
    BOT_NAME="Anubis" #your bot name
    ARQ_API_KEY="RAOQXI-ELCWVX-HGSFGY-HVWNDD-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="YonkoXHQ" #support group username without @
    OWNER_USERNAME="Ricky_animeboy" #owner username without @
    UPDATES_CHANNEL="yonkosdemonlogs" #Updates/News Channel username without @
    BOT_USERNAME="yonkoXprobot" #bot username without @
    REM_BG_API_KEY="" #not necessary
    GENIUS_API_TOKEN="" # api token from genius.com (not necessary)
    TIME_API_KEY="" #not necessary
    SPAMWATCH_API="J968E_20LgxrKjsdN24cqYtD~gNRTbU" #spamwatch api token from @SpamWatchBot
    WALL_API="" #wall api (not necessary)


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
