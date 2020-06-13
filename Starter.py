#
#   Project Chat-Bot
#

import datetime as dt


def init():
    # udata = open('userdata.cbdb', 'w')
    print('############################')
    print('    Welcome To Chat-Bot')
    print('############################')
    # udata.write('Chat-Bot Database\n')
    cloak = str(dt.datetime.now()).split(' ')
    cloak = str(cloak[1]).split(':')
    if int(cloak[0]) < 12:
        print('Good Morning, I am your virtual assistant')
    else:
        print('Good Afternoon, I am your virtual assistant')
    print('How can i helpyou today?')
    response = input()
    # udata.close()


init()
