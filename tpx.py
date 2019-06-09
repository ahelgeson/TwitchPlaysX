#!/usr/bin/env python
# Twitch Plays X
# Inpsired by http://twitch.tv/twitchplayspokemon and forked from Aidan
# Thomson's Twitch Plays repo: https://github.com/aidanrwt/twitch-plays. Many
# thanks to Aidan for creating and sharing this. This will only work with
# Python2. I plan on porting this to Python3 in the future.

from sys import exit
from config.config import config
import lib.bot as bot

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
