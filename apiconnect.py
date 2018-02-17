import requests
import time
import sys

def main():

    r_initial = requests.get('https://api.twitch.tv/kraken/channels/zerg3rr/follows')
    current_follower_num = r_initial.json()['_total']
