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
#  0.1 (2019/Oct.31):  first version


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from setext import *
from setext import _

from semessage import TextDialog
from sesearch import SearchDialog
from sepassword import PasswordDialog
from sesettings import SettingsDialog
from segpg import checkGnuPG, encrypt, decrypt, BadPassword, GnuPGError


#-------------------------------------------------------------------------------
# Editor class

class SecureEditor():
    '''Main editor window class.'''

    def __init__(self, win, config, filename=''):
        '''SecureEditor constructor.
        win: parent window
        config: configuration dictionary
        filename: path to filename to open
        '''
        self.win = win
        self.win.title(SSTE_NAME)
        self.win.option_add('*tearOff', FALSE)
        self.config = config

        self.text = Text(win, undo=TRUE, wrap='none')
        vscrl = ttk.Scrollbar(win, orient=VERTICAL, command=self.text.yview)
        hscrl = ttk.Scrollbar(win, orient=HORIZONTAL, command=self.text.xview)
        self.text.configure(yscrollcommand=vscrl.set,
                            xscrollcommand=hscrl.set)
        self.text['foreground'] = self.config['fgcolor']
        self.text['background'] = self.config['bgcolor']
        self.text['insertbackground'] = self.config['fgcolor']

        self.text.grid(column=0, row=0, sticky=(W,N,E,S))
        vscrl.grid(column=1, row=0, sticky=(N,S))
        hscrl.grid(column=0, row=1, sticky=(W,E))
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)

        self.buildMenu()
        self.bindAccelerators()

        if not checkGnuPG(self.config['gnupg']):
            self.getGnuPGPath()

        if filename:
            self.filename = filename
            self.openFile()
        else:
            self.onNew()


    #--------------------------------------------------------------------------
    # user interface commands

    def onNew(self, *args):
        '''Create new document.
        '''
        if self.safeToCloseDoc():
            self.filename = DEFAULT_FILENAME
            self.text.delete('1.0', 'end')
            self.text.focus()
            self.text.edit_modified(0)


    def onOpen(self, *args):
        '''Open document.
        '''
        if self.safeToCloseDoc():
            f = filedialog.askopenfilename()
            if f:
                self.filename = f
                self.openFile()


    def onSave(self, *args):
        '''Save document.
        '''
        if self.filename == DEFAULT_FILENAME:
            f = filedialog.asksaveasfilename()
            if f:
                self.filename = f
            else:
                return False
        self.saveFile()
        return True


    def onSaveAs(self, *args):
        '''Save document in a new file.
        '''
        f = filedialog.asksaveasfilename()
        if f:
            self.filename = f
            self.saveFile()


    def onQuit(self, *args):
        '''Close program.
        '''
        if self.safeToCloseDoc():
            self.win.destroy()


    def onFind(self, *args):
        '''Open Find dialog.
        '''
        SearchDialog(self.win, self.text, replace=False)


    def onReplace(self, *args):
        '''Open Replace dialog.
        '''
        SearchDialog(self.win, self.text, replace=True)


    def onSelectAll(self, *args):
        '''Select all text.
        '''
        self.text.tag_add('sel', "1.0", 'end')


    def onSettings(self, *args):
        '''Change application settings.
        '''
        SettingsDialog(self.win, self.text, self.config)


    def onManual(self, *args):
        '''Show Help dialog.
        '''
        self.infoDialog(SSTE_HELP)


    def onAbout(self, *args):
        '''Show About dialog.
        '''
        messagebox.showinfo(message='{} {}'.format(SSTE_NAME, SSTE_VERSION),
                            detail='{}\n\n{}'.format(SSTE_SHORT_COPYRIGHT,
                                                     SSTE_WEBSITE),
                            title=SSTE_NAME)


    def onCopyright(self, *args):
        '''Show Copyright dialog.
        '''
        self.infoDialog('{} {}\n{}\n\n{}'.format(SSTE_NAME, SSTE_VERSION,
                                                 SSTE_SHORT_COPYRIGHT,
                                                 SSTE_COPYRIGHT))


    def onWarranty(self, *args):
        '''Show Warranty dialog.
        '''
        self.infoDialog('{} {}\n{}\n\n{}'.format(SSTE_NAME, SSTE_VERSION,
                                                 SSTE_SHORT_COPYRIGHT,
                                                 SSTE_WARRANTY))


    #--------------------------------------------------------------------------
    # utility functions

    def getGnuPGPath(self):
        '''Guess GnuPG path or get it from user.
        '''
        for path in ['gpg', 'gpg.exe']:
            if checkGnuPG(path):
                self.config['gnupg'] = path
                return
        
        self.config['gnupg'] = ''
        self.error('Could not find GnuPG in the PATH.\n'
                   'Please configure it manually.')
        self.onSettings()


    def error(self, message):
        '''Show error message.
        '''
        messagebox.showinfo(parent=self.win,
                            title=SSTE_NAME,
                            message=_('Error'),
                            detail=message,
                            icon='error')


    def infoDialog(self, message):
        '''Build and show information dialog with title and message.
        '''
        self.win.wait_window(TextDialog(self.win, message))


    def safeToCloseDoc(self):
        '''Show safe to close dialog.
        '''
        if self.text.edit_modified():
            if messagebox.askyesno(
                    message=('Close document'),
                    detail=_('File has changed. Do you want to save it?'),
                    title=SSTE_NAME,
                    icon='question'):
                return self.onSave()

        return True


    def openFile(self):
        '''Open and decrypt file.
        '''
        passwd = self.getPassword(confirm=False)
        if passwd:
            try:
                text = open(self.filename, 'rb').read()
            except:
                self.error(_('Could not open file.'))
                self.filename = DEFAULT_FILENAME
                return

            try:
                text = decrypt(self.config['gnupg'], text, passwd)
            except BadPassword:
                self.error(_('Wrong password.'))
                return
            except GnuPGError as e:
                self.error(_('GnuPG error:\n{}').format(str(e)))
                return
            except Exception as e:
                self.error(e)
                return

            self.text.delete('1.0', 'end')
            self.text.insert('1.0', text)
            self.text.mark_set('insert', '1.0')
            self.text.see('insert')
            self.text.edit_modified(0)

    
    def saveFile(self):
        '''Encrypt and save file.
        '''
        passwd = self.getPassword(confirm=True)
        if passwd:
            try:
                text = encrypt(self.config['gnupg'],
                               self.text.get('1.0', 'end'), passwd)
            except GnuPGError as e:
                self.error(_('GnuPG error:\n{}').format(str(e)))
                return
            except Exception as e:
                self.error(e)
                return

            try:
                open(self.filename, 'wb').write(text)
            except:
                self.error(_('Could not write to file.'))
                self.filename = DEFAULT_FILENAME
                return
            
            self.text.edit_modified(0)


    def getPassword(self, confirm):
        '''Show get password dialog.
        '''
        passdialog = PasswordDialog(self.win, confirm)
        self.win.wait_window(passdialog)
        return passdialog.password


    #--------------------------------------------------------------------------
    # user interce building functions

    def buildMenu(self):
        '''Build and insert all menus.
        '''
        menubar = Menu(self.win)
        self.win['menu'] = menubar
        
        # File menu
        fileMenu = Menu(menubar)
        lbl, pos = labelUnderline(_('_File'))
        menubar.add_cascade(menu=fileMenu, label=lbl, underline=pos)
        lbl, pos = labelUnderline(_('_New'))
        fileMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+N'), command=self.onNew)
        lbl, pos = labelUnderline(_('_Open...'))
        fileMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+O'), command=self.onOpen)
        lbl, pos = labelUnderline(_('_Save'))
        fileMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+S'), command=self.onSave)
        lbl, pos = labelUnderline(_('Save _As...'))
        fileMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+Shift+S'), command=self.onSaveAs)
        fileMenu.add_separator()
        lbl, pos = labelUnderline(_('_Quit'))
        fileMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+Q'), command=self.onQuit)

        # Edit Menu
        editMenu = Menu(menubar)
        lbl, pos = labelUnderline(_('_Edit'))
        menubar.add_cascade(menu=editMenu, label=lbl, underline=pos)
        lbl, pos = labelUnderline(_('_Undo'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+Z'),
                             command=self.text.edit_undo)
        lbl, pos = labelUnderline(_('Re_do'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+Shift+Z'),
                             command=self.text.edit_redo)
        editMenu.add_separator()
        lbl, pos = labelUnderline(_('Cu_t'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+X'),
                             command=lambda: self.text.event_generate('<<Cut>>'))
        lbl, pos = labelUnderline(_('_Copy'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+C'),
                             command=lambda:
                                 self.text.event_generate('<<Copy>>'))
        lbl, pos = labelUnderline(_('_Paste'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+V'),
                             command=lambda:
                                 self.text.event_generate('<<Paste>>'))
        editMenu.add_separator()
        lbl, pos = labelUnderline(_('_Find...'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+F'), command=self.onFind)
        lbl, pos = labelUnderline(_('_Replace...'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+R'), command=self.onReplace)
        editMenu.add_separator()
        lbl, pos = labelUnderline(_('Select _All'))
        editMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('Ctrl+A'), command=self.onSelectAll)
        editMenu.add_separator()
        lbl, pos = labelUnderline(_('_Settings...'))
        editMenu.add_command(label=lbl, underline=pos,
                             command=self.onSettings)

        # Help Menu
        helpMenu = Menu(menubar)
        lbl, pos = labelUnderline(_('_Help'))
        menubar.add_cascade(menu=helpMenu, label=lbl, underline=pos)
        lbl, pos = labelUnderline(_('_Manual'))
        helpMenu.add_command(label=lbl, underline=pos,
                             accelerator=_('F1'), command=self.onManual)
        helpMenu.add_separator()
        lbl, pos = labelUnderline(_('_About'))
        helpMenu.add_command(label=lbl, underline=pos,
                             command=self.onAbout)
        lbl, pos = labelUnderline(_('_Copyright'))
        helpMenu.add_command(label=lbl, underline=pos,
                             command=self.onCopyright)
        lbl, pos = labelUnderline(_('_Warranty'))
        helpMenu.add_command(label=lbl, underline=pos,
                             command=self.onWarranty)


    def bindAccelerators(self):
        '''Bind all keyboard shortcuts.
        '''
        # File menu
        self.win.bind(_('<Control-n>'), self.onNew)
        self.win.bind(_('<Control-o>'), self.onOpen)
        self.win.bind(_('<Control-s>'), self.onSave)
        self.win.bind(_('<Control-S>'), self.onSaveAs)
        self.win.bind(_('<Control-q>'), self.onQuit)

        # Edit menu
        self.win.bind(_('<Control-f>'), self.onFind)
        self.win.bind(_('<Control-r>'), self.onReplace)
        self.win.bind(_('<Control-a>'), self.onSelectAll)

        # Help menu
        self.win.bind(_('<F1>'), self.onManual)


#------------------------------------------------------------------------------
# Initiate editor

def start(config, filename):
    '''Create main window and start the program.'''
    win = Tk()
    SecureEditor(win, config, filename)
    win.mainloop()

