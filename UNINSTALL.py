#!/usr/bin/env python3
'''Uninstall function.
   May be used as a standalone script.
'''

import sys
import os
import shutil


def _getlog():
    '''Get and parse application install log.
    '''
    log = []
    logfile = os.path.join(sys.path[0], 'install.log')
    if os.path.lexists(logfile):
        for i in open(logfile).readlines():
            ptype, sep, path = i.strip().partition(':')
            if '' in (ptype, sep, path):
                raise Exception('Error parsing uninstall log.')
            log.append((ptype, path))
    else:
        # no install log, add program directory only;
        # config file, if it exists, will be ignored.
        log = [('dir', sys.path[0])]

    return log


def yesno(question):
    '''Get a yes or no answer to a question.
    '''
    answer = ''
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = input(f'{question} (y/n): ').strip().lower()

    return answer in ('y', 'yes')


def uninstall():
    '''Uninstall application.
    '''
    try:
        ignore_config_files = False
        INSTALL_LOG = _getlog()
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
                    raise Exception('Unknown log entry type.')
    except Exception as e:
        print(f'Application could not be uninstalled.  Reason:\n{e}\n\n'
              'Some files or directories may still be on your filesystem.\n'
              'Please check these paths manually:\n', file=sys.stderr)
        print('\n'.join([path for ptype,path in INSTALL_LOG]), file=sys.stderr)
        sys.exit(1)

    print('Application successfully uninstalled.')
    sys.exit() # ensure application exits after it is uninstalled


if __name__ == '__main__':
    uninstall()
