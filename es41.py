from sys import exit
from random import randint

def death():
    quips = [ "you died , you kinda suck at this .",
              "nice job, you died ... jackass.",
              "such a luser.",
              "I have a small puppy that's better at this ."]

    print quips[randint (0,len(quips)-1)]
    exit(1)


def central_corridor():
    print "the gothons of planet percal # 25 have invaded your ship and destroyed "

    print "your entire crew, you are the last surviving member and your last "
    print "mission is to get the neutron destruct bomb from the weapons armory "

    print "put it in the bridge , and blow the ship up after getting into an "
    print "escape pod "
    print "\n"
    print "you're running down the central corridor to the weapons armory when "

    print "a gothon junps out , red scaly skin , dark grimy teeth ,and evil clown costume "

    print "flowing around his hate filled body , he's blocking the door to the "
    print "armory and about to pull a wwapon to blast you "

    action = raw_input(">")

    if action == "shoot!":
        print "quick on the draw you yank out your blaster and fire it at the gothon "
        print "his clown costume is flowing and moving around his body , whick throws "

        print "off your aim . your laser hits his costume but misses him entirely . this "

        print "completely ruins his brand new costume his mother bought him , which "
        print "makes him fly into an insane rage and blast you rapeatedly in the face until "

        print "you are dead . then he eats you "
        return 'death'

    elif action == "dogge!":
            print "like a world  "
            print "as the gothon's"

            print "in the middle "
            print "bang your  "
            print "you wake up "

            print "your head "
            return 'death '

    elif action == "tell a joke ":
        print "lucky for you "
        print "you tell the one "
        print "Lbhe zbgure vf "

        print "the gothon stops "
        print "while he's laughling "

        print "putting him down "

        return 'laser_wapon_armory'

    else :
        print "dose not "
        return "central_corridor"

def laser_wapon_armory():
    print "you do a dive roll "
    print "for more gothons"

    print "you stand up "

    print "neutron bomb in "
    print "and you "

    print "wrong 10 times "
    print "get the bomb , the code is 3 digits"

    code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
    guess = raw_input("[keypad]>")
    guess = 0

    while guess != code and guess < 10:
        print "BZZEDDD"
        guesses +=1
        guess =raw_input("[keypad]>")

    if guess == code :
        print "the container click "

        print "you grab the neutron "
        print "bridge where you "

        return 'the_bridge'
    else:
        print "the lock buzzes one "
        print "melting sound as the "

        print "you decide to "
        print "ship from their ship "
        return 'death'


def the_bridge():
    print "you must "

    print "under your "
    print "take control "

    print "clown costune "

    print "wapons out "
    print "arm and don't want "

    action = raw_input(">")

    if action == "throw the bomb" :
        print "in a panic you throw "

        print "and make a leap "
        print "tothon shoots "

        print "as you die "
        print "the bomb , you die "

        print "it goes off "
        return 'death '

    elif action == "slowly place the bomb":
        print "you pint your "

        print "and the tothos "
        print "you inch "

        print "place the bomb "

        print "you then junp "
        print "and blast the "

        print "now that the "
        print "get off this tin can"
        return 'escape_pod'
    else:
        print "dose not compute "
        return "the_bridge "

def escape_pod():
    print "you rush through "
    print "the escape "
    print "hardly any "
    print "interference "
    print "now need to "
    print "but you "
    print "do you take "

    good_pod = randint(1,5)
    guess = raw_input("[pod #]>")

    if int(guess) !=good_pod:
        print "you junp into "
        print "the pod escapes"
        print "implodes as the hull "
        print "into jam jelly "
        return 'death'
    else:
        print "you junp into %s and  "  % guess
        print "the pod easilly slides out "
        print "the planet "
        print "back and see "
        print "bright star"
        print "time. you won!"
        exit(0)
rooms={
        'death' : death,
        'central_corridor':central_corridor,
        'laser_wapon_armory': laser_wapon_armory,
        'the bridge': the_bridge,
        'escape_pod':escape_pod
        }
def runner(map,start):
    next = start

    while True :
        room = map[next]
        print "\n -------"
        next = room()
runner(rooms,'central_corridor')
