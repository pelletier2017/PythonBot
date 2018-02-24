#!/usr/bin/env python3

import datetime


def formatted_time():
    current_time = datetime.datetime.now()
    return "{:%H:%M})".format(current_time)
