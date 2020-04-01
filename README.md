# pysym
Symlink manager written in python 3.8.2

# installation
pysym is still in a very experimental phase and is not fully functional yet.

However, you are free to git clone the repo and use pysym in this early phase.

# how it works
pysym deals with two files, the `base` file, and the `link`. The `link` file is the actual symbolic link that points to the `base` file.

# what we have now
pysym can create a symbolic link that points to a file, and keep a log of it in `~/.config/pysyms/`.

# future releases
pysym will soon be able to actually manage your symlinks, keeping track of when it was made, managing flags for the symlinks, removing the symlinks, and more. 
