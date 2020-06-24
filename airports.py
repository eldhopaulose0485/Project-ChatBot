state = open('Databases/state_code.txt')
statel = state.readlines()
city = open('Databases/city_codes.txt')
cityl = city.readlines()
port = open('Databases/port_codes.txt')
portl = port.readlines()

portlist = []
i = 0

for s in statel:
    s = s.rstrip()
    portl[i] = portl[i].rstrip()
    cityl[i] = cityl[i].rstrip()
    portlist.append(tuple((s, cityl[i], portl[i])))
    i = i + 1


def printstate(state):
    print('\n--------------------------------')
    for p in portlist:
        if p[0].lower() == state.lower():
            print(p[1])
    print('--------------------------------\n')


def airpcheck(name):
    for p in portlist:
        if p[1].lower() == name.lower():
            return True
    else:
        return False


def statecheck(state):
    for p in portlist:
        if p[0].lower() == state.lower():
            return True
    else:
        return False


def placetocode(place):
    for p in portlist:
        if p[1].lower() == place.lower():
            return p[2]
