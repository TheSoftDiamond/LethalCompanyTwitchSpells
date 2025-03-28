# LethalCompanyTwitchSpells

This script is a modified version of the the [Twitch Speller](https://github.com/TheSoftDiamond/TwitchSpeller) here. This version of the software is setup to work with the Monster Hotkeys keybinds. I am uploading this project to help others who will be participating in the [planned Lethal Company stream](https://softdiamond.net/Lethal_March30_Stream/) with being able to use the Twitch Speller on their side.

As it currently stands, the code is set to look for a program called `Lethal Company.exe`. You may have to adjust the keybinds to suit your keyboard layout.

I would like to thank my friends and Jacon500 for helping me with this code to allow it to be possible.

Known issues:
Due to how twitch rate limits, words that have the same letter as before may get processed slower, this is just something I cannot control.

## Setup
To setup the code, you will need Python. The recommended version is Python 3.12.

Once that is done, you will need to run the following command to finish setup.

```pip install -r requirements.txt```

# Running the code

Once Python 3.12 is done, modify the settings.py file to your likings. You then can run the TwitchSpeller.py file and run it as normal.

# Note

This code is modified and based off of DougDoug's Twitch Plays Code which can be found at https://github.com/DougDougGithub/TwitchPlays

It also is modified from my own Twitch Speller:
https://github.com/TheSoftDiamond/TwitchSpeller
