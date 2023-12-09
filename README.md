Secure Simple Text Editor
=========================
version 1.1

Copyright (C) 2019 António Manuel Dias

contact: ammdias@gmail.com

website: [AMMDIAS GitHub](https://github.com/ammdias/sste)

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


## ABOUT THE PROGRAM

This is a text editor (simple text) that stores the files encrypted
by GnuPG, either with a symmetric encryption key or [several] public keys.

Encryption with public keys allows the sharing of an encrypted text document
by a group of people without the need to share a common password, encrypting the
document with the public keys of all people who needs access it. Encryption with
public keys is also convenient for a single user, as it doesn't require a
password input at saving the documents, only for opening.

Encryption with symmetric keys, the default, must be used when at least one of
the users doesn't have a GnuPG private/public key pair.

Depends on Python 3.4+, with Tkinter, and GnuPG 2.


## INSTALLATION (any system)

Before using, confirm that you have GnuPG and Python 3 with Tkinter installed
on your system.  If not, get them from your system's software store or from
the official download sites:

* Python: https://www.python.org/downloads/
* GnuPG:  https://gnupg.org/download/index.html

The program needs no special installation: just unzip the the compressed
file and run 'sste.py' with Python 3.  Read the program's help for further
instructions on how to use it.


## INSTALLATION (Linux systems)

You may properly install the program on a Linux system executing the provided
installation script, following these instructions:

1. Download the zip file containing the program and uncompress it. Then, open a
   terminal in the directory where the program was uncompressed and run the
   installation script with Python 3:

         $ python3 INSTALL.py

   You will be prompted for the installation directory --- i.e. the directory
   under which the folder containing all the application files will be placed
   --- and for the start link directory --- i.e. the directory where the
   symbolic link for the program will be created. The installation script
   will also ask you for the icon and desktop application file diretories.

   The default directories will install the program for the current user only
   and are suited for single-user systems.  If you want to keep these
   settings, just press ENTER when prompted.  The program will be installed in
   the directory `$HOME/.local/lib/sste` and the symbolic link
   `$HOME/.local/bin/sste` will be created.  On most Linux systems the
   `$HOME/.local/bin` directory will be inserted in the execution PATH, if it
   exists. If it doesn't, you will have to add it manually. The icon and
   desktop app file will be added to the respective `$HOME/.local/share`
   directories.

   If you want to install the program for all the users of the system, you
   should change the directories accordingly, e.g. `/usr/local/lib` for the
   installation directory and `/usr/local/bin` for the start link.  Of
   course, you will need to run the installation script with administration
   privileges:

         $ sudo python3 INSTALL.py

   If a previous installation exists on the selected directory, you will be
   asked if you want to overwrite it.  Answer "`yes`" (or just "`y`") if that
   is the case or "`no`"/"`n`" if not.
     
2. Test that the installation was successful with the command:

         $ sste

   Then, find the program in your desktop environment start menu and run it.

3. You may uninstall application with:

         $ sste --uninstall


## BUILD A NEW LOCALE (for localizers)

* Install gettext package:

        $ sudo apt install gettext
    
* Generate new template file:

        $ mv locales/sste.pot locales/sste.pot.old
        $ pygettext3 -o locales/sste.pot *.py
    
* Generate mo file (below, replace lo_LO by the Locale to be built (e.g en_US)):

        $ mkdir -p locales/lo_LO/LC_MESSAGES
        $ cd locales/lo_LO/LC_MESSAGES
        $ cp ../../sste.pot sste.po
        
  Translate the file (see locales/pt_PT for example) and then:
  
        $ msgfmt -o sste.mo sste
        
  Test the translation:
  
        $ cd ../../..
        $ LC_ALL=lo_LO.utf8 python3 sste.py
