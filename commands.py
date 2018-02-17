#!/usr/bin/env python3

import time
import bot
import cfg
#import argparse
#import numpy as np

def cleanMsg(response):
    chat_MSG =
chat_MSG = bot.re.compile(r"^:\w+!\w+@\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    return chat_MSG.sub("", response)

bot.chat(s, "I'm here!")

def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

chat_MSG = bot.re.compile(r"^:\w+!\w+@\.tmi\.twitch\.tv PRIVMSG #\w+ :")
time.sleep(30 / cfg.RATE)

while bot.PING or bot.PONG == True:
    print(str("I'm here"))




#simple hello command
if bot.response == "!hello":
    msg = "HELLO SCRUB"
    bot.s.send(msg)


cfg.CHAN.send_chat_message("I'm reading this!")



