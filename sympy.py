import os
import sys

# example:
# sympy create ~/picture.jpg ~/Pictures/Family/picture.jpg
# ^ will create a symlink to ~/picture.jpg in the ~/Pictures/Family directory
# sympy will also log this symlink in the sympies file (~/.config/sympy/
# 
# sympies) so the symlink can be easily cloned or deleted later

print(sys.argv)

def create():
    print("creating symlink...")
    os.system("ln -s "+sys.argv[2]+" "+sys.argv[3])

if len(sys.argv) > 1: # look for arguments like create, delete, etc
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
                print("created file "+sys.argv[2])
                create()
        else:
            create()

# TODO - log a list of symlinks to a file so they can be removed/edited