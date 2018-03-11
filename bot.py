# http://www.instructables.com/id/Twitchtv-Moderator-Bot/
# !/usr/bin/env python3

import time
import datetime
import json
import os.path
import random
import re
import requests
import socket
from datetime import timedelta


# project specific imports
from twitchbot import msgtime
from twitchbot import cfg
from twitchbot import botcommands
from twitchbot import twitchchat

WELCOME_MESSAGE_JSON = 'e:/Programming/projects/twitchbot/welcome_messages.json'


def ban(sock, user):
    """
   Ban a user from the current channel.
   Keyword arguments:
   sock -- the socket over which to send the ban command
   user -- the user to be banned
   """
    twitchchat.chat(sock, ".ban{}".format(user))


def timeout(sock, user, secs):
    """Time out a user for a period of time (input).
   Keyword arguments:
   sock -- the socket over which to send the timeout command
   user -- the user to be timed out
   secs --  the length of the timeout in seconds"""
    twitchchat.chat(sock, ".timeout {}".format(user, secs))


def save_to_file(all_parts):
    today = datetime.date.today()
    save_path = "chat_history/"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    complete_name = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
    # writes each message to the file
    with open(complete_name, 'a', encoding='utf-8') as f:
        to_file = msgtime.formatted_time() + all_parts
        f.write(to_file)
    print(msgtime.formatted_time(), all_parts)


def load_welcome_messages():
    file = open(WELCOME_MESSAGE_JSON, 'r')
    messages = json.load(file)
    return messages


def update_welcome_messages(messages, new_user, new_msg):
    messages[new_user] = new_msg
    with open(WELCOME_MESSAGE_JSON, 'w') as f:
        json.dump(messages, f)


def connect_socket():
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))
    return s


def get_viewers():
    channel_json = requests.get(url='https://tmi.twitch.tv/group/user/zerg3rr/chatters').json()
    viewers = (channel_json['chatters']['viewers'] + channel_json['chatters']['moderators'])
    return viewers


def handle_commands(s, username, message, welcome_messages):

    if message.startswith('!pythoncommands'):
        twitchchat.chat(s, botcommands.python_commands())

    elif message.startswith("!hello"):
        twitchchat.chat(s, botcommands.hello() + ' ' + username)

    elif message.startswith("!eightball"):
        twitchchat.chat(s, random.choice(botcommands.eight_ball()))

    elif message.startswith("!bm"):
        twitchchat.chat(s, botcommands.bm())

    elif message.startswith('!github'):
        twitchchat.chat(s, botcommands.github())

    elif message.startswith('!guessnumber'):
        twitchchat.chat(s, botcommands.guess_number(message))

    elif message.startswith('!feelgood'):
        twitchchat.chat(s, botcommands.feel_good())

    elif message.startswith('!joinmessage'):
        # takes all text after "!joinmessage " to use as join_message
        message_regex = re.search(r"(!joinmessage .+)", message)
        join_message = message_regex.group(0).split(" ", 1)[1].strip() + ' - ' + username

        update_welcome_messages(welcome_messages, username, join_message)
        twitchchat.chat(s, '!remove' + ' ' + '1000' + ' ' + username)

        # cooldown - if user welcome message used in last 5 minutes, skip


def main():
    last_time_welcomed = {}

    s = connect_socket()
    welcome_messages = load_welcome_messages()
    chat_regex = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    prev_viewers = set(get_viewers())

    while True:

        response = s.recv(1024).decode("utf-8")
        message = chat_regex.sub("", response)
        try:
            username = re.search(r"\w+", response).group(0)
            all_parts = (username + ': ' + message)

        # welcomes all new viewers
            viewers = set(get_viewers())

            new_viewers = viewers - prev_viewers
            for viewer in new_viewers:
                if viewer in welcome_messages:
                    last_updated = last_time_welcomed.get(viewer)
                    if last_updated is None or last_updated + timedelta(seconds=300) > datetime.datetime.now():

                        twitchchat.chat(s, welcome_messages[viewer])
                        last_time_welcomed[viewer] = datetime.time()

            prev_viewers = viewers

            # tests connection/reconnects if disconnect occurs
            if len(response) == 0:
                print("disconnected")
                s = connect_socket()

            # tests if we get a ping so we can pong back
            elif response == "PING :tmi.twitch.tv\r\n":
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
                print("PING PONG")
                time.sleep(1 / cfg.RATE)

            # otherwise prints text and writes to file
            else:
                save_to_file(all_parts)
                handle_commands(s, username, message, welcome_messages)

        except (AttributeError, ValueError, TypeError):
            pass


main()
