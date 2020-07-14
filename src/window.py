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

from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/nickgirga/musik/window.ui')
class MusikWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MusikWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def about_button_clicked(self, widget):
        widget.run()
        widget.destroy()

    @Gtk.Template.Callback()
    def preferences_button_clicked(self, widget):
        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Preferences page is currently under development.")
        message.run()
        message.destroy()
