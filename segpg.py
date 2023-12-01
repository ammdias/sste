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

__version__ = '1.0'
__date__ = '2023-11-28'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import re
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
        res = subprocess.run([gpg, '--version'], stdout=subprocess.DEVNULL)
    except:
        return False

    return res.returncode == 0


def encrypt(gpg, text, filename):
    '''Encrypt text with symmetric key.
    gpg: path to GnuPG executable.
    text: string with text to encrypt.
    filename: path to the output file.
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


def encryptTo(gpg, recipients, text, filename):
    '''Encrypt text with public key(s).
    gpg: path to GnuPG executable.
    recipients: list of GnuPG recipient email addresses.
    text: string with text to encrypt.
    filename: path to the output file.
    '''
    if not recipients:
        raise GnuPGError(_('At least one recipient must be given.'))

    try:
        recipients = [ f'--recipient={r}' for r in recipients ]
        res = subprocess.run([gpg, '--encrypt', *recipients, '--quiet', '--yes',
                                   '--output', filename],
                             capture_output=True,
                             input=text.encode(sys.stdin.encoding)) 
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if res.returncode != 0:
        raise GnuPGError(res.stderr.decode(sys.stdout.encoding))


def decrypt(gpg, filename):
    '''Decrypt encrypted file.
    gpg: path to GnuPG executable.
    filename: path to the encrypted file.
    Returns string with decrypted text.
    '''
    try:
        res = subprocess.run([gpg, '--decrypt', '--quiet', filename],
                             capture_output=True) 
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if res.returncode != 0:
        raise GnuPGError(res.stderr.decode(sys.stdout.encoding))

    return res.stdout.decode(sys.stdout.encoding)


def keyIds(gpg):
    '''Return list of available GnuPG public keys.
    gpg: path to GnuPG executable.
    '''
    try:
        res = subprocess.run([gpg, '--list-public-keys', '--with-colons'],
                             capture_output=True)
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if res.returncode != 0:
        raise GnuPGError(res.stderr.decode(sys.stdout.encoding))

    # GnuPG result with option --with-colons is always UTF-8 encoded
    keys = [ k.split(':') for k in res.stdout.decode('utf8').splitlines() ]

    # return list of email addresses if keys are not revoked or expired
    pattern = re.compile('<(.*)>')
    ids = [ re.search(pattern, k[9])
                for k in keys if k[0]=='uid' and k[1] not in ('r', 'e') ]

    return [ i.group(1) for i in ids if i ]
