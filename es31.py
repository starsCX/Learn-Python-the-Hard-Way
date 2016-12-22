print " you enter a dark room with two doors . do you go through door #1 or door #2?"


door = raw_input(">")

if door == "1":
    print "there's a giant bear here eating a cheese cake . what do you do ?"
    print "1. take the cake ."
    print "2. scream at the bear "

    bear=raw_input(">")

    if bear=="1":
        print "the bear eats your face off. good job"
    elif bear == "2":
        print "the bear eats your legs off , good job "
    else:
        print "well dong %s is probably better. bear runs away " % bear

elif door == "2":
    print "into the "
    print "1. "
    print "2."
    print "3."
    insanity = raw_input(">")

    if insanity == "1" or insanity == "2" :
        print "your body "
    else:
        print "the insanity "
else:
    print "you stumble  "
