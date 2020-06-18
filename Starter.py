#
#   Project Chat-Bot
#

import datetime as dt
from googlesearch import search
import webview
import pyttsx3
import webbrowser


engine = pyttsx3.init()
engine.setProperty('rate', 150)


def engWordsList():
    englishwords = open('Databases/english_words.txt')
    wordslist = englishwords.readlines()
    return wordslist


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


def placeFix(secondCall=False):
    print('Where do you want to explore today?')
    speak('Where do you want to explore today?')
    global response
    while 1:
        response = input()
        if response + '\n' in engWordsList():
            print('Please provide the name of a place to proceed')
            speak('Please provide the name of a place to proceed')
        else:
            break
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
        print('Here are the Attractins of ' + response)
        speak('here are the Attractins of ' + response)
        webview.start()
    print('\nDo you want to fix ' + response + ' or change?')
    speak('Do you want to fix ' + response + ' or change?')
    while(1):
        fixResponse = input().lower()
        if fixResponse.find('change') >= 0:
            placeFix(True)
            break
        elif fixResponse.find('fix') >= 0:
            print(response + ' Fixed as destination')
            speak(response + ' Fixed as destination')
            break
        else:
            print('Do you want to fix ' + response + ' or want change?')
            speak('Do you want to fix ' + response + ' or want change?')
    if secondCall == False:
        step2()
    else:
        pass


def step2():
    print('Do you want to see the map of ' + response + '?')
    speak('Do you want to see the map of ' + response + '?')
    mapRespond = input().lower()
    if mapRespond.find('ye') >= 0 or mapRespond.find('ok') >= 0 or mapRespond.find('see') >= 0:
        webview.create_window(
            response, 'https://www.google.com/maps/place/' + response)
        print('Here is the map of ' + response)
        speak('here is the map of ' + response)
        webview.start()
    roomsFind()


def roomsFind():
    print('Then do you want to see available rooms in ' + response)
    speak('Then do you want to see available rooms in ' + response)
    roomRespond = input()
    if roomRespond.find('ye') >= 0 or roomRespond.find('ok') >= 0 or roomRespond.find('see') >= 0:
        print("What type of hote you are expecting?: ")
        speak("What type of hote you are expecting?: ")
        hotelType = input()
        links = list(search(hotelType + 'oyo rooms in ' + response,
                            tld="com", num=1, stop=1, pause=2))
        print('Hre are the available Hotels in ' + response)
        speak('Hre are the available Hotels in ' + response)
        webbrowser.open(links[0], new=2)
    print('I am waiting here for your response to help you\n')
    speak('I am waiting here for your response to help you')


init()
