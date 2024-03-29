"""Secure Simple Text Editor related stuff

Editor for secure (encrypted) simple text files
Copyright (C) 2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = '1.2'
__date__ = '2023-12-20'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import os
import sys
import gettext


#------------------------------------------------------------------------------
# bind gettext domain (internationalization)
gettext.bindtextdomain('sste', os.path.join(sys.path[0], 'locales'))
gettext.textdomain('sste')
_ = gettext.gettext


#------------------------------------------------------------------------------
def labelUnderline(label):
    '''Format Tkinter menu label from general format.
       label: label with underscore before letter to underline
       Returns tuple (Tkinter label, Tkinter underline position).
    '''
    i = label.find('_')
    return (label[:i] + label[i+1:], i)


#------------------------------------------------------------------------------
# Defaults text

DEFAULT_FILENAME = _('[ New secure text file ]')


#------------------------------------------------------------------------------
# Legal stuff constants

try:
    SSTE_VERSION = open(os.path.join(sys.path[0], '__version__')).read().strip()
except:
    SSTE_VERSION = __version__

SSTE_NAME = 'Secure Simple Text Editor'
SSTE_WEBSITE = 'https://github.com/ammdias/sste'
SSTE_WEBSITE_LABEL = 'AMMDIAS'
SSTE_SHORT_COPYRIGHT = _('''Editor for secure (encrypted) simple text files
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
along with this program.  If not, see <https://www.gnu.org/licenses/>.''')

SSTE_COPYRIGHT = _('''From the Preamble of the GNU General Public License:
        
The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

See the file 'gpl.txt' on the program's directory for more details.
If it's missing please refer to http://www.gnu.org/licenses/gpl.txt
''')

SSTE_WARRANTY = _('''From the GNU General Public License:
    
15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE
COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS"
WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY
AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

16. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
''')


#------------------------------------------------------------------------------
# Help text

SSTE_HELP = _('''
Secure Simple Text Editor

Copyright (C) 2019 António Manuel Dias
contact: ammdias@gmail.com

This program comes with ABSOLUTELY NO WARRANTY;  for details use command
'sste.py --warranty' or go to 'Help > Warranty' on the graphical user
interface.

This is free software, and you are welcome to redistribute it under certain
conditions; use command 'sste.py --copyright' or go to 'Help > Copyright' on
the graphical user interface for details.

----

SSTE is a text editor (simple text) that stores the files encrypted
by GnuPG, either with a symmetric encryption key or [several] public keys.

Encryption with public keys allows the sharing of an encrypted text document
by a group of people without the need to share a common password, encrypting the
document with the public keys of all people who needs access it. Encryption with
public keys is also convenient for a single user, as it doesn't require a
password input at saving the documents, only for opening.

Encryption with symmetric keys, the default, must be used when at least one of
the users doesn't have a GnuPG private/public key pair.

Depends on Python 3.4+, with Tkinter, and GnuPG 2.


Installation and first run
==========================

To install, simply uncompress the zip file, navigate to the uncompressed
directory and run 'sste.py' with Python 3.

Alternately, in Linux or other Unix-like operating system, you may use the
included installation script to install the program:

    $ python3 INSTALL.py

The program will try to find the GnuPG executable in the PATH.  If it can not
find it, it will prompt the user to manually provide the path in the Settings
Dialog (see below).  If GnuPG is not installed in your system, please download
it from the system's software store or, at your option, from the GnuPG site:

* https://gnupg.org/download/index.html


Usage
=====

The program works as any common graphical simple-text editor.  You may insert,
delete, select, copy and paste text as usual.  When saving, you will be prompted
to insert and confirm a password to encrypt the file.  Similarly, when opening
a file the program will ask for a password to decrypt the file.  If public keys
are used to encrypt the file, the password to the keys will only be asked when
opening the file.

Below is a description of the menu items and its actions:

File menu
---------

* New: start editing a new file.  If the file you were currently editing was
       modified since the last save you will be prompted to save it.

* Open: open a saved file.  When prompted insert the password used to encrypt
        the file or to open the private key to decrypt it.

* Save: save the current file. If you are using symmetric encryption, which is
        the default, enter the secret password to encrypt the file when
        prompted.

* Save as: save the current file with a different name.

* Save to: save the current file encrypted for a selected list of GnuPG
           recipients (using its public keys). Select all the intended
           recipients in the list and press 'Ok'. Only recipients in the
           default keyring and with valid public keys are shown.  Be sure to
           always select your public, in addition to the keys of all other
           recipients that need to access the file. If you forget to add your
           public key, you won't be able to open the file yourself, as
           only the users with the private keys corresponding to the chosen
           public keys can decrypt the file.

* Quit: close the program.  You will be prompted to save the file if it has
        changed since the last save.

Edit menu
---------

* Undo: undo most recent change in the text.

* Redo: redo most recent undo in the text.

* Cut: cut the selected text into the clipboard.

* Copy: copy the selected text to the clipboard.

* Paste: insert the clipboard text.

* Find: find pieces of text in the editor.  Insert the text to find in the
        dialog and press 'ENTER'.  If the text is found it will be selected and
        shown in the editor window.  If not found, a warning will be given
        that the end of the file was reached -- you may restart the search
        from the top of the file.  Press 'ESCAPE' to close the dialog.

* Replace: replace pieces of text in the editor.  Insert the text to find and
           the text to replace it in the dialog and press 'ENTER'.  If the
           text is found, you will be asked if you want to replace it.

* Select all: select all text in the editor.

* Settings: change the settings of the editor. Available options:

    * Text color: change the color of the text. Click the button to open the
            color choosing dialog.
    * Background color: change the background (paper) color.  Click the button
            to open the color choosing dialog.
    * GnuPG path: choose the correct path to the GnuPG executable.  Click the
            button to open the file dialog.
    * GnuPG default recipients. Click the button to open the recipients dialog.
            The default recipients (may be just one) are the public keys that
            will be used to encrypt all the files at saving time, except if
            using the 'Save To' option. Be sure to always select your public
            key, or you won't be able to open the file -- only the users with
            the corresponding private keys to the chosen public keys can decrypt
            the file.

Help menu
---------

* Manual: display this dialog.

* About: display information about the program.

* Copyright: display the copyright information.

* Warranty: display the warranty information.


Uninstall application
=====================

The program may be uninstalled from the terminal with the command:

    $ sste --uninstall

or, from within the folder where the program is installed:

    $ python3 UNINSTALL.py
''')
