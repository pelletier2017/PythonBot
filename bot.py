#!/usr/bin/env python3

import cfg
import msgtime
#import commands
import os.path
import socket
import datetime
import re
from time import sleep
import sys


def chat(sock, msg):
    """
    send a chat message to the server
    Keyboard arguments:
    sock -- the socket over which to send the message
    msg -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban{}".format(user))

def timeout(sock, user, secs=input()):
    """
    Time out a user for a period of time (input).
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs --  the length of the timeout in seconds
    """
    chat(sock, ".timeout {}".format(user, secs))


s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
print("")
s.send("PASS {}\r\n".format("oauth:ib74ojtkqgux11lmoykpoc719co3zq").encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")

    if len(response) == 0:
        print("disconnected")
        s = socket.socket()
        s.connect((cfg.HOST, cfg.PORT))
        s.send("PASS {}\r\n".format("oauth:ib74ojtkqgux11lmoykpoc719co3zq").encode("utf-8"))
        s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
        s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    today = datetime.date.today()
    save_path = 'E:/Files'
    completeName = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
    file1 = open(completeName, "a");
    toFile = (response + "/n")
    file1.write(toFile)
    #THIS IS WHERE THE ENCODING PROBLEM IS
    response = s.recv(1024).decode("utf-8", errors='replace')

    """response = s.recv(1024).decode("utf-8", "ignore")"""

    print(msgtime.formatted_time)
    print(response)
    cfg.sleep(0.5)
    file1.close()


while True:
    response = s.recv(1024).decode("utf-8")
    response = response.decode('utf-8', 'ignore').encode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)

while True:
    response = s.recv(1024).decode("utf-8")
    response = response.decode('utf-8', 'ignore').encode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)
    sleep(1 / cfg.RATE)

"""
def chat_MSG(response):
    chat_MSG = re.compile(r"^:\w+!\w+@\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    if "!test" in response:
        print("Testing, Testing, 1,2,3")
    #chat(s, "Testing, Testing, 1,2,3")
    #return chat_MSG.sub("", response)
"""

while True:
    response = s.recv(1024).decode("utf-8")
    response = response.decode('utf-8', 'ignore').encode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        print(username + ": " + cfg.message)
    sleep(1 / cfg.RATE)

while True:
    response = s.recv(1024).decode("utf-8")
    response = response.decode('utf-8', 'ignore').encode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        print(username + ": " + cfg.message)
        for pattern in cfg.PATT:
            if re.match(pattern, cfg.message):
                ban(s, username)
                break
        sleep(1 / cfg.RATE)




