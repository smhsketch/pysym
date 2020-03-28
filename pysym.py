#!/usr/bin/python3
import os
import sys

# example:
# sympy create ~/picture.jpg ~/Pictures/Family/picture.jpg
# ^ will create a symlink to ~/picture.jpg in the ~/Pictures/Family directory
# sympy will also log this symlink in the pysyms folder (~/.config/pysym/) so the symlink can be easily cloned or deleted later

user = (os.environ["USER"])

try:
    symfile = open("/home/"+user+"/.config/sympies/pysym.version", "r") # python does not understand ~
    symfile.readlines()
    symfile.close()

except FileNotFoundError:
    print("there is no sympies folder. creating...")
    os.system("mkdir ~/.config/sympies && touch ~/.config/sympies/pysym.version")

def create():
    print("creating symlink...")
    os.system("ln -s "+sys.argv[2]+" "+sys.argv[3])

if len(sys.argv) > 1: # look for arguments like create, delete, etc
    if sys.argv[1] == "version":
        os.system("head ~/.config/sympies/pysym.version")
    if sys.argv[1] == "create":
        try: # checks to make sure the file to be symlinked exists
            check = open(sys.argv[2])
            check.close()
        except FileNotFoundError: # if the file doesn't exist, give the option to create it
            if input("No file found to be symlinked... create one now? ") == "n":
                print("no symlink made")
                exit()
            else:
                os.system("touch "+sys.argv[2])
                os.system("touch ~/.config/sympies/"+sys.argv[2]+".pysym")
                os.system("echo "+sys.argv[3]+" | head -n 1 >> ~/.config/sympies/"+sys.argv[2]+".pysym") # FIXME
                print("created file "+sys.argv[2])
                create()
        else:
            create()
    elif sys.argv[1] == "view":
            pass

# TODO - log a list of symlinks to a file so they can be removed/edited