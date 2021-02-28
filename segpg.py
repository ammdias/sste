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
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

__version__ = '0.2'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


#------------------------------------------------------------------------------
# Changes history:
#  0.1 (2019/Oct.31):    first version


from setext import _
from subprocess import check_call, Popen, PIPE, DEVNULL


#------------------------------------------------------------------------------
# Exceptions

class BadPassword(Exception):
    '''Wrong password in decryption.
    '''
    pass

class GnuPGError(Exception):
    '''Generic GnuPG error.
    '''
    pass


#------------------------------------------------------------------------------
# utility functions

def _execute(gpg, text, passwd, cmd):
    '''Execute GnuPG with command 'cmd' and return answer.
    '''
    try:
        proc = Popen((gpg, cmd, '--batch', '--quiet', '--passphrase', passwd),
                      stdin=PIPE, stdout=PIPE, stderr=PIPE)
        text, err = proc.communicate(text)
    except:
        raise Exception(_('Could not execute GnuPG.'))

    if err:
        err = err.decode(encoding='utf-8')
        if 'Bad session key' in err:
            raise BadPassword
        raise GnuPGError(e)

    return text


#------------------------------------------------------------------------------
# public interface

def checkGnuPG(gpg):
    '''Check ig GnuPG is available.
    gpg: path to GnuPG executable.
    '''
    try:
        check_call((gpg, '--version'), stdout=DEVNULL, stderr=DEVNULL)
    except:
        return False

    return True


def encrypt(gpg, text, passwd):
    '''Encrypt text with password.
    gpg: path to GnuPG executable.
    passwd: passphrase to use in encryption.
    text: string with text to encrypt.
    Return bytes array with encrypted text.
    '''
    return _execute(gpg, bytes(text, encoding='utf-8'), passwd, '-c')


def decrypt(gpg, text, passwd):
    '''Decrypt text with password.
    gpg: path to GnuPG executable.
    passwd: passphrase to use in decryption.
    text: bytes array with encrypted text.
    Returns string with decrypted text.'''
    return _execute(gpg, text, passwd, '-d').decode(encoding='utf-8')

