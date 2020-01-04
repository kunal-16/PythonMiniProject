# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random

max_range=100
max_guess=7
remanining_guess=max_guess

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0, max_range)

def reset():
    print "Reset and beginning new game!"
    global remanining_guess
    global max_guess
    remanining_guess=max_guess
    new_game()    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range
    max_range = int(100)
    print "Secret number range set to [0,100)"
    global max_guess
    max_guess=7
    new_game()
    print "Starting New Game!"
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range
    max_range = int(1000)
    print "Secret number range set to [0,1000)"
    global max_guess
    max_guess=10
    new_game()
    print "Starting New Game!"
    
    
def input_guess(guess):
    # main game logic goes here
    print "you entered",guess
    global remanining_guess
    remanining_guess=remanining_guess-1  
    if int(guess) > secret_number:
        print "Lower!"
    elif int(guess) < secret_number:
        print "Higher!"
    elif int(guess) == secret_number:
        print "Correct!"
        new_game()
    print "Remaining number of guesses",remanining_guess
    if remanining_guess == 0:
        print "You lost!"
        reset()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0 100)", range100, 200)
f.add_button("Range is [0 1000)", range1000, 200)
f.add_button("Reset", reset, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
