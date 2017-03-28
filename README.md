# PythonBot
A twitch bot being written and updated in python 
Created by twitch.tv/zerg3rr and twitch user Thukor, updated thoroughly until a critical error was found.
Error encompassed foreign characters which were passed through the program, when it went to write to the notepad file (textwrite.py) it would crash the program and it would need to be restarted.
An example of this character would be " 漢字 "
