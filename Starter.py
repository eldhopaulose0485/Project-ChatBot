#
#   Project Chat-Bot
#

import datetime as dt
from googlesearch import search
import webview
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

response = ''

def speak(word):
    engine.say(word)
    engine.runAndWait()
    engine.stop()


def init():
    print('\n####################################')
    print('   Welcome To virtual Tour Guide')
    print('####################################\n')
    cloak = str(dt.datetime.now()).split(' ')
    cloak = str(cloak[1]).split(':')
    if int(cloak[0]) < 12:
        print('Good Morning, I am your virtual Tour Guide')
        speak('Good Morning, I am your virtual Tour Guide')
    else:
        print('Good Afternoon, I am your virtual Tour Guide')
        speak('Good Afternoon, I am your virtual Tour Guide')
    placeFix()


def placeFix():
    print('Where do you want to explore today?')
    speak('Where do you want to explore today?')
    global response
    response = input()
    links = list(search('tourist attractions of  ' + response,
                        tld="com", num=20, stop=20, pause=2))
    # print(links)
    for link in links:
        if str(link).find('tripadvisor') >= 0:
            webview.create_window(response, str(link))
            print('Here are the Attractins of ' + response)
            speak('here are the Attractins of ' + response)
            webview.start()
            break
    else:
        webview.create_window(response, str(links[0]))
    print('\nDo you want to fix ' + response + ' or change?')
    speak('Do you want to fix ' + response + ' or change?')
    while(1):
        fixResponse = input().lower()
        if fixResponse.find('change') >= 0:
            placeFix()
            break
        elif fixResponse.find('fix') >= 0:
            print(response + ' Fixed as destination')
            speak(response + ' Fixed as destination')
            break
        else:
            print('Do you want to fix ' + response + ' or want change?')
            speak('Do you want to fix ' + response + ' or want change?')
    step2()


def step2():
    print('Do you want to know attractions of ' + response + '?')
    speak('Do you want to know attractions of ' + response + '?')
    


init()
