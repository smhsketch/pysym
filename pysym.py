# Copyright 2020 Patrick Warren (smhsketch)

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


#!/usr/bin/python3
import os
import sys

# example:
# pysym create ~/picture.jpg ~/Pictures/Family/picture.jpg
# ^ will create a symlink to ~/picture.jpg in the ~/Pictures/Family directory
# pysym will also log this symlink in the pysyms folder (~/.config/pysym/) so the symlink can be easily cloned or deleted later

user = os.environ["USER"]
pwd = os.environ["PWD"]
version = "0.0.6"

try:
    symfile = open("/home/"+user+"/.config/pysyms/pysym.version", "r") # check if the pysyms folder exists 
    symfile.readlines()
    symfile.close()

except FileNotFoundError:
    print("there is no pysyms folder. creating...")
    os.system("mkdir ~/.config/pysyms && touch ~/.config/pysyms/pysym.version")
    os.system("echo "+version+" >> ~/.config/pysyms/pysym.version")

def create():
    name = input("name this symlink - this does not affect file names: ")
    os.system("touch ~/.config/pysyms/"+name+".pysym")

    if sys.argv[3].startswith("/"): # make the link register the full path
        write = sys.argv[3]
    else:
        write = pwd+"/"+sys.argv[3]
    os.system("echo "+write+" >> ~/.config/pysyms/"+name+".pysym")

    if sys.argv[2].startswith("/"): # make the link register the full path
        write2 = sys.argv[2]
    else:
        write2 = pwd+"/"+sys.argv[2]
    
    os.system("echo "+write2+" >> ~/.config/pysyms/"+name+".pysym") # make the log file
    os.system("ln -s "+sys.argv[2]+" "+sys.argv[3])
    print("Successfully created symlink")

if len(sys.argv) > 1: # look for arguments like create, delete, etc
    if sys.argv[1] == "version":
        os.system("head ~/.config/pysyms/pysym.version")
    if sys.argv[1] == "create":
        try: # checks to make sure the file to be symlinked exists
            check = open(sys.argv[2])
            check.close()
        except FileNotFoundError: # if the file doesn't exist, give the option to create it
            if input("No base file found to be symlinked... create one now? ") == "n":
                print("no files created; no symlinks made")
                exit()
            else:
                os.system("touch "+sys.argv[2])
                print("created file "+sys.argv[2])
        create()

    elif sys.argv[1] == "view":
        if sys.argv[2] == "":
            print("please give a symlink to view")
            exit()
        try:
            symfile = open("/home/"+user+"/.config/pysyms/"+sys.argv[2]+".pysym")
            info = symfile.readlines()
            symfile.close()
            print()
            print((info[0])[:-1]+" --> "+(info[1]))
        except FileNotFoundError:
            print("not found. maybe check the spelling?")
            exit()

    elif sys.argv[1] == "delete" or sys.argv[1] == "remove":
        if sys.argv[2] == "":
            print("please specify a symlink to remove")
            exit()
        try:
            symfile = open("/home/"+user+"/.config/pysyms/"+sys.argv[2]+".pysym")
            info = symfile.readlines()
            symfile.close()
        except FileNotFoundError:
            print("not found. maybe check the spelling?")
            exit()
        
        delete = input("would you like to remove the base, link, or both?")
        if delete == "base" or delete == "both":
            os.remove((info[1])[:-1])
        if delete == "link" or delete == "both":
            os.remove((info[0])[:-1])
        os.remove("/home/"+user+"/.config/pysyms/"+sys.argv[2]+".pysym")
        print()
        print("successfully deleted symlink")
        print()