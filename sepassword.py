"""Secure Simple Text Editor

Editor for secure (encrypted) simple text files
(C) 2019 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

__version__ = '0.2'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


#------------------------------------------------------------------------------
# Changes history:
#  0.1 (2019/Oct.31): First version


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from setext import SSTE_NAME
from setext import _


#------------------------------------------------------------------------------
class PasswordDialog(Toplevel):
    '''Password dialog for SSTE program.
    '''

    def __init__(self, parent, confirm):

        Toplevel.__init__(self, parent)
        self.title(SSTE_NAME)
        self._confirm = confirm

        # make modal
        self.transient(parent)
        self.grab_set()

        self._passwd = StringVar()
        self._passwdconf = StringVar()
        self.password = ''

        d = ttk.Label(self, text=_('Password:'))
        d.grid(column=0, row=0, sticky=W, padx=2, pady=2)
        p = ttk.Entry(self, textvariable=self._passwd, show='*')
        p.grid(column=0, row=1, sticky=(W, E), padx=2, pady=2)

        if self._confirm:
            d = ttk.Label(self, text=_('Confirm:'))
            d.grid(column=0, row=2, sticky=W, padx=2, pady=2)
            c = ttk.Entry(self, textvariable=self._passwdconf, show='*')
            c.grid(column=0, row=3, sticky=(W, E), padx=2, pady=2)

        p.focus()

        self.bind('<Return>', self.onClose)
        self.bind('<Escape>', self.onQuit)


    def onClose(self, *args):
        if not self._confirm or self._passwd.get() == self._passwdconf.get():
            self.password = self._passwd.get()
            self.destroy()
        else:
            messagebox.showinfo(parent=self,
                                title=SSTE_NAME,
                                message=_('Error:'),
                                detail=_("Entered passwords don't match."),
                                icon='error')

    def onQuit(self, *args):
        self.destroy()
