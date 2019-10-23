#!/usr/bin/python3

import os
import time

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


def isSelected(value):
    if (value in user_options):
        return "X"
    return value


def opt(value, string):
    return r + "  [" + green + str(value) + r + "] " + string


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
          "\n  Select the options you would like to use, then type 'start' to continue:\n\n"+opt(isSelected("1"), "Make a Desktop Application\n") +
          opt(isSelected("2"), "Make a .deb file (DOESN'T WORK ON NFTS!)\n") +
          opt(isSelected("3"), "Compile your project into a .tar.xz/.zip file\n"))


def run():
    sysstuff = "Getting everything setup for you"
    for i in range(0, 4):
        welcome()
        print()
        opt(red + "+", sysstuff)
        sysstuff = sysstuff + "."
        time.sleep(1)
    welcome()
    print("\n" + r + "  ---  ---\n")

    project = input(r + "  [" + green + "*" + r +
                    "] Please enter your project name (project): ")
    if(project == ""):
        project = "project"

    directory = input(r + "  [" + green + "*" + r +
                      "] Please enter your project name directory (~/mystuff): ")
    if(directory == ""):
        directory = "~/mystuff"

    script = input(r + "  [" + green + "*" + r + "] Please enter your script's directory (~/mystuff.py) \n   (FOR NON-INTERPRETER LANGUAGES, PUT THE DIRECTORY OF THE COMPILED EXECUTABLE!)\n  [" + green + "|" + r + "] Enter here: ")
    if(script == ""):
        script = "~/mystuff.py"

    runscript = input(r + "  [" + green + "*" + r +
                      "] Please enter the command in the terminal to run your tool\n (python3 mystuff.py) (DO NOT PUT SUDO)\n  [" + green + "|" + r + "] Enter here: ")

    if(one == "*"):
        image = input(r + "  [" + green + "*" + r +
                      "] Please enter your image/logo's directory (~/mystuff.ico): ")
        if(image == ""):
            image = "~/mystuff.ico"

        terminal = input(
            r + "  [" + green + "*" + r + "] Is your software run on a terminal? (y/n): ")
        if(terminal.lower() == "y" or terminal.lower() == "yes"):
            terminal = "true"

        welcome()
        sysstuff = "Packaging everything for you"
        for i in range(0, 4):
            welcome()
            print()
            opt(red + "+", sysstuff)
            sysstuff = sysstuff + "."
            time.sleep(1)
        try:

            projectdir = project+"dir"

            # makes the directory file
            os.system("mkdir " + directory)
            opt(red + "+", "Made " + directory)

            # makes the projectdir file
            os.system("mkdir " + directory + "/" + projectdir)
            opt(red + "+", "Made " + directory + "/" + project)

            # moves the projectdir file into the directory file
            os.system("cp " + script + " " + directory + "/" + projectdir)
            opt(red + "+", "Moved " + script +
                " to " + directory + "/" + projectdir)

            os.system("cp " + image + " " + directory + "/" + projectdir)
            opt(red + "+", "Moved " + image +
                " to " + directory + "/" + projectdir)

            os.system("touch " + project)
            opt(red + "+", "Made the batch file called " + project)

            file = open(project, "a")
            file.write(runscript)
            file.close()

            os.system("mv " + project + " " + directory)
            opt(red + "+", "Moved " + project + " to " + directory)

            opt(red + "+", "Creating " + project + ".desktop (PRESS CNTRL + C)")
            os.system("cat > " + project + ".desktop")
            print()
            opt(red + "+", "Created " + project + ".desktop")

            os.system("mv " + project + ".desktop " + directory)
            opt(red + "+", "Moved " + project + ".desktop to " + directory)

            # make it for .desktop file and then write stuff to it
            # make it write stuff to the bat file too
            # https://formulae.brew.sh/formula/lynis#default
            # https://askubuntu.com/questions/90764/how-do-i-create-a-deb-package-for-a-single-python-script

        except:
            opt(red + "x", "Something in the setup when wrong.")
            raise

    if(two == "*"):
        name = input(r + "  [" + green + "*" + r +
                     "] Please enter your name (null): ")
        email = input(r + "  [" + green + "*" + r +
                      "] Please enter your email (N/A): ")
        opt("*", "Please enter your project description: ")
        print("  (This is my custom linux application)")
        description = input("  ")


def mainMenu():
    answer = ""
    global user_options
    try:
        while(True):
            welcome()
            answer = input("  Please enter an input: ")
            
            if(answer.lower() == "start"):
                run()
                break
            try:
                user_options.append(int(answer))
                print(user_options)
                time.sleep(1)
            except:
                print("ARE YOU RETARDED? tf is this? "+answer)
                break
               

            
    except KeyboardInterrupt:
        print("\n")
        opt(red + "+", "Exiting...")
        exit()
    except:
        print()
        opt(red + "x", "Something went wrong. Sorry.")
        raise
     


mainMenu()
