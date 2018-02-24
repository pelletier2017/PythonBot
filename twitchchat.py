#!/usr/bin/env python3

import datetime
import os

import cfg
import msgtime


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


def save_bot_response(msg):
    today = datetime.date.today()
    save_path = "chat_history/"
    complete_name = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
    # writes each message to the file
    with open(complete_name, 'a', encoding='utf-8') as f:
        to_file = msgtime.formatted_time() + msg
        f.write(to_file)
    print(msgtime.formatted_time, msg)