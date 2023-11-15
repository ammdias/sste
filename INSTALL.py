#!/usr/bin/env python3
'''Installation script.
'''

import sys
import os.path
import shutil

from CONFIG import *


PKG_DIR = sys.path[0]
INSTALL_DIR = os.path.join('~', '.local', 'lib')
BIN_DIR = os.path.join('~', '.local', 'bin')
ICO_DIR = os.path.join('~', '.local', 'share', 'icons')
APP_DIR = os.path.join('~', '.local', 'share', 'applications')
CONFIG_DIR = os.path.join('~', '.config')


def _quit(msg):
    '''Print error message and quit.
    '''
    print(f'Error: {msg}\n', file=sys.stderr)
    sys.exit(1)


def yesno(question):
    '''Get a yes or no answer to a question.
    '''
    answer = ''
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = input(f'{question} (y/n): ').strip().lower()

    return answer in ('y', 'yes')


try:
    # print greeting
    print(DOC)
    print('Version:', VERSION)
    print('Copyright (C)', COPYRIGHT_YEAR, AUTHOR)
    print(LICENSE)


    # get installation directories
    d = input(f'Installation directory [{INSTALL_DIR}]: ').strip()
    INSTALL_DIR = os.path.expanduser(os.path.join(d or INSTALL_DIR, APP_NAME))
    START_SCRIPT_PATH = os.path.join(INSTALL_DIR, START_SCRIPT)
    if ICO_FILE:
        ICO_FILE_PATH = os.path.join(INSTALL_DIR, ICO_FILE)
    if DESKTOP_FILE:
        DESKTOP_FILE_PATH = os.path.join(INSTALL_DIR, DESKTOP_FILE)

    d = input(f'Start link directory [{BIN_DIR}]: ').strip()
    BIN_DIR = os.path.expanduser(d or BIN_DIR)
    LINK_PATH = os.path.join(BIN_DIR, LINK_NAME)

    if ICO_FILE:
        d = input(f'Icons directory [{ICO_DIR}]: ').strip()
        ICO_DIR = os.path.expanduser(d or ICO_DIR)
        ICO_PATH = os.path.join(ICO_DIR, ICO_FILE)
    else:
        ICO_PATH = None

    if DESKTOP_FILE:
        d = input(f'Applications directory [{APP_DIR}]: ').strip()
        APP_DIR = os.path.expanduser(d or APP_DIR)
        APP_PATH = os.path.join(APP_DIR, DESKTOP_FILE)
    else:
        APP_PATH = None

    if CONFIG_FILES:
        d = input(f'Configuration files directory [{CONFIG_DIR}]: ').strip()
        CONFIG_DIR = os.path.expanduser(d or CONFIG_DIR)
        if len(CONFIG_FILES) > 1:
            CONFIG_DIR = os.path.join(CONFIG_DIR, APP_NAME)

    print()


    # check if install path exists and clean it if it does
    if PKG_DIR in (INSTALL_DIR, BIN_DIR, ICO_DIR, APP_DIR, CONFIG_DIR):
        _quit("Installation directory cannot be the same as package directory.")
    try:
        if os.path.exists(INSTALL_DIR):
            try:
                with open(os.path.join(INSTALL_DIR, '__version__'), 'r') as f:
                    oldversion = f.read().strip()
            except:
                pass  # corrupted previous installation? just remove it.
            else:
                print(f'Version {VERSION} will be installed '
                      f'over existing version {oldversion}.')
                if not yesno('Proceed anyway?'):
                    _quit("Installation interrupted by user.")
                print()
            print('Removing old version...')
            shutil.rmtree(INSTALL_DIR)
        for p in (LINK_PATH, ICO_PATH, APP_PATH):
            if p and os.path.lexists(p):
                print(f'Removing old symbolic link {p}...')
                os.remove(p)
    except Exception as e:
        _quit(f"Could not remove old installation. Reason:\n{e}")


    # copy files to install directory
    try:
        print('Creating installation directories...')
        os.makedirs(INSTALL_DIR)
        print('Copying files:')
        for i in FILES:
            print(f'... {i}')
            shutil.copy2(os.path.join(PKG_DIR, i), INSTALL_DIR) 
        for i in TREES:
            print(f'... /{i}/')
            shutil.copytree(os.path.join(PKG_DIR, i),
                            os.path.join(INSTALL_DIR, i))
    except Exception as e:
        _quit(f"Could not copy files to installation directory. Reason:\n{e}")


    # make symbolic links
    try:
        print('Creating symbolic link to startup script...')
        os.chmod(START_SCRIPT_PATH, 0o755)
        os.makedirs(BIN_DIR, exist_ok=True)
        os.symlink(START_SCRIPT_PATH, LINK_PATH)
    except Exception as e:
        _quit(f"Could not create symbolic link to application script. Reason:\n{e}")

    if ICO_FILE:
        try:
            print('Creating symbolic link to icon...')
            os.makedirs(ICO_DIR, exist_ok=True)
            os.symlink(ICO_FILE_PATH, ICO_PATH)
        except Exception as e:
            _quit(f"Could not create symbolic link to icon. Reason:\n{e}")

    if DESKTOP_FILE:
        try:
            print('Creating symbolic link to desktop file...')
            os.makedirs(APP_DIR, exist_ok=True)
            os.symlink(DESKTOP_FILE_PATH, APP_PATH)
        except Exception as e:
            _quit(f"Could not create symbolic link to desktop file. Reason:\n{e}")


    # copy default configuration files, if they don't already exist
    if CONFIG_FILES:
        try:
            print('Creating configuration files directory...')
            os.makedirs(CONFIG_DIR, exist_ok=True)
            print('Copying necessary configuration files:')
            for i in CONFIG_FILES:
                if not os.path.exists(os.path.join(CONFIG_DIR, i)):
                    print(f'... {i}')
                    shutil.copy2(os.path.join(PKG_DIR, i), CONFIG_DIR) 
        except Exception as e:
            _quit(f"Could not copy configuration files. Reason:\n{e}")

    print('\nApplication successfully installed.\n')

except:
    print("\nInstallation interrupted by user or unknown error.\n")
