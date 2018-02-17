"""#!/usr/bin/python
import socket
import cfg

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
            self.irc.send("PRIVMSG " + chan + " " + msg + "n")

    def connect(self, server, channel, botnick):
        #defines the socket
        print ("connecting to:"+server)
        self.irc.connect((server, 6667))
        self.irc.send(("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!n"))
        self.irc.send("NICK " + botnick + "n")
        self.irc.send("JOIN " + channel + "n")

    def get_text(self):
        text =  self.irc.recv(2040)

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split() [1] + 'rn')

            return text



s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(oauth:ib74ojtkqgux11lmoykpoc719co3zq).encode("utf-8"))
s.send("NICK {}\r\n".format(giphertius).encode("utf-8"))
s.send("JOIN {}\r\n".format(zerg3rr).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")
    print(response)
    sleep(0.5)

"""
