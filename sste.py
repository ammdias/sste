#!/usr/bin/python3

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

__version__ = '1.1'
__date__ = '2023-12-09'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import os
import sys
import argparse
import json

from setext import SSTE_NAME, SSTE_VERSION, SSTE_SHORT_COPYRIGHT, \
                   SSTE_COPYRIGHT, SSTE_WARRANTY
from setext import _
from seditor import start


#------------------------------------------------------------------------------
# default settings

config_files = (
    os.path.expanduser(os.path.join('~', '.sste')),
    os.path.expanduser(os.path.join('~', '.config', 'sste'))
)

for i in config_files:
    if os.path.exists(i):
        break
CONFIG_FILE = i

DEFAULT_CONFIG = {
    'fgcolor': 'black',
    'bgcolor': 'white',
    'gnupg': '',
    'gpgrcpts': []
}


#------------------------------------------------------------------------------
# process arguments and show information or start GUI

parser = argparse.ArgumentParser(description=
                                 SSTE_NAME + ' ' +  SSTE_VERSION)

parser.add_argument("filename", type=str, nargs='?', default='',
                    help=_('file to open'))

parser.add_argument("--gnupg", type=str, default='',
                    help=_('GnuPG command, including complete path if not on PATH'))

parser.add_argument("-c", "--copyright", action="store_true",
                    help=_('show copyright information.'))

parser.add_argument("-w", "--warranty", action="store_true",
                    help= _('show warranty information.'))

parser.add_argument("-v", "--version", action="store_true",
                    help=_('show version information.'))

parser.add_argument("--uninstall", action="store_true",
                    help=_('uninstall application'))

args = parser.parse_args()

# uninstall application
if args.uninstall:
    from UNINSTALL import uninstall
    uninstall()

# check options to show program information
if args.copyright:
    print(SSTE_NAME, SSTE_VERSION, '\n')
    print(SSTE_SHORT_COPYRIGHT, '\n')
    print(SSTE_COPYRIGHT)

elif args.warranty:
    print(SSTE_NAME, SSTE_VERSION, '\n')
    print(SSTE_SHORT_COPYRIGHT, '\n')
    print(SSTE_WARRANTY)

elif args.version:
    print(SSTE_NAME, SSTE_VERSION, '\n')
    print(SSTE_SHORT_COPYRIGHT)

# no 'show' options, start the program
else:
    try:
        config = json.loads(open(CONFIG_FILE, 'r').read())
        for k in DEFAULT_CONFIG:  # set missing options, if any
            if k not in config:
                config[k] = DEFAULT_CONFIG[k]
    except:
        print(_("Could not load '.config' file.\n"
                "Starting with default configuration."))
        config = DEFAULT_CONFIG
    
    # check GnuPG path option
    if args.gnupg:
        config['gnupg'] = args.gnupg

    # start the program
    try:
        start(config, args.filename)

        # save settings at program exit
        open(CONFIG_FILE, 'w').write(json.dumps(config, indent=4))
    except KeyboardInterrupt:
        pass
