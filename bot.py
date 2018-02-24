# http://www.instructables.com/id/Twitchtv-Moderator-Bot/
# !/usr/bin/env python3

from time import sleep
import datetime
import json
import os.path
import random
import re
import socket

# project specific imports
import msgtime
import cfg
import botcommands
import twitchchat

# if it works without this line i think we should remove it
#sys.path.append('e:/Programming/projects/twitchbot/botcommands')


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
    complete_name = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
    # writes each message to the file
    with open(complete_name, 'a', encoding='utf-8') as f:
        to_file = msgtime.formatted_time() + all_parts
        f.write(to_file)
    print(msgtime.formatted_time(), all_parts)


def connect_socket():
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))
    return s


def handle_commands(all_parts, message, s, username):

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
        message = re.search(r"(joinmessage .+)", all_parts)
        join_message = ' '.join(message.group(0).split(" ")[1:])
        join_message = join_message.strip()
        botcommands.messages[username] = join_message
        with open('welcome_messages.json', 'w') as jfp:
            json.dump(botcommands.messages, jfp)


def main():

    s = connect_socket()
    while True:

        response = s.recv(1024).decode("utf-8")
        # this breaks up the response so you can have a simpler/nicer looking output

        chat_msg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        message = chat_msg.sub("", response)
        username = re.search(r"\w+", response).group(0)
        all_parts = (username + ': ' + message)

        # this part is exactly the same as the file in chat_history
        # with open('allparts.txt', 'a', encoding='utf-8') as file:
        #    file.write(all_parts)

        # tests connection/reconnects if disconnect occurs
        if len(response) == 0:
            print("disconnected")
            s = connect_socket()

        # tests if we get a ping so we can pong back
        elif response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            print("PING PONG")
            sleep(1 / cfg.RATE)

        # otherwise prints text and writes to file
        else:
            save_to_file(all_parts)
            handle_commands(all_parts, message, s, username)


main()
