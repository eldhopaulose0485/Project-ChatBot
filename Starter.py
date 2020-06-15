#
#   Project Chat-Bot
#

import datetime as dt
from googlesearch import search
import webview
import pyttsx3
import os




def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.run()


def init():
    print('\n############################')
    print('    Welcome To Chat-Bot')
    print('############################\n')
    cloak = str(dt.datetime.now()).split(' ')
    cloak = str(cloak[1]).split(':')
    if int(cloak[0]) < 12:
        print('Good Morning, I am your virtual Tour Guide')
    else:
        print('Good Afternoon, I am your virtual Tour Guide')
    print('Where do you want to explore today?')
    speak('Where do you want to explore today?')
    response = input()
    links = list(search('about ' + response, tld="co.in", num=10, stop=10, pause=2))
    # for j in links: 
    #     print(j)
    print(links[0])
    webview.create_window('Hello world', links[0])
    webview.start()


init()
