def sendWhisper(s, user, message):
    messageTemp = "PRIVMSG #jtv :.w" + user + " " + message
    s.send(messageTemp + "\r\n")
    print("Whisper: " +messageTemp)
    sendWhisper(s, "zerg3rr", "testing")