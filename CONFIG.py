'''Installation script configuration file.
'''

DOC = 'Installation script for Secure Simple Text Editor.'
COPYRIGHT_YEAR = '2019'
VERSION = '0.3'
DATE = '2023-11-15'
AUTHOR = 'António Manuel Dias <ammdias@gmail.com>'
LICENSE = '''
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
'''


# List of file to be copied to installation the directory
FILES = ('sste.py', 'seditor.py', 'segpg.py', 'semessage.py', 'sesearch.py',
         'sesettings.py', 'setext.py', 'sste.desktop', 'sste.svg',
         '__version__', 'LICENSE.md', 'README.md', 'CHANGES.md')

# List of directories to be copied to the installation directory
TREES = ('locales',)

# Name of the icon file
ICO_FILE = 'sste.svg'

# Name of the desktop entry file (for GUI menus)
DESKTOP_FILE = 'sste.desktop'

# Name of the python file to be called to start the program
START_SCRIPT = 'sste.py'

# Name of the application (will be the name of the installation directory)
APP_NAME = 'sste'

# Name of the symbolic link to start the program
LINK_NAME = 'sste'

# List of configuration files
CONFIG_FILES = ()
