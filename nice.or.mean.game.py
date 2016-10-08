# Python: version 2.7.11

# Author: Mark Kogon learning from Daniel A. Christie, the
# real author whose teaching this section of the course

# Purpose:  This is step 6 of the Python Course, I am going
# though the video Daniel is narrating teaching us to write
# a python game

def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
        check if this is a new game
        if it is, get user's name
        if it ks not a new game, thank the player for
        playing again and continue with the game
    """
    if name != "": # if we don't have the name, then get the name        
        print("\nThank you for playing again {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                print ("\nWelcome, {}!".format(name))
                print ("\nIn this game, you will be greeted by several different people.  \nYou can be nice or mean.")
                print ("At the end of the game, you fate will be influenced from your actions.")
                stop = False
    return name

def nice_mean(nice,mean,name):
    show_score(nice,mean,name)
    pick = raw_input("\nA Stranger approaches you for a conversation. \nWill you be nice or mean? n/m:").lower()
    if pick == "n":
        print ("They smile, wave, and walk away after a pleasant conversation...")
        nice = (nice + 1)
        stop = False
    if pick == "m":
        print ("\nThe Stranger glares at you, and storms off...")
        mean = (mean + 1)
        stop = False
    score(nice,mean,name) # pass the 3 vars to the score function

def show_score(nice,mean,name):
    print ("\n{}, you currently have ({}, Nice) and ({}, Mean) points".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored in nice, mean and name vars
    if nice > 5: # if condition is true, call win function, passing in the vars
        win(nice,mean,name)
    if mean > 5: # if condition is true, call lose function with the nice, mean and name vars
        lose(nice,mean,name)
    else:  # else call nice_mean passing in the vars
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win!\nEveryone lives you and you now live in a palace!".format(name))
    again(nice,mean,name) # call again function, passing in the vars

def lose(nice,mean,name):
    print("\nToo bad, game over! \n{} You live in a van by the river, wretched and alone!".format(name))
    again(nice,mean,name) # call again function, passing in the vars

def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print ("\nSee you later alligator!")
            stop = False
            exit()
        else:
            print ("\nPlease enter a 'y' for Yes or an 'n' for No... ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # not resetting the name var as the same user is playing again
    start(nice,mean,name)

# the start of the program

if __name__ == "__main__":
    start();
