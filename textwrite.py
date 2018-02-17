#!/usr/bin/env python3

import datetime
import os.path
import bot

today = datetime.date.today()

save_path = 'E:/Files'
completeName = os.path.join(save_path, str(today)+".txt")
file1 = open(completeName, "a")

toFile = (bot.PRIVMSG + "/n")
file1.write(toFile)

