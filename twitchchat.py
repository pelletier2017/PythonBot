#!/usr/bin/env python3
from twitchbot import cfg


def chat(sock, msg):
    """
   send a chat message to the server
   Keyboard arguments:
   sock -- the socket over which to send the message
   msg -- the message to be sent
   """
    full_msg = "PRIVMSG {} :{}\n".format(cfg.CHAN, msg)
    msg_encoded = full_msg.encode("utf-8")
    print(msg_encoded)
    sock.send(msg_encoded)

# this breaks up the response so you can have a simpler/nicer looking output


