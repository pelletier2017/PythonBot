# defining commands to be used in chat

# !/usr/bin/env python3
import re
import random


def hello():
    return "hello"


def eight_ball():
    return ["No", "Yes", "Leave me alone", "I think we already know the answer to THAT",
            "I'm not sure, I bet Manoli or Ron know though",
            "My sources point to yes", "Could be yes, could be no, nobody knows!", "Maybe",
            "Are you kidding me?", "You may rely on it", 'Outlook not so good', 'Don\'t count on it',
            'Most likely', 'Without a doubt', 'As I see it, yes']


def bm():
    bm_list = ["Bronze 5 is too good for you", "You're terrible at this",
               "Your mother is a bronze 5 and your father smells of elderberries",
               "Crying yourself to sleep again tonight? Good.",
               "Is your father still out at the store? Don't worry, he'll come back soon",
               "If only someone cared...",
               "You must be a glutton for punishment eh?", "I bet you main yasuo",
               "You degenerate weeb lover", "Hey you tried, now if only that mattered...",
               'Trying for first in the Darwin awards? Go you!', "Nobody loves you, stop bothering me",
               "You have two parts of brain, 'left' and 'right'. In the left side, there's nothing right. "
               "In the right side, there's nothing left.",
               "It's better to let someone think you are an idiot than to open your mouth and prove it."]
    return random.choice(bm_list)


def python_commands():
    return 'https://giphertius.wordpress.com/2018/02/20/giphertius-python-commands/'


def github():
    return 'https://github.com/ZERG3R/PythonBot'


def guess_number(message):

    secret_num = random.randint(1, 100)
    guess_regex = re.search(r"(guessnumber \d+)", message)
    guess = guess_regex.group(0).split(" ")[1]

    if int(guess) > secret_num:
        response = 'Number is too high! Try guessing lower'
    elif int(guess) < secret_num:
        response = 'Number is too low! Try guessing higher'
    else:
        response = "YOU GOT IT!"

    #else:
    #    give_command = '!give ' + username + ' ' + string_num
    #    # msg_countdown += 1
    #    random_number_generator()

    return response + " btw the answer was " + str(secret_num)


def feel_good():
    feel_good_list = ["You're more fun than a ball pit filled with candy. "
                      "(And seriously, what could be more fun than that?)",
                      "That thing you don't like about yourself is what makes you so interesting.",
                      "If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener.",
                      "The people you love are lucky to have you in their lives.",
                      "Our community is better because you're in it.",
                      "You inspire me.",
                      "You have a gift for making people comfortable.",
                      "You are nothing less than special.",
                      "You always make people smile.",
                      "You have a heart of gold.",
                      "I like the way you are.",
                      "Thanks for being there for me.",
                      "You inspired me to become a better person.",
                      "You smell good today.",
                      "I am honored to get to know you.",
                      "You are so talented!",
                      "I will be here to support you on your decisions.",
                      "I believe in you."
                      ]
    return random.choice(feel_good_list)

