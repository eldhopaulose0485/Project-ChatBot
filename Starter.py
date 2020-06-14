#
#   Project Chat-Bot
#

import datetime as dt


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
    print('How can i help you today?')
    # response = input()


init()
