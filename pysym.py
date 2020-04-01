#!/usr/bin/python3
import os
import sys

# example:
# pysym create ~/picture.jpg ~/Pictures/Family/picture.jpg
# ^ will create a symlink to ~/picture.jpg in the ~/Pictures/Family directory
# pysym will also log this symlink in the pysyms folder (~/.config/pysym/) so the symlink can be easily cloned or deleted later

user = os.environ["USER"]
pwd = os.environ["PWD"]
version = "0.0.5"

try:
    symfile = open("/home/"+user+"/.config/pysyms/pysym.version", "r") # python does not understand ~
    symfile.readlines()
    symfile.close()

except FileNotFoundError:
    print("there is no pysyms folder. creating...")
    os.system("mkdir ~/.config/pysyms && touch ~/.config/pysyms/pysym.version")
    os.system("echo "+version+" >> ~/.config/pysyms/pysym.version")

def create():
    print("creating symlink...")
    os.system("ln -s "+sys.argv[2]+" "+sys.argv[3])

if len(sys.argv) > 1: # look for arguments like create, delete, etc
    if sys.argv[1] == "version":
        os.system("head ~/.config/pysyms/pysym.version")
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
                os.system("touch ~/.config/pysyms/"+sys.argv[2]+".pysym")
                if sys.argv[3].startswith("/"): # make the link register the full path
                    write = sys.argv[3]
                else:
                    write = pwd+"/"+sys.argv[3]
                os.system("echo "+write+" >> ~/.config/pysyms/"+sys.argv[2]+".pysym")
                if sys.argv[2].startswith("/"): # make the link register the full path
                    write2 = sys.argv[2]
                else:
                    write2 = pwd+"/"+sys.argv[2]
                os.system("echo "+write2+" >> ~/.config/pysyms/"+sys.argv[2]+".pysym")

                print("created file "+sys.argv[2])
                create()
        else:
            create()
    elif sys.argv[1] == "view":
            pass

# TODO - add delete option
