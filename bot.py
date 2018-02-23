# http://www.instructables.com/id/Twitchtv-Moderator-Bot/
# !/usr/bin/env python3

from time import sleep
from twitchbot import msgtime, cfg, botcommands, twitchchat
import os.path, sys, socket, datetime, re, random,  json
sys.path.append('e:/Programming/projects/twitchbot/botcommands')


def ban(sock, user):
    """
   Ban a user from the current channel.
   Keyword arguments:
   sock -- the socket over which to send the ban command
   user -- the user to be banned
   """
    twitchchat.chat(sock, ".ban{}".format(user))


def timeout(sock, user, secs=input()):
    """Time out a user for a period of time (input).
   Keyword arguments:
   sock -- the socket over which to send the timeout command
   user -- the user to be timed out
   secs --  the length of the timeout in seconds"""
    twitchchat.chat(sock, ".timeout {}".format(user, secs))


# connects us to IRC
s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
print("")
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))


while True:

    response = s.recv(1024).decode("utf-8")
    # this breaks up the response so you can have a simpler/nicer looking output

    chat_msg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    message = chat_msg.sub("", response)
    username = re.search(r"\w+", response).group(0)

    allparts = (username + ':' + ' ' + message)
    with open('allparts.txt', 'w', encoding='utf-8') as file:
        file.write(allparts)

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

        if '!pythoncommands' in allparts:
            twitchchat.chat(s, botcommands.pythoncommands())

        if '!joinmessage' in allparts:
            # try:
            message = re.search(r"(joinmessage .+)", allparts)
            joinmessage = ' '.join(message.group(0).split(" ")[1:])
            joinmessage = joinmessage.strip()
            botcommands.messages[username] = joinmessage
            with open('welcome_messages.json', 'w') as jfp:
                json.dump(botcommands.messages, jfp)
            # except:
                # pass
        # print(botcommands.new_list)
        for i in botcommands.new_list:
            print(i)
            if i in botcommands.messages:
                print(i)
                twitchchat.chat(s, botcommands.messages[i])

        if "!hello" in allparts:
            twitchchat.chat(s, botcommands.hello() + ' ' + username)

        if "!eightball" in allparts:
            twitchchat.chat(s, random.choice(botcommands.eightball()))

        if "!bm" in allparts:
            twitchchat.chat(s, random.choice(botcommands.bm()))

        if '!github' in allparts:
            twitchchat.chat(s, botcommands.github())

        if '!guessnumber' in allparts:
            twitchchat.chat(s, botcommands.guessnumber())
