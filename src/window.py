# window.py
#
# Copyright 2020 nickgirga
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
from gi.repository import Gtk
from threading import Thread

@Gtk.Template(resource_path='/com/github/nickgirga/musik/window.ui')
class MusikWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MusikWindow'

    LIBRARY_PATH = os.path.expanduser('~/Documents/musik')

    # a nested list to represent the different pads and the locations of their audio clips
    pads = [["A1", LIBRARY_PATH + "/Samples/Percussion/Kicks/kick0.mp3"], ["B1", LIBRARY_PATH + "/Samples/Percussion/Snares/snare0.mp3"], ["C1", LIBRARY_PATH + "/Samples/Percussion/Hats/Closed/closed-hat0.mp3"], ["D1", LIBRARY_PATH + "/Samples/Percussion/Hats/Half/half-closed-hat0.mp3"], ["E1", LIBRARY_PATH + "/Samples/Percussion/Hats/Open/open-hat0.mp3"],
           ["A2", LIBRARY_PATH + "/Samples"], ["B2", LIBRARY_PATH + "/Samples"], ["C2", LIBRARY_PATH + "/Samples"], ["D2", LIBRARY_PATH + "/Samples"], ["E2", LIBRARY_PATH + "/Samples"],
           ["A3", LIBRARY_PATH + "/Samples/Ukulele/uke0.mp3"], ["B3", LIBRARY_PATH + "/Samples/Ukulele/uke1.mp3"], ["C3", LIBRARY_PATH + "/Samples/Ukulele/uke2.mp3"], ["D3", LIBRARY_PATH + "/Samples/Ukulele/uke3.mp3"], ["E3", LIBRARY_PATH + "/Samples"]]
    
    # stores the index of the pad button that was last pressed; used for displaying pad settings
    last_pressed_pad = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_musik_library()

    # called upon initialization to fetch existing default assets. if none exist, download from git repository
    def initialize_musik_library(self):
        # verify the library's root folder exists
        if (not os.path.exists(self.LIBRARY_PATH)):
            response = self.create_simple_message_dialog("No musik library was found in \"~/Documents\". Would you like to create a new library directory at \"~/Documents/musik\"?", True)
            if (response == Gtk.ResponseType.YES):
                print("Started creating library at \"~/Documents/musik\"...")
                
                # clone assets into temporary directory
                print("Cloning assets from https://github.com/nickgirga/musik-asset-library.git")
                os.system("git clone https://github.com/nickgirga/musik-asset-library.git " + self.LIBRARY_PATH)
                print("Done cloning assets!")
                
                # finish
                print("Done creating Musik library!")
                print(self.pads[0][1])
            else:
                # skip library creation and exit
                print("skipping library creation... (user request)")

        # initialize audio clips
        return

    # a general function used to play mp3 clips natively using mpg123
    def play_mp3_native(self, clip_path):
        thread = Thread(target = self.audio_thread, args = (clip_path, ))
        thread.start()

    # a gernal function used to create new threads that play audio using mpg123
    def audio_thread(self, args):
        os.system("mpg123 \"" + args + "\"")

    # creates a simple message dialog with the OK button and INFO message type
    def create_simple_message_dialog(self, text, yesno):
        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.YES_NO if yesno else Gtk.ButtonsType.OK, text)
        response = message.run()
        message.destroy()
        return response

    # a general function used to open popup menus
    @Gtk.Template.Callback()
    def popup_button_clicked(self, popup):
        popup.show_all()
        popup.popup()

    # a general function used to open windows
    @Gtk.Template.Callback()
    def window_button_clicked(self, widget):
        widget.run()
        widget.destroy()

    # a general function used as a placeholder to verify signals are working on UI elements
    @Gtk.Template.Callback()
    def feature_not_implemented(self, widget):
        self.create_simple_message_dialog("Sorry! This feature hasn't been implemented yet!", False)

    # this function is called any time a pad is pressed. `num` is the index of the stack that the pad's settings reside on
    def press_pad(self, widget, num):
        # update last_pressed_pad
        self.last_pressed_pad = num

        # get children
        label = widget.get_children()[0]
        my_file_chooser_button = widget.get_children()[1]
        padloc = self.pads[self.last_pressed_pad][0]
        filename = self.pads[self.last_pressed_pad][1]

        # update label to match
        label.set_text("Pad " + padloc + " Settings")
        my_file_chooser_button.set_filename(filename)

        #  verify file exists at specified path and play it using mpg123
        if (type(filename) == type(None) or filename == ""): return
        self.play_mp3_native(filename)

    @Gtk.Template.Callback()
    def set_pad_clip(self, widget):
        filename = widget.get_filename()
        if (type(filename) == type(None) or filename == ""):
            self.create_simple_message_dialog("Error setting audio clip. Ensure the clip exists in the specified location and ensure it is in MP3 format.", False)
            return
        self.pads[self.last_pressed_pad][1] = filename
        print("Successfully set pad " + self.pads[self.last_pressed_pad][0] + " audio clip location to \"" + filename + "\"")

    # called when the pad in the A1 place is pressed
    @Gtk.Template.Callback()
    def a1_pad_pressed(self, widget):
        self.press_pad(widget, 0)

    # called when the pad in the A2 place is pressed
    @Gtk.Template.Callback()
    def a2_pad_pressed(self, widget):
        self.press_pad(widget, 1)

    # called when the pad in the A3 place is pressed
    @Gtk.Template.Callback()
    def a3_pad_pressed(self, widget):
        self.press_pad(widget, 2)

    # called when the pad in the A4 place is pressed
    @Gtk.Template.Callback()
    def a4_pad_pressed(self, widget):
        self.press_pad(widget, 3)

    # called when the pad in the A5 place is pressed
    @Gtk.Template.Callback()
    def a5_pad_pressed(self, widget):
        self.press_pad(widget, 4)

    # called when the pad in the B1 place is pressed
    @Gtk.Template.Callback()
    def b1_pad_pressed(self, widget):
        self.press_pad(widget, 5)

    # called when the pad in the B2 place is pressed
    @Gtk.Template.Callback()
    def b2_pad_pressed(self, widget):
        self.press_pad(widget, 6)

    # called when the pad in the B3 place is pressed
    @Gtk.Template.Callback()
    def b3_pad_pressed(self, widget):
        self.press_pad(widget, 7)

    # called when the pad in the B4 place is pressed
    @Gtk.Template.Callback()
    def b4_pad_pressed(self, widget):
        self.press_pad(widget, 8)

    # called when the pad in the B5 place is pressed
    @Gtk.Template.Callback()
    def b5_pad_pressed(self, widget):
        self.press_pad(widget, 9)

    # called when the pad in the C1 place is pressed
    @Gtk.Template.Callback()
    def c1_pad_pressed(self, widget):
        self.press_pad(widget, 10)

    # called when the pad in the C2 place is pressed
    @Gtk.Template.Callback()
    def c2_pad_pressed(self, widget):
        self.press_pad(widget, 11)

    # called when the pad in the C3 place is pressed
    @Gtk.Template.Callback()
    def c3_pad_pressed(self, widget):
        self.press_pad(widget, 12)

    # called when the pad in the C4 place is pressed
    @Gtk.Template.Callback()
    def c4_pad_pressed(self, widget):
        self.press_pad(widget, 13)

    # called when the pad in the C5 place is pressed
    @Gtk.Template.Callback()
    def c5_pad_pressed(self, widget):
        self.press_pad(widget, 14)
