Twitch Plays X
================

Inpsired by http://twitch.tv/twitchplayspokemon and forked from Aidan Thomson's
Twitch Plays repo: https://github.com/aidanrwt/twitch-plays. Many thanks to
Aidan for creating and sharing this. This will only work with Python2. I plan on
porting this to Python3 in the future.

Installation
------------

**NOTE:** Python 2 must be installed on the machine that will run this.

Download/clone this into your preferred directory, and edit the
`config/config.py` file to inlcude your twitch username and
[OAuth token](http://www.twitchapps.com/tmi/).

**NOTE:** Be sure to secure this token! Anyone who has this can stream on your
channel. 

### Emulator Setup

You could run the bot now and it should mostly work depending on your
emulator key input, but it's best to customize a bit more for a flawless setup 
and some better features. In whichever emulator you are going to use, set the
inputs to:
```
Up: 0
Down: 1
Left: 2
Right: 3
A Button: 4
B Button: 5
Start: 6
Select: 7
```
For emulators of systems that have more buttons (e.g. N64 C, Z, and shoulder 
buttons), you can use whatever keys you won't be using normally on the host
machine. More info can be found in the `config.py` file comments.

### Config Setup

All configuration is done within `config.py`, with the exception of `game.py`,
which holds the dictionary for the strings you'd like to accept in your chat to
do a command, and how long you'd like that command to last. Customization in
the config file includes:
* Keyword or spam throttling
* Hold-down key functionality
* Burst-key or spam-key functionality
* Command line display height of chat inputs

### Final Step!

Once you have your emulator and config set, open Command Prompt, move into the
directory where this was saved (e.g. `cd C:\\User\Desktop\TwitchPlaysX`) and run
the command: `python tpx.py`. **NOTE:** Your emulator will have to be the active
window once this is launched for it to accept any input. Make sure it is in
focus before testing.

### Questions/Comments

If you need help or have questions, feel free to file a bug on Github or
[message me on twitch](http://www.twitch.tv/message/compose?to=toastviking).
