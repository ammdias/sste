"""SSTE GnuPG communication library
 
Secure simple-text editor
Use 'gpg' to encrypt and decrypt text with symmetric cypher
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

__version__ = '0.3'
__date__ = '2023-11-12'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import sys
import subprocess
from setext import _


#------------------------------------------------------------------------------
# Exceptions

class GnuPGError(Exception):
    '''Generic GnuPG error.
    '''
    pass


#------------------------------------------------------------------------------
# public interface

def checkGnuPG(gpg):
    '''Check ig GnuPG is available.
    gpg: path to GnuPG executable.
    '''

    try:
        res = subprocess.run([gpg, '--version'])
    except:
        return False

    return res.returncode == 0


def encrypt(gpg, text, filename):
    '''Encrypt text with password.
    gpg: path to GnuPG executable.
    passwd: passphrase to use in encryption.
    text: string with text to encrypt.
    Return bytes array with encrypted text.
    '''
    try:
        res = subprocess.run([gpg, '--symmetric', '--quiet', '--yes',
                                   '--output', filename],
                             capture_output=True,
                             input=text.encode(sys.stdin.encoding)) 
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if res.returncode != 0:
        raise GnuPGError(res.stderr.decode(sys.stdout.encoding))


def decrypt(gpg, filename):
    '''Decrypt text with password.
    gpg: path to GnuPG executable.
    passwd: passphrase to use in decryption.
    text: bytes array with encrypted text.
    Returns string with decrypted text.'''
    try:
        res = subprocess.run([gpg, '--decrypt', '--quiet', filename],
                             capture_output=True) 
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if res.returncode != 0:
        raise GnuPGError(res.stderr.decode(sys.stdout.encoding))

    return res.stdout.decode(sys.stdout.encoding)

