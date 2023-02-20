## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBTZEh9JRGRgK3IWCwRBZWIOXAyRmyLyIK46JRrNnK1Axn0B7KEERYUQ76oMn6TNEauslrmW-ypPoWDlHV-y4t1kWeeI_w-qj4kwyGkypiErLSVU6ujSrRdGxWWBLzWEuM2euVsHKK7A-N5rzL9-HF2G3wNCnHCQV7fnn5JoepZMWOEqa7h2un5nZxZ6tdkRTPUnyOhBhi_J3xlwFe6cK6bd0UA9vxDY1lf5PWobPmq-hPnKYxkPLg9nQGyoWVk0TUM8qaCTAFerz4eY05Y3LtcDIfPaYXruM-MB0IZoW9cq2qm8tn9_Dx8viQM52wAmXUK0cTv_2Mpa1labDf08cq6AAAAATy6BAcA")
BOT_TOKEN = getenv("BOT_TOKEN", "6209867750:AAHvO1EpaZ8a23dsacwf86FT7frFMkMeF-s")
BOT_NAME = getenv("BOT_NAME", "nxtmusicbot")
API_ID = int(getenv("API_ID", "2790569"))
API_HASH = getenv("API_HASH", "7c72307ff7c7e44d2b416e551145f5ba")
OWNER_NAME = getenv("OWNER_NAME", "ragnar_zxc")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "YurikoPlugin")
BOT_USERNAME = getenv("BOT_USERNAME", "nxtmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5911954612").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
