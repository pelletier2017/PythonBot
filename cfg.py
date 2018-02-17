#!/usr/bin/env python3

from time import sleep

HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "giphertius"
PASS = "oauth:ib74ojtkqgux11lmoykpoc719co3zq"
CHAN = "#zerg3rr"

RATE = (20/30) #messages per seconds

PATT = [
    r"swear",
    "hello"
    r"some_pattern"
]
