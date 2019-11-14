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
    return brown+str(value)

# displays [value], string for main menu


def resetInput():
    global name, directory, script, image, isTerminal
    name = ""
    directory = ""
    script = ""
    image = ""
    isTerminal = True


def opt(value, string):
    return r + "  [" + brown + str(value) + r + "] " + string

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
    print('''            Input Table
    --------------------------
    |\tname\t=\t{}
    |\tfolder\t=\t{}
    |\tscript\t=\t{}
    |\ticon\t=\t{}
    |\tconsole\t=\t{}
    --------------------------
    '''.format(name, directory, script, icon, str(isTerminal)))

# request for the variable input and prompts if info is correct

def requestInformation():
    # makes these things global

    global name,directory,script,icon,isTerminal

    # asks for name of app

    name = input(opt("+", "Enter app name : "))
    if (name == ""):
        name = "appname"

    # folder location for every project item

    print(opt("!", "(THIS FOLDER SHOULD CONTAIN ALL YOUR PROJECT FILES INSIDE IT!)"))
    directory = input(opt("+", "Enter your project's directory (~/myproject): "))
    if (directory == ""):
        directory = "~/myproject"

    # script to run/ write to bash file

    script = input(
        opt("+", "Please enter your main script name.file (mystuff.py): "))
    if (script == ""):
        script = "mystuff.py"

    if (1 in user_options):

      # icon image inside the folder so we can link it to .desktop file

      print(opt("!", "(THIS ICON IMAGE SHOULD ALREADY BE IN YOUR PROJECT FOLDER)"))
      icon = input(opt("+", "Enter your project's directory (mystuff.ico): "))
      if (icon == ""):
          icon = "mystuff.ico"

      # determine if terminal runs when launching through the desktop icon file

      isTerminal = input(
          opt("+", "Is your app run on a terminal? (y/n): "))
      isTerminal = (isTerminal.lower() == "y" or isTerminal.lower() == "yes")

      # This is used to enter the command into the bash file so it nows how to rub the program

      runscript = input(opt("+", "Please enter the command in the terminal to run your tool ('python3 ')\n  "))
      if(runscript == ""):
        runscript = "./"

      # asks user if all the information is correct (in case they mispelled something or whatever)
      os.system("clear")
      logo()
      displayInformation()
      answer = input(opt("+", "Is all the information here correct? (y/n): "))
      if(answer.lower() == "y" or answer.lower() == "yes"):
          return True
      return False
    
    elif (2 in user_options):
      exit()

    elif (3 in user_options):
      exit()

    else:
      os.system("clear * 5")
      input(opt(red + "!", "LADPM: Error. You didn't select any option.   " + invis))
      print(r)
      raise KeyboardInterrupt()


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
            #directory is the name of the folder

            # makes the directory file
            # os.system("mkdir " + directory)
            # opt(red + "+", "Made " + directory)

            print(opt("*", "Making " + name + " files...\n"))

            os.system("mkdir -p " + projectdir)
            print(opt(red + "*", "Made " + projectdir))

            os.system("cp -r " + directory + " " + projectdir)
            print(opt(red + "*", "Copied " + directory +
                      " to " + projectdir))

            # create bash file

            print(opt(red + "*", "Made the batch file called " + name))

            file = open(name, "a")
            file.write("Hello")
            file.close()

            # moves the bash file into the folder

            os.system("mv " + name + " " + projectdir)
            print(opt(red + "*", "Moved " + name + " to " + projectdir))

            # create setup file

            print(opt(red + "*", "Made the setup file called setup" + name + ".sh"))

            file = open("setup" + name + ".sh", "a")
            file.write("Hello")
            file.close()

            # moves the bash file into the folder

            os.system("mv setup" + name + ".sh " + projectdir)
            print(opt(red + "*", "Moved setup" + name + ".sh to " + projectdir))

            # creates the desktop file

            #print(opt(red + "*", "Creating " + name + ".desktop (PRESS CNTRL + C)"))
            #os.system("cat > " + name + ".desktop")
            os.system("touch " + name + ".desktop")
            print(opt(red + "*", "Created " + name + ".desktop"))

            # moves desktop file into the folder

            os.system("mv " + name + ".desktop " + projectdir)
            print(opt(red + "*", "Moved " + name + ".desktop to " + projectdir))

            # make it for .desktop file and then write stuff to it
            # make it write stuff to the bat file too
            # https://formulae.brew.sh/formula/lynis#default
            # https://askubuntu.com/questions/90764/how-do-i-create-a-deb-package-for-a-single-python-script

            # making stuff for loading screen plus asking if everything is ok

            input("\n" + opt("*", "All processes finished. Please press enter to continue...") + invis)
            print(r + "")

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
            print(r + "  " + ul + "Select the an option, then type 'start' to continue:" + r + "\n  Tip: reselecting an option will deselect\n")
            print(opt(isSelected(1), "Make a Desktop Application"))
            print(opt(isSelected(2), "Make a .deb file (DOESN'T WORK ON NFTS!)"))
            print(opt(isSelected(3), "Compile your name into a .tar.xz/.zip file\n"))
            print(opt(green+"start", "Start program"))
            print(opt(red+"exit", "Quit program"))
            print()

            answer = input("  Enter option: ")

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
        os.system("clear * 5")
        print(opt(green + "+", "LADPM: Exiting..."))
        sys.exit()
    except:
        print(opt(red + "!", "LADPM: Something went wrong."))
        raise
    # recursion of mainmenu in case there is an error
    resetInput()
    mainMenu()

mainMenu()
