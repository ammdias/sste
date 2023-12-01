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
from tkinter import messagebox

from setext import SSTE_NAME
from setext import _


#------------------------------------------------------------------------------
class SearchDialog(Toplevel):
    '''Text search dialog for SSTE program.
    '''

    def __init__(self, parent, editor, replace):

        Toplevel.__init__(self, parent)
        self.title(SSTE_NAME)
        self.replace = replace
        self.editor = editor

        # make modal
        self.transient(parent)
        self.grab_set()

        self._search = StringVar()
        d = ttk.Label(self, text=_('Find text:'))
        d.grid(column=0, row=0, sticky=W, padx=2, pady=2)
        t = ttk.Entry(self, width=20, textvariable=self._search)
        t.grid(column=0, row=1, columnspan=3, sticky=(W, E), padx=2, pady=2)
        t.focus()
        
        buttonrow = 2
        if replace:
            self._replace = StringVar()
            d = ttk.Label(self, text=_('Replace with:'))
            d.grid(column=0, row=2, sticky=W, padx=2, pady=2)
            t = ttk.Entry(self, width=20, textvariable=self._replace)
            t.grid(column=0, row=3, columnspan=3, sticky=(W, E), padx=2, pady=2)
            buttonrow = 4

        close = ttk.Button(self, text=_('Close'), command=self.onClose)
        close.grid(row=buttonrow, column=1, sticky=(W, E), padx=5, pady=10)
        search = ttk.Button(self, text=_('Search'), command=self.onSearch)
        search.grid(row=buttonrow, column=2, sticky=(W, E), padx=5, pady=10)

        self.bind('<Return>', self.onSearch)
        self.bind('<Escape>', self.onClose)


    def onSearch(self, *args):
        '''Search text in editor text widget.'''
        # unselect any currently selected text
        self.editor.tag_remove('sel', '1.0', 'end')

        countVar = StringVar()
        start = self.editor.search(self._search.get(), 'insert', nocase=True,
                                   stopindex='end', count=countVar)
        if start:
            end = '{}+{}c'.format(start, countVar.get())
            self.editor.see(start)
            self.editor.tag_add('sel', start, end)
            if self.replace:
                if messagebox.askyesno(title=SSTE_NAME,
                                       message=_('Replace text'),
                                       detail=_('Replace current selection?'),
                                       icon='question'):
                    self.editor.delete(start, end)
                    self.editor.insert(start, self._replace.get())
                    end = '{}+{}c'.format(start, len(self._replace.get()))
                else:
                    self.editor.tag_remove(start, end)
            self.editor.mark_set('insert', end)
        else:
            if messagebox.askyesno(title=SSTE_NAME,
                                   message=_('Text not found.'),
                                   detail=_('Go to top of document?'),
                                   icon='question'):
                # unselect currently selected text
                self.editor.tag_remove('sel', '1.0', 'end')
                self.editor.mark_set('insert', '1.0')
                self.editor.see('1.0')
            else:
                self.destroy()


    def onClose(self, *args):
        self.destroy()
