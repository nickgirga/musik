# Musik
### A simple GTK music sequencer designed with touch UI in mind first.

This is meant for simply having fun and jamming out on a mobile Linux device. It was designed for use with the PinePhone on Phosh, but it will work on basically anything that can use GTK.

## Build instructions

- This uses the meson build system, so make sure you have that installed. Also make sure you have at least GTK 3 installed for runtime.
  - Probably not a bad idea to run `sudo apt-get install build-essential` or `sudo pacman -S base-devel` before hand to grab common build dependencies.
- Navigate to where you store projects using `cd` in the CLI or a GUI file browser.
  - If in a GUI file browser, right click or click the menu button and look for a "Open in terminal" option. If this doesn't exist in your GUI, just open a terminal and manually navigate to it using `cd [directory]`.
- Run `git clone https://github.com/nickgirga/musik.git` to clone the repository into an automatically created directory named "musik".
- Run `cd musik/` to enter the project's root directory.
  - Here you can start making changes and interacting with the git repository (like committing changes, etc).
- To build the project for installation, lets change directory into "./_build". Simply run `cd _build/`.
- I often reconfigure meson and flip flop between x86_64 and aarch64 and push those changes inadvertently as I work, so you may have to run `meson --reconfigure` to set the right build preferences. It may fail to build otherwise.
- We're almost done! All you have to do now is simply run `meson install` and authorize the changes via polkit. So basically, just enter your password when it pops up :P
- Now you should be able to launch it via a "musik" icon in you app launcher (a desktop file is left in /usr/share/applications) or you can use the command `musik`.
- Have fun!

### Known Issues:

'HdyViewSwitcherBar' doesn't seem to be cooperating with my GTK composite template. Because of this, I have reverted back to using the standard 'GtkStackSwitcher'. It looks a lot less elegant and flows off of phone screens by default, but I plan on tackling this soon. In the meantime, using the "scale-to-fit" script on Phosh should make it usable via mobile. This can be done by launching the terminal and running "scale-to-fit musik on" as user.
