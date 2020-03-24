#!/usr/bin/python3

# MADE MY DANIEL / LIN8X AND REQUIRES CREDIT IN ORDER TO USE!
# Please, I spent alot of time into this :)

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

# global variables for user input
name = "test"
directory = "test"
script = "test"
image = "test"
isTerminal = True
runscript = "test"


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
    version = ""
    maintainer = ""
    description = ""
    arch = ""
    depends = ""
    runscript = ""
    isTerminal = True


def opt(value, string):
    return r + "  [" + brown + str(value) + r + "] " + string

# displays the logo


def logo():
    os.system("clear")
    print(r + """
     .---.
    /     \\
    \\.@-@./
    /`\_/`\\
   //  _  /\\ """ + brown + "\t BETA: Version 0.1" + white + """
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

def displayInformationOne():
    print('''            Input Table
    --------------------------
    |\tname\t=\t{}
    |\tfolder\t=\t{}
    |\tscript\t=\t{}
    |\ticon\t=\t{}
    |\tconsole\t=\t{}
    |\tcommand\t=\t{}
    --------------------------
    '''.format(name, directory, script, icon, str(isTerminal),runscript))

def displayInformationTwo():
  print("Please read the debian packages guidelines to ensure your program follows the social contract: " + lcyan + ul + "https://www.debian.org/social_contract#guidelines" + r + "\n")
  print('''            Input Table
    --------------------------------
    |\tname        \t=\t{}
    |\tfolder      \t=\t{}
    |\tscript      \t=\t{}
    |\tversion     \t=\t{}
    |\tmaintainer  \t=\t{}
    |\thomepage    \t=\t{}
    |\tdescription \t=\t{}
    |\tarchitecture\t=\t{}
    |\tdepends\t\t\t=\t{}
    --------------------------------
    '''.format(name, directory, script, version, maintainer, homepage, description, arch, depends))
    #format(name, directory, script, version, maintainer, homepage, description, arch, depends))

# request for the variable input and prompts if info is correct

def requestInformation():
    # makes these things global

    #For all options: name, directory, script
    #For option 1: icon, isTerminal
    #For option 2: version, arch, maintainer, depends, homepage, description
    global name,directory,script,icon,isTerminal,runscript,version,arch,maintainer,depends,homepage,description

    if not user_options:
      KeyboardInterrupt()

    if(1 not in user_options and 2 not in user_options and 3 in user_options):
      return True

    # asks for name of app

    name = input(opt("+", "Enter app name : "))
    if (name == ""):
        name = "appname"

    # folder location for every project item

    print(opt("!", "(THIS FOLDER SHOULD CONTAIN ALL YOUR PROJECT FILES INSIDE IT!)"))
    directory = input(opt("+", "Enter your project's directory (/myproject): "))
    if (directory == ""):
        directory = "myproject"
    # script to run/ writrune to bash file
    script = input(opt("+", "Please enter your main script file (mystuff.py): "))
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
          opt("+", "Does your app run on a terminal? (y/n): "))
      isTerminal = (isTerminal.lower() == "y" or isTerminal.lower() == "yes")

      # This is used to enter the command into the bash file so it nows how to rub the program

      runscript = input(opt("+", "Please enter the command in the terminal to run your tool ('python3', 'java', 'perl', etc)\n  "))
      if(runscript == ""):
        runscript = "python3"
      #if(""):
        #runscript.remove("/", "")

      # asks user if all the information is correct (in case they mispelled something or whatever)

      os.system("clear")
      logo()
      displayInformationOne()
      answer = input(opt("+", "Is all the information here correct? (y/n): "))
      if(answer.lower() == "y" or answer.lower() == "yes"):
          return True
      return False
    
    elif (2 in user_options):
      #For option 2: version, arch, maintainer, depends, homepage, description

      #Asks for version name

      version = input(opt("+", "Please enter the version of your launcher (1.0): "))
      if(version == ""):
        version = "1.0"

      #Asks for maintainer information

      maintainer = input(opt("+", "Please enter your maintainer information (Jane Doe <Email@notgiven.com>): "))
      if(maintainer == ""):
        maintainer = "Jane Doe <Email@notgiven.com>"

      #asks for homepage

      homepage = input(opt("+", "Please enter your homepage/github link (http://www.github.com/): "))
      if(homepage == ""):
        homepage = "www.github.com"

      #asks for description

      description = input(opt("+", "Please enter a description of your tool in one sentence (Just a simple program!): " + "\n  "))
      if(description == ""):
        description = "Just a simple program!"

      #Asks for architecture type
      
      print(opt(red + "*", "LEAVE EMPTY IF YOU DON'T KNOW WHAT YOU'RE DOING!"))
      arch = input(opt("+", "Please enter your architecture type (all): "))
      if(arch == ""):
        arch = "all"

      #asks for dependencies

      depends = input(opt("+", "Please enter your tool/program's dependencies (${misc:Depends}, ${python3:Depends}): "))
      if(depends == ""):
        depends = "${misc:Depends}, ${python3:Depends}"
      
      logo()
      displayInformationTwo()
      answer = input(opt("+", "Is all the information here correct? (y/n): "))
      if(answer.lower() == "y" or answer.lower() == "yes"):
          return True
      return False

    elif (3 in user_options):
      return True

    else:
      os.system("clear")
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
            if("/" in directory):
              directory.replace("/", "")
            if("~" in directory):
              directory.replace("~")
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
            file.write("sudo " + runscript + " /opt/" + directory + "/" + script)
            file.close()

            # moves the bash file into the folder

            os.system("mv " + name + " " + projectdir)
            print(opt(red + "*", "Moved " + name + " to " + projectdir))

            # create setup file

            print(opt(red + "*", "Made the setup file called setup" + name + ".sh"))

            file = open("setup" + name + ".sh", "a")
            # moves the .desktop file to act like a real application
            file.write("sudo mv " + name + ".desktop" + " /usr/share/applications")

            # moves all necessary files to /opt/

            file.write(" && sudo mv " + directory + " /opt/")
            # allows you to run the application by name in the terminal
            file.write(" && sudo mv " + name + " /usr/bin")
            file.close()

            # moves the bash file into the folder

            os.system("mv setup" + name + ".sh " + projectdir)
            print(opt(red + "*", "Moved setup" + name + ".sh to " + projectdir))

            # creates the desktop file

            #print(opt(red + "*", "Creating " + name + ".desktop (PRESS CNTRL + C)"))
            #os.system("cat > " + name + ".desktop")

            os.system("touch " + name + ".desktop")
            print(opt(red + "*", "Created " + name + ".desktop"))
            file = open(name + ".desktop", "a")
            # the reason i did this is so its easier to read in code
            file.write("[Desktop Entry]")
            file.write("\nEncoding=UTF-8")
            file.write("\nVersion=1.0")
            file.write("\nType=Application")
            file.write("\nTerminal=" + str(isTerminal).lower())
            file.write("\nExec=" + name)
            file.write("\nName=" + name)
            file.write("\nIcon=/opt/" + directory + "/" + icon)
            file.close()

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
            os.system("clear")
            opt(red + "!", "LADPM: Something in the setup when wrong.")
            raise

    if (2 in user_options):
        if (1 in user_options):
          user_options.remove(1)
          process()
        logo()

        projectdeb = name + "debfile"

        os.system("mkdir -p " + projectdeb + "/DEBIAN")
        print(opt(red + "*", "Made " + projectdeb + "/DEBIAN"))

        os.system("mkdir -p " + projectdeb + "/usr/bin")
        print(opt(red + "*", "Made " + projectdeb + "/usr/bin"))

        os.system("touch control")
        print(opt(red + "*", "Made control file"))

        #name, directory, script, version, maintainer, homepage, description, arch, depends
        #writes all configurations to the control file
        #print("Package: linuxconfig\nVersion: 1.0\nSection: custom\nPriority: optional\nArchitecture: all\nEssential: no\nInstalled-Size: 1024\nMaintainer: linuxconfig.org\nDescription: Print linuxconfig.org on the screen")

        #input("\n" + opt(red + "*", "Copy and paste the following into the control file. Please press enter to continue once done...") + invis)
        
        print(r + "")

        os.system("mv control " + projectdeb + "/DEBIAN/")
        print(opt(red + "*", "Made " + projectdeb + "/DEBIAN/control"))

        #Writing to file
        cf = open(projectdeb + "/DEBIAN/control", "a")
        
        cf.write("Package: " + name + "\nVersion: " + version + "\nMaintainer: " + maintainer + "\nDescription: " + description + "\nArchitecture: " + arch + "\nDepends: " + depends)
        cf.close()
        print(opt(red + "*", "Sucessfully entered information in " + projectdeb + "/DEBIAN/control"))

        os.system("cp " + directory + "/" + script + " " + projectdeb + "/usr/bin")
        print(opt(red + "*", "Copied " + directory + "/" + script + " to " + projectdeb + "/usr/bin"))

        try:
          #os.system("dpkg-deb --build " + projectdeb)
          #os.system("dpkg-deb --build " + projectdeb + " " + name+"_"+version+"_"+arch+".deb")
          #sudo dpkg -b appnamedebfile appnamedebfile.deb
          print(opt(red+ "DEV MESSAGE","As of right now, there is no automatic solution that I could find that automatically makes the .deb file."))
          print(opt(red + "STEP 1", "Please re-copy and paste the information in " + projectdeb + "/DEBIAN/control"))
          print(opt(red + "STEP 2", "Then do 'dpkg -b " + projectdeb))
        except:
          print(opt(red + "!", "LDAPM: Error! Could not use dpkg! Is it installed?"))

        input("\n" + opt(red + "*", "All processes finished. Please press enter to continue...") + invis)
        print(r + "")

    if (3 in user_options):
        logo()
        filename = input(opt(red + "+", "Please enter the directory where your entire project is stored: "))
        choose = input(opt(red + "+", "Please pick either zip or tar format (z/t): "))
        if(choose.lower() == "z"):
          os.system("zip -r " + filename + ".zip " + filename)
          print(opt(red + "*", "Made " + filename + ".zip"))
        else:
          os.system("tar cf - " + filename + " | xz -z - > " + filename + ".tar.xz")
          print(opt(red + "*", "Made " + filename + ".tar.xz"))
        # tar cf - directory/ | xz -z - > directory.tar.xz

        user_options.remove(3)
        input("\n" + opt(red + "*", "All processes finished. Please press enter to continue...") + invis)
        print(r + "")


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
            print(opt(isSelected(3), "Compile your name into a .tar.xz/.zip file (REQUIRES ZIP AND/OR TAR!)\n"))
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
                # add optionhttps://ttsreader.com/
                user_options.append(answer)

    except KeyboardInterrupt:
        os.system("clear")
        print(opt(green + "+", "LADPM: Exiting..."))
        sys.exit()
    except:
        print(opt(red + "!", "LADPM: Something went wrong."))
        raise
    # recursion of mainmenu in case there is an error
    resetInput()
    mainMenu()

mainMenu()
