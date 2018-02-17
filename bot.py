# http://www.instructables.com/id/Twitchtv-Moderator-Bot/
#!/usr/bin/env python3

from StreamPythonbotbroke import cfg
from StreamPythonbotbroke import msgtime
import os.path
import socket
import datetime
from time import sleep
# import re


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
    #print("Test complete")


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


while True:
    response = s.recv(1024).decode("utf-8")

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
        sleep(1 / cfg.RATE)

    # otherwise prints text and writes to file
    else:

        # creates the file path using the date
        today = datetime.date.today()
        save_path = 'E:/Files'
        completeName = os.path.join(save_path, str(today) + cfg.CHAN + ".txt")
        with open(completeName, 'a', encoding='utf-8') as f:

            # this breaks up the response so you can have a simpler/nicer looking output
            semi = response.find(' :')
            exclam = response.find('!')
            part1 = response[1:exclam]
            part3 = response[semi:]
            part3 = part3.strip(' ')
            allparts = (part1 + ' ' + part3)

            # writes the lines to the file
            toFile = (msgtime.formatted_time + allparts + "\n")
            f.write(toFile)
            print(msgtime.formatted_time)
            print(allparts)
            cfg.sleep(0.5)

        print("test6")
        if "hello" in allparts:
            chat(s, 'Hello')
