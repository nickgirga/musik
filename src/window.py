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

import os
from gi.repository import Gtk
from threading import Thread

@Gtk.Template(resource_path='/com/github/nickgirga/musik/window.ui')
class MusikWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MusikWindow'

    # create a nested list to represent the different pads and the locations of their audio clips
    pads = [["A1", "res/kick.mp3"],
                  ["A2", "res/snare.mp3"],
                  ["A3", "res/hat.mp3"],
                  ["A4", ""],
                  ["A5", ""],
                  ["B1", ""],
                  ["B2", ""],
                  ["B3", ""],
                  ["B4", ""],
                  ["B5", ""],
                  ["C1", ""],
                  ["C2", ""],
                  ["C3", ""],
                  ["C4", ""],
                  ["C5", ""]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # a general function used to play mp3 clips natively using mpg123
    def play_mp3_native(self, clip_path):
        thread = Thread(target = self.audio_thread, args = (clip_path, ))
        thread.start()

    def audio_thread(self, args):
        os.system("mpg123 " + args)

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
        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Sorry! This feature hasn't been implemented yet!")
        message.run()
        message.destroy()

    # this function is called any time a pad is pressed. `num` is the index of the stack that the pad's settings reside on
    def press_pad(self, widget, num):
        # get children
        label = widget.get_children()[0]
        my_file_chooser_button = widget.get_children()[1]

        # update label to match
        label.set_text("Pad " + self.pads[num][0] + " Settings")
        my_file_chooser_button.set_filename(self.pads[num][1])

        # get filename/path
        #temporarily omitted

        # verify file exists at specified path and play it using mpg123
        #if (type(filename) == type(None)): return
        #self.play_mp3_native(filename)

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
