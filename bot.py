# http://www.instructables.com/id/Twitchtv-Moderator-Bot/
# !/usr/bin/env python3


# create some dank commands
# russian roulette game, join channel message, hangman game (users can enter words), guess number game

from twitchbot import cfg
from twitchbot import msgtime
# from twitchbot import botcommands
import os.path
import socket
import datetime
from time import sleep
import re
import random


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


def ban(sock, user):
    """
   Ban a user from the current channel.
   Keyword arguments:
   sock -- the socket over which to send the ban command
   user -- the user to be banned
   """
    chat(sock, ".ban{}".format(user))


def timeout(sock, user, secs=input()):
    """Time out a user for a period of time (input).
   Keyword arguments:
   sock -- the socket over which to send the timeout command
   user -- the user to be timed out
   secs --  the length of the timeout in seconds"""
    chat(sock, ".timeout {}".format(user, secs))

# connects us to IRC
s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
print("")
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

randnum = random.randint(1, 1000)
guessnumbercount = 0
while True:
    response = s.recv(1024).decode("utf-8")
    # this breaks up the response so you can have a simpler/nicer looking output

    chat_msg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    message = chat_msg.sub("", response)
    username = re.search(r"\w+", response).group(0)

    allparts = (username + ':' + ' ' + message)

    # tests connection/reconnects if disconnect occurs
    if len(response) == 0:
        print("disconnected")
        s = socket.socket()
        s.connect((cfg.HOST, cfg.PORT))
        s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
        s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
        s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    # tests if we get a ping so we can pong back
    elif response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        print("PING PONG")
        sleep(1 / cfg.RATE)

    # otherwise prints text and writes to file
    else:

        # creates the file path using the date
        today = datetime.date.today()
        save_path = 'E:/Files'
        completeName = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
        with open(completeName, 'a', encoding='utf-8') as f:

            # writes the lines to the file
            toFile = (msgtime.formatted_time + allparts + "\n")
            f.write(toFile)
            print(msgtime.formatted_time, allparts)

            hello = "hello"
            eightball = ["No", "Yes", "Leave me alone", "I think we already know the answer to THAT",
                         "I'm not sure, I bet Manoli or Ron know though",
                         "My sources point to yes", "Could be yes, could be no, nobody knows!", "Maybe",
                         "Are you kidding me?", "You may rely on it", 'Outlook not so good', 'Don\'t count on it',
                         'Most likely', 'Without a doubt', 'As I see it, yes']
            bm = ["Bronze 5 is too good for you", "You're terrible at this",
                  "Your mother is a bronze 5 and your father smells of elderberries",
                  "Crying yourself to sleep again tonight? Good.",
                  "Is your father still out at the store? Don't worry, he'll come back soon",
                  "If only someone cared...",
                  "You must be a glutton for punishment eh?", "I bet you main yasuo",
                  "You degenerate weeb lover", "Hey you tried, now if only that mattered...",
                  'Trying for first in the Darwin awards? Go you!', "Nobody loves you, stop bothering me"]

            github = 'https://github.com/ZERG3R/PythonBot'

            if "hello" in allparts:
                chat(s, hello + ' ' + username)

            if "eightball" in allparts:
                chat(s, random.choice(eightball))

            if "bm" in allparts:
                chat(s, random.choice(bm))

            if 'github' in allparts:
                chat(s, github)

            if 'guessnumber' in allparts:
                number = 0
                stringnum = str(randnum)
                try:
                    info = re.search(r"(guessnumber \d+)", allparts)
                    number = info.group(0).split(" ")[1]
                except:
                    pass
                guessnumbercount += 1
                if guessnumbercount % 5 == 0:
                    if int(number) > randnum:
                        chat(s, 'Number is too high! Try guessing lower')
                    elif int(number) < randnum:
                        chat(s, 'Number is too low! Try guessing higher')
                elif stringnum in allparts:
                    chat(s, '!give ' + username + ' ' + stringnum)
                    randnum = random.randint(1, 1000)

            #if "!roulette" in allparts:
            #    botcommands.russian_roulette()
