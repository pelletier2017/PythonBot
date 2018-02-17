#!/usr/bin/env python3

from StreamPythonbotbroke import cfg
from StreamPythonbotbroke import msgtime
import os.path
import socket
import datetime
from time import sleep


def chat(sock, msg):
    """
    send a chat message to the server
    Keyboard arguments:
    sock -- the socket over which to send the message
    msg -- the message to be sent
    """
    full_msg = "PRIVMSG ${} :{}".format(cfg.CHAN, msg)
    msg_encoded = full_msg.encode("utf-8")
    sock.send(msg_encoded)
    print("Test complete")


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

s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
print("")
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))


while True:
    response = s.recv(1024).decode("utf-8")
    if len(response) == 0:
        print("disconnected")
        s = socket.socket()
        s.connect((cfg.HOST, cfg.PORT))
        s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
        s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
        s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    # need this try except loop for any foreign characters in response input
    try:

        # creates the file path using the date
        today = datetime.date.today()
        save_path = 'E:/Files'
        completeName = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
        file1 = open(completeName, "a")

        # this breaks up the response so you can have a simpler/nicer looking output
        semi = response.find(' :')
        exclam = response.find('!')
        part1 = response[1:exclam]
        part3 = response[semi:]
        part3 = part3.strip(' ')
        allparts = (part1 + ' ' + part3)

        # writes the lines to the file
        toFile = (msgtime.formatted_time + allparts + "/n")
        file1.write(toFile)
        print(msgtime.formatted_time)
        print(allparts)
        cfg.sleep(0.5)
        file1.close()
    except UnicodeEncodeError:
        print('Encode error, passing')
        pass


# is needed for when twitch servers decide to send out another ping so we can pong back
while True:
    response = s.recv(1024).decode("utf-8")
    response = response.decode('utf-8', 'ignore').encode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)
    sleep(1 / cfg.RATE)


def chat_msg():  # doesn't currently work
    pass

if "!test" in response:
    chat(s, "FKIN WORK PLEASE")

