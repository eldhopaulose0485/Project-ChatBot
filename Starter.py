#
#   Project Chat-Bot
#

import datetime as dt

def init():
    #udata = open('userdata.cbdb', 'w')
    print('####################################')
    print('    Welcome To Tourism Helpline')
    print('####################################')
    #udata.write('Chat-Bot Database\n')
    cloak = str(dt.datetime.now()).split(' ')
    cloak = str(cloak[1]).split(':')
    if int(cloak[0]) < 12:
        print('Good Morning ')
    #udata.close()

init()