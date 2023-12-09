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

INSTALL_LOG = []


def _quit(msg):
    '''Print error message and quit.
    '''
    print(f'Error: {msg}\n', file=sys.stderr)
    _rollback()
    sys.exit(1)


def _log(ptype, path):
    '''Record entry in install log.
    '''
    INSTALL_LOG.append((ptype, path))


def _rollback():
    '''Roll back installation.
    '''
    try:
        ignore_config_files = False
        for ptype, path in INSTALL_LOG:
            match ptype:
                case 'dir':
                    shutil.rmtree(path)
                case 'link':
                    os.remove(path)
                case 'config_dir':
                    if yesno(f"Remove settings directory '{path}'?"):
                        shutil.rmtree(path)
                        ignore_config_files = True
                case 'config_file':
                    if ignore_config_files:
                        continue
                    if yesno(f"Remove configuration file '{path}'?"):
                        os.remove(path)
                case _:
                    _quit('Unknown log entry type.')
    except Exception as e:
        print('Installation could not be rolled back.\n'
              'Some files or directories may still be on your filesystem.\n'
              'Please check these paths manually:\n', file=sys.stderr)
        print('\n'.join([path for ptype,path in INSTALL_LOG]), file=sys.stderr)
        sys.exit(1)

    print('Installation rolled back successfully.', file=sys.stderr)


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
    if ICO_FILE:
        ICO_FILE_PATH = os.path.join(INSTALL_DIR, ICO_FILE)
    if DESKTOP_FILE:
        DESKTOP_FILE_PATH = os.path.join(INSTALL_DIR, DESKTOP_FILE)

    d = input(f'Start link directory [{BIN_DIR}]: ').strip()
    BIN_DIR = os.path.expanduser(d or BIN_DIR)

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
        for p in (ICO_PATH, APP_PATH):
            if p and os.path.lexists(p):
                print(f"Removing old symbolic link '{p}'...")
                os.remove(p)
        for i in LINKS:
            p = os.path.join(BIN_DIR, i)
            if os.path.lexists(p):
                print(f"Removing old symbolic link '{i}'...")
                os.remove(p)
    except Exception as e:
        _quit(f"Could not remove old installation. Reason:\n{e}")


    # copy files to install directory
    try:
        print('Creating installation directories...')
        os.makedirs(INSTALL_DIR)
        _log('dir', INSTALL_DIR)
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


    # make files executable
    try:
        print('Configuring executable files...')
        for i in EXECS:
            print(f'... {i}')
            os.chmod(os.path.join(INSTALL_DIR, i), 0o755)
    except Exception as e:
        _quit(f"Could not change file '{i}' to executable. Reason:\n{e}")


    # make symbolic links
    try:
        print('Creating symbolic links...')
        os.makedirs(BIN_DIR, exist_ok=True)
        for i in LINKS:
            print(f'... {i}')
            fpath = os.path.join(INSTALL_DIR, LINKS[i])
            lpath = os.path.join(BIN_DIR, i)
            os.symlink(fpath, lpath)
            _log('link', lpath)
            print
    except Exception as e:
        _quit(f"Could not create symbolic link '{i}'. Reason:\n{e}")

    if ICO_FILE:
        try:
            print('Creating symbolic link to icon...')
            os.makedirs(ICO_DIR, exist_ok=True)
            os.symlink(ICO_FILE_PATH, ICO_PATH)
            _log('link', ICO_PATH)
        except Exception as e:
            _quit(f"Could not create symbolic link to icon. Reason:\n{e}")

    if DESKTOP_FILE:
        try:
            print('Creating symbolic link to desktop file...')
            os.makedirs(APP_DIR, exist_ok=True)
            os.symlink(DESKTOP_FILE_PATH, APP_PATH)
            _log('link', APP_PATH)
        except Exception as e:
            _quit(f"Could not create symbolic link to desktop file. Reason:\n{e}")


    # copy default configuration files, if they don't already exist
    if CONFIG_FILES:
        try:
            print('Creating configuration files directory...')
            os.makedirs(CONFIG_DIR, exist_ok=True)
            if APP_NAME in CONFIG_DIR:
                _log('config_dir', CONFIG_DIR)
            print('Copying necessary configuration files:')
            for i in CONFIG_FILES:
                if not os.path.exists(os.path.join(CONFIG_DIR, i)):
                    print(f'... {i}')
                    shutil.copy2(os.path.join(PKG_DIR, i), CONFIG_DIR) 
                    _log('config_file', os.path.join(CONFIG_DIR, i))
        except Exception as e:
            _quit(f"Could not copy configuration files. Reason:\n{e}")


    # save install log to install directory
    try:
        with open(os.path.join(INSTALL_DIR, 'install.log'), 'w') as f:
            for entry in INSTALL_LOG:
                print(f'{entry[0]}:{entry[1]}', file=f)
    except Exception as e:
        _quit(f'Could not save install log. Reason:\n{e}')

    print('\nApplication successfully installed.\n')


except Exception as e:
    print(e, file=sys.stderr)
    print("\nInstallation interrupted by user or unknown error.\n", file=sys.stderr)
    _rollback()

