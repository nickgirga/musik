# Musik

# This project has been migrated to [GitLab](https://gitlab.com/nickgirga/musik)

### A simple GTK music sequencer designed with touch UI in mind first.

This is meant for simply having fun and jamming out on a mobile Linux device. It was designed for use with the PinePhone on Phosh, but it should be easy to adapt for any platform. Feel free to fork :)

## Build instructions

- This uses the meson build system, so make sure you have that installed. Also make sure you have at least `GTK 3` (as well as `PyGObject`) and `mpg123` installed for runtime.
  - Probably not a bad idea to run `sudo apt-get install build-essential` or `sudo pacman -S base-devel` before hand to grab common build dependencies.
- Navigate to where you store projects using `cd` in the CLI or a GUI file browser.
  - If in a GUI file browser, right click or click the menu button and look for a "Open in terminal" option. If this doesn't exist in your GUI, just open a terminal and manually navigate to it using `cd [directory]`.
- Run `git clone https://github.com/nickgirga/musik.git` to clone the repository into an automatically created directory named "musik".
- Run `cd musik/` to enter the project's root directory.
  - Here you can start making changes and interacting with the git repository (like committing changes, etc).
- I've just added a small installer script to simplify reconfiguring and installing Musik using meson. Simply call `./install.sh` in the root directory, enter your password when it pops up, and answer Y/N to the scale-to-fit prompt (for small devices running Phosh; most will answer no).
  - If it fails to install because the polkit could not get authorization, simply run the script using `sudo ./install.sh` or run it as root by running `su` before.
- Now you should be able to launch it via a "musik" icon in you app launcher (a desktop file is left in /usr/local/share/applications) or you can use the command `musik`.  
- Have fun!

Note: Systems with multiple Python versions may run into "gi module not found" errors if the environment being used is missing python3-gi/pygobject. If you run into these errors, ensure they are installed and that the shebang of "/usr/local/bin/musik" points to the appropriate version of Python. Most users' should read `#!/usr/bin/python`. To edit the shebang, simply open "/usr/local/bin/musik" in a text editor of your choice and edit the very first line.

### There's still lots of work to do!
This is still a very barebones project. Basically nothing really does anything besides the pads at the moment. But the beauty of open source software is that anybody can contribute. If you're interested in helping make awesome, free tools that are accessible to musicians everywhere, please fork my project, check the [issues](https://github.com/nickgirga/musik/issues) page, check the [project](https://github.com/nickgirga/musik/projects/1) page, and see if there's anything you can help with. If you manage to solve the issue, make a pull request. Even doing something as simple as opening a known bug under the [issues](https://github.com/nickgirga/musik/issues) page will help us track all of the work that needs to be done. All contributions are appreciated.
