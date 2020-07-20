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

import os, pyaudio, wave
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/github/nickgirga/musik/window.ui')
class MusikWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MusikWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # a general function used to play audio clips using pyaudio+wave
    def play_audio_clip_pyaudio(clip_name, chunk_size):
        # open sound file
        wf = wave.open(clip_name, 'rb')

        # create PortAudio interface
        p = pyaudio.PyAudio()

        #open .Stream object
        stream = p.open(format = p.get_format_from_width(wf.getsamplewidth()), channels = wf.getchannels(), rate = wf.getframerate(), output = True)

        # read data in chunks
        data = wf.readframes(chunk_size)

        #write to stream and play sound
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk_size)

        # close stream
        stream.close()

        # terminate interface
        p.terminate()

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

    # called when the pad in the A1 place is pressed
    @Gtk.Template.Callback()
    def a1_pad_pressed(self, widget):
        play_audio_clip_pyaudio("res/kick.wav", 1024)

    # called when the pad in the A2 place is pressed
    @Gtk.Template.Callback()
    def a2_pad_pressed(self, widget):
        playsound("res/snare.ogg")

    # called when the pad in the A3 place is pressed
    @Gtk.Template.Callback()
    def a3_pad_pressed(self, widget):
        playsound("res/hat.ogg")
