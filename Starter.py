#
#   Project Chat-Bot
#

import datetime as dt
from googlesearch import search
import pyttsx3
import webbrowser
import time
import airports as ap

engine = pyttsx3.init()
engine.setProperty('rate', 170)


def placeCheck(links):
    for link in links:
        if str(link).find(response) >= 0:
            return True
    else:
        return False


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
        speak('Good Morning, I am your virtual Tour Guide.')
    else:
        print('Good Afternoon, I am your virtual Tour Guide')
        speak('Good Afternoon, I am your virtual Tour Guide.')
    placeFix()


def placeFix(secondCall=False):
    print('Where do you want to explore today?')
    speak('Where do you want to explore today?')
    global response
    while 1:
        response = input()
        links = list(search('tourist attractions of  ' + response,
                            tld="com", num=10, stop=10, pause=2))
        if (not placeCheck(links)) or (response + '\n' in engWordsList()):
            print('Please provide the name of a place to proceed')
            speak('Please provide the name of a place to proceed')
        else:
            break
    for link in links:
        if link.find('tripadvisor') >= 0:
            print('Here are the Attractions of ' + response)
            speak('here are the Attractions of ' + response)
            webbrowser.open(link, new=2)
            break
    else:
        print('Here are the Attractions of ' + response)
        speak('here are the Attractions of ' + response)
        webbrowser.open(str(links[0]), new=2)
    time.sleep(5)
    print('Do you want to fix ' + response + ' or change?')
    speak('Do you want to fix ' + response + ' or change?')
    while 1:
        fixResponse = input().lower()
        if fixResponse.find('change') >= 0:
            placeFix(True)
            break
        elif fixResponse.find('fix') >= 0:
            print(response + ' Fixed as destination')
            speak(response + ' Fixed as destination')
            break
        else:
            print('Do you want to fix ' + response + ' or change?')
            speak('Do you want to fix ' + response + ' or change?')
    if not secondCall:
        step2()
    else:
        pass


def step2():
    print('Do you want to see the map of ' + response + '?')
    speak('Do you want to see the map of ' + response + '?')
    mapRespond = input().lower()
    if mapRespond.find('ye') >= 0 or mapRespond.find('ok') >= 0 or mapRespond.find('see') >= 0:
        print('Here is the map of ' + response)
        speak('here is the map of ' + response)
        webbrowser.open('https://www.google.com/maps/place/' + response, new=2)
        time.sleep(10)
    roomsFind()


def roomsFind():
    print('Then do you want to see available hotels in ' + response)
    speak('Then do you want to see available hotels in ' + response)
    roomRespond = input()
    if roomRespond.find('ye') >= 0 or roomRespond.find('ok') >= 0 or roomRespond.find('see') >= 0:
        print("What type of hotels you are expecting?: ")
        speak("What type of hotels you are expecting?: ")
        hotelType = input()
        links = list(search(hotelType + 'oyo rooms in ' + response,
                            tld="com", num=1, stop=1, pause=2))
        print('Here are the ' + hotelType + ' Hotels in ' + response)
        speak('Here are the ' + hotelType + ' Hotels in ' + response)
        webbrowser.open(links[0], new=2)
        time.sleep(10)


def flightbook():
    print('Tell me your current location')
    speak('Tell me your current location')
    loc = input()
    while 1:
        if not ap.airpcheck(loc):
            print('There is no AirPort in this location.')
            speak('There is no AirPort in this location.')
            print('Tell me the state of your location')
            speak('Tell me the state of your location')
            tstate = input()
            if ap.statecheck(tstate):
                print('Here are the available airports in ' + tstate)
                speak('Here are the available airports in ' + tstate)
                ap.printstate(tstate)
                print('Choose the AirPort of your location')
                speak('Choose the AirPort of your location')
                loc = input()
        else:
            break
    print('Tell me the AirPort of your destination')
    speak('Tell me the AirPort of your destination')
    dairp = input()
    while 1:
        if not ap.airpcheck(dairp):
            print('There is no AirPort in this location.')
            speak('There is no AirPort in this location.')
            print('Tell me the state of destination')
            speak('Tell me the state of destination')
            tstate = input()
            if ap.statecheck(tstate):
                print('Here are the available airports in ' + tstate)
                speak('Here are the available airports in ' + tstate)
                ap.printstate(tstate)
                print('Choose the AirPort of your destination')
                speak('Choose the AirPort of your destination')
                dairp = input()
        else:
            break
    print('Enter date in the format dd/mm/yyyy')
    speak('Enter date in the format as given')
    date = input().split('/')
    flightlink = 'https://flight.yatra.com/air-search-ui/seodom/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=' + ap.placetocode(
        loc) + '&originCountry=IN&destination=' + ap.placetocode(dairp) + '&destinationCountry=IN&flight_depart_date=' + \
                 date[0] + '%2F' + date[1] + '%2F' + date[2] + '&ADT=1&CHD=0&INF=0&preferred=&class=Economy&source=seo'
    webbrowser.open(flightlink, new=2)


def callcab():
    print('Which taxi service do you need? Uber or OlaCab')
    speak('Which taxi service do you need? Uber or OlaCab')
    taxys = input()
    if taxys.find('uber') >= 0:
        webbrowser.open('https://www.olacabs.com/', new=2)
    else:
        webbrowser.open('https://www.uber.com/in/en/', new=2)


def trainbook():
    print('Tell me the starting point')
    speak('Tell me the starting point')
    spoint = input()
    print('Tell me the destination point')
    speak('Tell me the destination point')
    dpoint = input()
    links = list(search('book train from ' + spoint + 'to ' + dpoint,
                        tld="com", num=1, stop=1, pause=2))
    print('Here are the available trains from ' + spoint + ' to ' + dpoint)
    speak('Here are the available trains from ' + spoint + ' to ' + dpoint)
    webbrowser.open(links[0], new=2)


def finalStep():
    brk = False
    while 1:
        print('I am waiting for your response to help you')
        speak('I am waiting for your response to help you')
        wordList = [('plane', 'flight', 'air'), ('train', 'rail'),('bus', 'ticket', 'tickets'), ('cab', 'taxi')]
        query = input().lower()
        squery = query.split(' ')
        for word in squery:
            if word in wordList[0]:
                print('Here you can book  flight tickets')
                speak('Here you can book  flight tickets')
                flightbook()
                break
            elif word in wordList[3]:
                print('Here you can book Taxi tickets')
                speak('Here you can book  Taxi tickets')
                callcab()
                break
            elif word in ['pnr']:
                print('Enter PNR Number')
                speak('Enter PNR Number')
                pnr = input()
                webbrowser.open('https://erail.in/pnr-status/' + pnr, new=2)
                break
            elif word in wordList[1]:
                print('Here you can book train tickets')
                speak('Here you can book train tickets')
                trainbook()
                break
            elif word in ['explore']:
                brk = True
                break
            elif word in wordList[2]:
                print('Here you can book bus tickets')
                speak('Here you can book bus tickets')
                webbrowser.open('https://www.makemytrip.com/bus-tickets/', new=2)
                break
            elif word in ['thankyou']:
                print('Dont mention it. I am always happy to help you')
                speak('Dont mention it. I am always happy to help you')
                break
        else:
            print('I cant understand what you are trying to say')
            speak('I cant understand what you are trying to say')
        if brk:
            break
    placeFix()


init()
finalStep()
