#!/usr/bin/python3

import os
import time
import sys

user_options = []

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

# updates main menu options based on input
def isSelected(value):
    if (value in user_options):
        return "X"
    return value

# displays [value], string for main menu
def opt(value, string):
    return r + "  [" + green + str(value) + r + "] " + string

# displays the logo 
def welcome():
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
          "\n  2nd Developer: " + green + "asian-code" + r + " - " + ul + lcyan + "www.github.com/asian-code" + r +
          "\n  Select the options you would like to use, then type 'start' to continue:\n\n"+opt(isSelected(1), "Make a Desktop Application\n") +
          opt(isSelected(2), "Make a .deb file (DOESN'T WORK ON NFTS!)\n") +
          opt(isSelected(3), "Compile your name into a .tar.xz/.zip file\n"))


def run():
    #bash file name
    name = input(opt("*","Enter app name : "))
    if(name == ""):
        name = "projects"
    # folder location
    directory = input(opt("*","enter your projects name directory (~/mystuff): "))
    if(directory == ""):
        directory = "~/mystuff"
    # script to run/ write to bash file
    script = input(opt("*","Please enter your script's directory (~/mystuff.py): "))
    if(script == ""):
        script = "~/mystuff.py"
    # need to talk to DANISGAY about what its purpose
    runscript = input(opt("*","Please enter the command in the terminal to run your tool\n (python3 mystuff.py)"))

    if(1 in user_options):
        # get location of icon image 
        image = input(opt("*","Please enter your image/logo's directory (home/mystuff.ico): "))
        if(image == ""):
            image = "~/mystuff.ico"
        # determine if terminal runs when launching through desktop icon
        terminal = input(opt("*", "Is your software run on a terminal? (y/n): "))
        terminal = (terminal.lower() == "y" or terminal.lower() == "yes")
        try:
            # NEED TO CHECK FOR USER INPUT TO INCREASE APPLICATION SECURITY
            # app is using terminal commands which could be injected
            #make sure name and dir input are characters only
            projectdir = name+"dir"

            # makes the directory file
            #os.system("mkdir " + directory)
            #opt(red + "+", "Made " + directory)

            # makes the parentfolder with subfolder 
            os.system("mkdir -p " + directory + "/" + projectdir)
            print(opt(red + "+", "Made " + directory + "/" + name))

            # copies the script file into the directory 
            os.system("cp " + script + " " + directory + "/" + projectdir)
            opt(red + "+", "Moved " + script +
                " to " + directory + "/" + projectdir)

            os.system("cp " + image + " " + directory + "/" + projectdir)
            opt(red + "+", "Moved " + image +
                " to " + directory + "/" + projectdir)

            os.system("touch " + name)
            opt(red + "+", "Made the batch file called " + name)

            file = open(name, "a")
            file.write(runscript)
            file.close()

            os.system("mv " + name + " " + directory)
            opt(red + "+", "Moved " + name + " to " + directory)

            opt(red + "+", "Creating " + name + ".desktop (PRESS CNTRL + C)")
            os.system("cat > " + name + ".desktop")
            print()
            opt(red + "+", "Created " + name + ".desktop")

            os.system("mv " + name + ".desktop " + directory)
            opt(red + "+", "Moved " + name + ".desktop to " + directory)

            # make it for .desktop file and then write stuff to it
            # make it write stuff to the bat file too
            # https://formulae.brew.sh/formula/lynis#default
            # https://askubuntu.com/questions/90764/how-do-i-create-a-deb-package-for-a-single-python-script

        except:
            opt(red + "x", "Something in the setup when wrong.")
            raise

    if(2 in user_options):
        name = input(r + "  [" + green + "*" + r +
                     "] Please enter your name (null): ")
        email = input(r + "  [" + green + "*" + r +
                      "] Please enter your email (N/A): ")
        opt("*", "Please enter your projects description: ")
        print("  (This is my custom linux application)")
        description = input("  ")


def mainMenu():
    answer = ""
    global user_options
    try:
        while(True):
            os.system("clear")
            welcome()
            answer = input("\tPlease enter an input: ")

            if(answer.lower() == "start"):
                run()
                break
            try:
                user_options.append(int(answer))
            except:
                print(opt(red+"!","ARE YOU RETARDED? Not a number!  ("+answer+")"))
                raise KeyboardInterrupt()

    except KeyboardInterrupt:
        print(opt(red + "!", "Exiting..."))
        sys.exit()
    except:
        print(opt(red + "!", "Something went wrong:"))
        raise


mainMenu()
