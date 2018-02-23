# defining commands to be used in chat

# !/usr/bin/env python3
import re
import socket
import random
import requests
import json

s = socket.socket


def hello():
    hellovar = "hello"
    return hellovar


def eightball():
    eightballlist = ["No", "Yes", "Leave me alone", "I think we already know the answer to THAT",
                     "I'm not sure, I bet Manoli or Ron know though",
                     "My sources point to yes", "Could be yes, could be no, nobody knows!", "Maybe",
                     "Are you kidding me?", "You may rely on it", 'Outlook not so good', 'Don\'t count on it',
                     'Most likely', 'Without a doubt', 'As I see it, yes']
    return eightballlist


def bm():
    bmlist = ["Bronze 5 is too good for you", "You're terrible at this",
              "Your mother is a bronze 5 and your father smells of elderberries",
              "Crying yourself to sleep again tonight? Good.",
              "Is your father still out at the store? Don't worry, he'll come back soon",
              "If only someone cared...",
              "You must be a glutton for punishment eh?", "I bet you main yasuo",
              "You degenerate weeb lover", "Hey you tried, now if only that mattered...",
              'Trying for first in the Darwin awards? Go you!', "Nobody loves you, stop bothering me",
              "You have two parts of brain, 'left' and 'right'. In the left side, there's nothing right. "
              "In the right side, there's nothing left.", "It's better to let someone think you are an idiot than to "
                                                          "open your mouth and prove it."]
    return bmlist


def pythoncommands():
    pythoncommandsvar = 'https://giphertius.wordpress.com/2018/02/20/giphertius-python-commands/'
    return pythoncommandsvar


def github():
    githubvar = 'https://github.com/ZERG3R/PythonBot'
    return githubvar


def randomnumbergenerator():
    randnum = random.randint(1, 100)
    return randnum

def guessnumber():
    with open('allparts.txt', 'r') as f:
        allparts = f.read()
        print(allparts)
        if allparts is not None:
            username = re.search(r"\w+", allparts).group(0)
    # guesses_count = 0
    stringnum = str(randomnumbergenerator())
    print(stringnum)
    info = re.search(r"(guessnumber \d+)", allparts)
    number = info.group(0).split(" ")[1]
    if int(number) > randomnumbergenerator():
        toohigh = 'Number is too high! Try guessing lower'
        return toohigh
    elif int(number) < randomnumbergenerator():
        toolow = 'Number is too low! Try guessing higher'
        return toolow
    else:
        givecommand = '!give ' + username + ' ' + stringnum
        # msg_countdown += 1
        randomnumbergenerator()
        return givecommand


# JOIN MESSAGE
# JOIN MESSAGE
# JOIN MESSAGE
jsonData = requests.get(url='https://tmi.twitch.tv/group/user/zerg3rr/chatters').json()
users = jsonData['chatters']['viewers'] + jsonData['chatters']['moderators']
users = list(users)
print(users)
while True:
    # start_time = time.time()
    newuserlist = jsonData['chatters']['viewers'] + jsonData['chatters']['moderators']
    newuserlist = list(newuserlist)
    new_list = set(newuserlist) - set(users)
    fp = open("e:/Programming/projects/twitchbot/welcome_messages.json", 'r')
    messages = json.load(fp)
    users = newuserlist
    break
