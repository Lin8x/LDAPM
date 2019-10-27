#!/usr/bin/python3

# Please Update For Later:
# Make it so when they user enters "start" with nothing selected, it won't run and will reload the menu (with the error message right below logo())
# Make it so when the number is selected twice, its UNSELECTED.
# Make it so when the mainMenu() is called again, it RESETS everything selected
# make it so when u answer all the information, it asks if all the information is correct, then does the animation
# make it so all the * + - ! makes god damn sense:
# # "*" Means proccess / operation
# # "!" Means for an error
# # "+" Means something is being added or listed (like the listed information when it asks if all the info is correct)
# # "-" Means something really important is missing (like if a dependency isnt there)

# Commentary to eric/asian-code:
# OMG WHY DID U ADD THE OPTIONS TO THE LIST CAUSE THE LOGO AND INFO IS SUPPOSED TO BE CALLED MULTIPLE TIMES, DO NOT COMBINE THE OPTIONS LIST WITH THE THING BEING SHOWED FOR ALMOST EVERY SCREEN AHHHHHH GOD DANG IT
# ERIC WHY DID U REMOVE THE DAMN DESKTOP FILE SECTION OMFG ITS SUPPOSED TO BE THERE
# ERIC PLEASE MAKE EVERY ERROR U EVER MAKE START AT A NEW LINE OR CLEAR THE SCREEN, PREFERABLY THE LATTER.

import os
import time
import sys

user_options = []  # contains int values

r = '\033[0m'  # reset
bold = '\033[01m'
d = '\033[02m'  # disable
ul = '\033[04m'  # underline
reverse = '\033[07m'
st = '\033[09m'  # strikethrough
invis = '\033[08m'  # invisible
white = '\033[0m'
cwhite = '\33[37m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'

# variable for user input
name = "test"
directory = "test"
script = "test"
image = "test"
isTerminal = True


def isSelected(value):
    if (value in user_options):
        return green+"X"
    return r+str(value)

# displays [value], string for main menu


def resetInput():
    global name, directory, script, image, isTerminal
    name = ""
    directory = ""
    script = ""
    image = ""
    isTerminal = True


def opt(value, string):
    return r + "  [" + str(value) + r + "] " + string

# displays the logo


def logo():
    os.system("clear " * 5)
    print(r + """
     .---.
    /     \\
    \\.@-@./
    /`\_/`\\
   //  _  /\\
  | \     )|\\""" + brown + " \t _____________________________")
    print(""" ▒▒▒▒▒▒▒▒▒▒▒▒▒▒\t   _    ___   _   ___ __  __
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒\t  | |  |   \ /_\ | _ \  \/  |
  ░░░░░░░░░░░░ \t  | |__| |) / _ \|  _/ |\/| |
  ░░░░░░░░░░░░ \t  |____|___/_/ \_\_| |_|  |_|
  ░░░░░░░░░░░░ \t _____________________________

  (L)inux (D)esktop (A)pplication (P)ackage (M)anager

  """ + r + "1st Developer: " + green + "lin8x" + r + " - " + ul + lcyan + "www.github.com/lin8x " + r +
          "\n  2nd Developer: " + green + "asian-code" + r + " - " + ul + lcyan + "www.github.com/asian-code" + r + "\n")

# displays a table of all user inputs for variables


def displayInformation():
    print('''
            Input Table
    --------------------------
    |\tname\t=\t{}
    |\tfolder\t=\t{}
    |\tscript\t=\t{}
    |\ticon\t=\t{}
    |\tconsole\t=\t{}
    --------------------------
    '''.format(name, directory, script, image, str(isTerminal)))

# request for the variable input and prompts if info is correct


def requestInformation():
    global name,directory,script,image,isTerminal
    name = input(opt("+", "Enter app name : "))
    if (name == ""):
        name = "project"

    # folder location

    directory = input(
        opt("+", "Enter your project's name directory (~/mystuff): "))
    if (directory == ""):
        directory = "~/mystuff"

    # script to run/ write to bash file

    script = input(
        opt("+", "Please enter your script's directory (~/mystuff.py): "))
    if (script == ""):
        script = "~/mystuff.py"

    image = input(
        opt("+", "Please enter your image/logo's directory (home/mystuff.ico): "))
    if (image == ""):
        image = "~/mystuff.ico"

    # determine if terminal runs when launching through the desktop icon file

    isTerminal = input(
        opt("+", "Is your app run on a terminal? (y/n): "))
    isTerminal = (isTerminal.lower() == "y" or isTerminal.lower() == "yes")

    # This is used to enter the command into the bash file so it nows how to rub the program

    # runscript = input(opt(
    #     "+", "Please enter the command in the terminal to run your tool\n (python3 mystuff.py)"))

    # asks user if all the information is correct (in case they mispelled something or whatever)
    os.system("clear")
    logo()
    displayInformation()
    answer = input(opt("+", "Is all the information here correct? (y/n): "))
    if(answer.lower() == "y" or answer.lower() == "yes"):
        return True
    return False


def process():
    os.system("clear")
    logo()
    #get variable input until correct
    iscorrect = False
    while not iscorrect:
        iscorrect = requestInformation()

     # penguin animation here


    if (1 in user_options):
        try:
            logo()

            # NEED TO CHECK FOR USER INPUT TO INCREASE APPLICATION SECURITY
            # app is using terminal commands which could be injected
            # make sure name and dir input are characters only
            projectdir = name + "dir"

            # makes the directory file
            # os.system("mkdir " + directory)
            # opt(red + "+", "Made " + directory)

            os.system("mkdir -p " + directory + "/" + projectdir)
            print(opt(red + "*", "Made " + directory + "/" + name))

            # copies the script file into the directory

            os.system("cp " + script + " " + directory + "/" + projectdir)
            print(opt(red + "*", "Moved " + script +
                      " to " + directory + "/" + projectdir))

            # copies the icon file to subfolder

            os.system("cp " + image + " " + directory + "/" + projectdir)
            print(opt(red + "+", "Moved " + image +
                      " to " + directory + "/" + projectdir))

            # create bash file

            print(opt(red + "*", "Made the batch file called " + name))

            file = open(name, "a")
            file.write(runscript)
            file.close()

            # moves the bash file into the folder

            os.system("mv " + name + " " + directory)
            print(opt(red + "*", "Moved " + name + " to " + directory))

            # creates the desktop file
            # ERIC WHY WOULD U REMOVE THIS, IT WORKS PERFECTLY. IF YOU CAN MAKE IT MORE EFFICIENT, DON'T DELETE IT, COMMENT IT OUT AT LEAST!

            print(opt(red + "*", "Creating " + name + ".desktop (PRESS CNTRL + C)"))
            os.system("cat > " + name + ".desktop")
            print("\n" + opt(red + "*", "Created " + name + ".desktop"))

            # moves desktop file into the folder

            os.system("mv " + name + ".desktop " + directory)
            print(opt(red + "*", "Moved " + name + ".desktop to " + directory))

            # make it for .desktop file and then write stuff to it
            # make it write stuff to the bat file too
            # https://formulae.brew.sh/formula/lynis#default
            # https://askubuntu.com/questions/90764/how-do-i-create-a-deb-package-for-a-single-python-script

            # making stuff for loading screen plus asking if everything is ok

        except:
            os.system("clear " * 5)
            opt(red + "!", "LADPM: Something in the setup when wrong.")
            raise

    # if (2 in user_options):
    #     d


def mainMenu():
    answer = ""
    global user_options

    try:
        while (True):
            os.system("clear")
            logo()
            print("Select the options you would like to use, then type 'start' to continue:\nTip: reselecting an option will deselect\n\n")
            print(opt(isSelected(1), "Make a Desktop Application"))
            print(opt(isSelected(2), "Make a .deb file (DOESN'T WORK ON NFTS!)"))
            print(opt(isSelected(3), "Compile your name into a .tar.xz/.zip file\n"))
            print(opt(green+"start", "Start program"))
            print(opt(red+"exit", "Quit program"))
            print()

            answer = input("Enter option: ")

            if (answer.lower() == "start"):
                process()
                break
            if(answer.lower() == "exit"):
                raise KeyboardInterrupt()
            try:
                answer = int(answer)
            except:
                print(opt("!", "Not a valid commmand"))

            # remove selected
            if(answer in user_options):
                user_options.remove(answer)
            else:
                # add option
                user_options.append(answer)

    except KeyboardInterrupt:
        print(opt(green + "+", "LADPM: Exiting..."))
        sys.exit()
    except:
        print(opt(red + "!", "LADPM: Something went wrong."))
        raise
    # recursion of mainmenu in case there is an error
    resetInput()
    mainMenu()


mainMenu()
