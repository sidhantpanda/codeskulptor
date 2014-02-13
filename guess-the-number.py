# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
# initialize global variables used in your code
count = 0
ranno = 0
plays = 0
maxtries = 7
points = 0
ranno = random.randrange(0,100)

# define event handlers for control panel
    
def range100():
    global plays
    global points
    global maxtries
    maxtries=7
    
    if plays>=3:
        print "3 games are over"
        print "Total points :" , points
        return
    global count
    count=0
    global ranno
    ranno = random.randrange(0,100)
    print "Game restarted with range 0-100"
    # button that changes range to range [0,100) and restarts
    return
def range1000():
    global plays
    global points
    global maxtries
    maxtries=10
    
    if plays>=3:
        print "3 games are over"
        print "Total points :" , points
        return
    global count
    count=0
    global ranno
    ranno = random.randrange(0,100)
    print "Game restarted with range 0-1000"
    # button that changes range to range [0,1000) and restarts
    return
def get_input(guess):
    global count
    global points
    global maxtries
    global plays
    count = count +1
    if plays>=3:
        print "3 games are over"
        print "Total points :" , points
        return
    if count>maxtries:
        print "Maximum tries used"
        plays = plays + 1
        if maxtries==7:
            range100()
        else:
            range1000()
        return
    global ranno
    player=int(guess)
    #print player
    if player<ranno:
        print "Higher. Number of guesses remaining:",maxtries-count
    elif player>ranno:
        print "Lower. Number of guesses remaining:",maxtries-count
    else:
        print "Congratulations!"
        plays = plays + 1
        points = points + 1
        print "Total points :" , points
        if maxtries==7:
            range100()
        else:
            range1000()
    return
    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)
brange100 = frame.add_button("Range 0-100", range100)
brange1000 = frame.add_button("Range 0-1000", range1000)
inp = frame.add_input("Enter your guess:", get_input, 50)

# register event handlers for control elements


# start frame
frame.start()

# always remember to check your completed program against the grading rubric
