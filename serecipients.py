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
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = '1.0'
__date__ = '2023-11-28'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


from tkinter import *
from tkinter import ttk

from setext import SSTE_NAME
from setext import _


#------------------------------------------------------------------------------
class RecipientsDialog(Toplevel):
    '''Dialog to choose list of GnuPG recipients.
    '''

    def __init__(self, parent, settings):

        Toplevel.__init__(self, parent)
        self.title(SSTE_NAME)
        self.settings = settings
        self.settings['recipients'].sort()

        # make modal
        self.transient(parent)
        self.grab_set()

        items = Variable(value=self.settings['recipients'])

        lbl = ttk.Label(self, text=_('Select GnuPG recipients:'))
        self.listbox = Listbox(self, listvariable=items,
                                     height=15, selectmode=MULTIPLE)
        vscroll = ttk.Scrollbar(self, orient=VERTICAL,
                                      command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=vscroll.set)
        clearAll = ttk.Button(self, text=_('Clear All'), command=self.onClearAll)
        selAll = ttk.Button(self, text=_('Select All'), command=self.onSelectAll)
        cancel = ttk.Button(self, text=_('Cancel'), command=self.onCancel)
        ok = ttk.Button(self, text=_('Ok'), command=self.onOk)

        lbl.grid(row=0, column=0, columnspan=5, sticky=W, padx=2, pady=5)
        self.listbox.grid(row=1, column=0, columnspan=4, sticky=(W,N,E,S))
        vscroll.grid(row=1, column=4, sticky=(N, S))
        clearAll.grid(row=2, column=0, sticky=(W, E), padx=5, pady=10)
        selAll.grid(row=2, column=1, sticky=(W, E), padx=5, pady=10)
        cancel.grid(row=2, column=2, sticky=(W, E), padx=5, pady=10)
        ok.grid(row=2, column=3, sticky=(W, E), padx=5, pady=10)

        # pre-select items in listbox
        for i in self.settings['selected']:
            self.listbox.select_set(self.settings['recipients'].index(i))

        self.listbox.focus()

        self.bind('<Return>', self.onOk)
        self.bind('<Escape>', self.onCancel)


    def onClearAll(self, *args):
        '''Clear all selected items.
        '''
        self.listbox.select_clear(0, END)


    def onSelectAll(self, *args):
        '''Select all items.
        '''
        self.listbox.select_set(0, END)


    def onOk(self, *args):
        '''Get selected recipients.
        '''
        self.settings['selected'] = [ self.listbox.get(i)
                                      for i in self.listbox.curselection() ]
        self.destroy()


    def onCancel(self, *args):
        '''Change selected recipients to None, as operation was cancelled.
        '''
        self.settings['selected'] = None
        self.destroy()
