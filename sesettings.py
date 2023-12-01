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
from tkinter import colorchooser
from tkinter import filedialog

from segpg import keyIds
from serecipients import RecipientsDialog
from setext import _, SSTE_NAME


#------------------------------------------------------------------------------
class SettingsDialog(Toplevel):
    '''Settings dialog for SSTE program.
    '''

    def __init__(self, parent, editor, config):

        Toplevel.__init__(self, parent)
        self.title(SSTE_NAME)
        self.editor = editor
        self.settings = config          # keep original configuration
        self.config = config.copy()     # local configuration copy

        # make modal
        self.transient(parent)
        self.grab_set()

        self._fgcolor = StringVar()
        self._fgcolor.set(self.config['fgcolor'])
        self._bgcolor = StringVar()
        self._bgcolor.set(self.config['bgcolor'])
        self._gnupg = StringVar()
        self._gnupg.set(self.config['gnupg'])
        self._gpgrcpts = StringVar()
        self._gpgrcpts.set(', '.join(self.config['gpgrcpts']))

        d = ttk.Label(self, text=_('Text color:'))
        d.grid(column=0, row=0, sticky=W, padx=2, pady=2)
        b = ttk.Button(self, width=25, textvariable=self._fgcolor,
                       command=self.onFGColor)
        b.grid(column=1, row=0, columnspan=2, sticky=(W,E), padx=2, pady=2)
        b.focus()

        d = ttk.Label(self, text=_('Background color:'))
        d.grid(column=0, row=1, sticky=W, padx=2, pady=2)
        b = ttk.Button(self, width=25, textvariable=self._bgcolor,
                       command=self.onBGColor)
        b.grid(column=1, row=1, columnspan=2, sticky=(W,E), padx=2, pady=2)

        d = ttk.Label(self, text=_('GnuPG path:'))
        d.grid(column=0, row=2, sticky=W, padx=2, pady=2)
        b = ttk.Button(self, width=25, textvariable=self._gnupg,
                       command=self.onGnuPG)
        b.grid(column=1, row=2, columnspan=2, sticky=(W,E), padx=2, pady=2)

        d = ttk.Label(self, text=_('GnuPG default recipients:'))
        d.grid(column=0, row=3, sticky=W, padx=2, pady=2)
        b = ttk.Button(self, width=25, textvariable=self._gpgrcpts,
                       command=self.onRecipients)
        b.grid(column=1, row=3, columnspan=2, sticky=(W,E), padx=2, pady=2)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=4, columnspan=3, sticky=(W,E), padx=5, pady=5)

        cancel = ttk.Button(self, text=_('Cancel'), command=self.onCancel)
        cancel.grid(row=5, column=1, sticky=(W, E), padx=2, pady=5)
        ok = ttk.Button(self, text=_('Ok'), command=self.onOk)
        ok.grid(row=5, column=2, sticky=(W, E), padx=2, pady=5)

        self.bind('<Return>', self.onOk)
        self.bind('<Escape>', self.onCancel)


    def onFGColor(self, *args):
        '''Choose text color.
        '''
        c = colorchooser.askcolor(title=_('Text color'),
                                  initialcolor=self.config['fgcolor'])
        if c[1]:
            self.config['fgcolor'] = c[1] 
            self._fgcolor.set(self.config['fgcolor'])
            self.editor['foreground'] = self.config['fgcolor']
            self.editor['insertbackground'] = self.config['fgcolor']


    def onBGColor(self, *args):
        '''Choose background color.
        '''
        c = colorchooser.askcolor(title=_('Background color'),
                                  initialcolor=self.config['bgcolor'])
        if c[1]:
            self.config['bgcolor'] = c[1] 
            self._bgcolor.set(self.config['bgcolor'])
            self.editor['background'] = self.config['bgcolor']


    def onGnuPG(self, *args):
        '''Choose GnuPG path.
        '''
        p = filedialog.askopenfilename(title=_('GnuPG path'),
                                       initialfile=self.config['gnupg'])
        if p:
            self.config['gnupg'] = p 
            self._gnupg.set(self.config['gnupg'])


    def onRecipients(self, *args):
        '''Choose GnuPG default recipients.
        '''
        settings = {
                'recipients': keyIds(self.config['gnupg']),
                'selected': self.config['gpgrcpts']
        }
        rd = RecipientsDialog(self, settings)
        self.wait_window(rd)

        if settings['selected'] is not None:
            self.config['gpgrcpts'] = settings['selected']
            self._gpgrcpts.set(', '.join(self.config['gpgrcpts']))


    def onOk(self, *args):
        '''Aplly new configuration.
        '''
        for k in self.config:
            self.settings[k] = self.config[k]
        self.destroy()


    def onCancel(self, *args):
        '''Revert configuration to original settings.
        '''
        self.editor['foreground'] = self.settings['fgcolor']
        self.editor['background'] = self.settings['bgcolor']
        self.editor['insertbackground'] = self.settings['fgcolor']
        self.destroy()
