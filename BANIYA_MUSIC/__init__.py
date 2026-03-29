from BANIYA_MUSIC.core.bot import Sona
from BANIYA_MUSIC.core.dir import dirr
from BANIYA_MUSIC.core.git import git
from BANIYA_MUSIC.core.userbot import Userbot
from BANIYA_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
