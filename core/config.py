from . import *

import os


if not os.path.isfile("config.cfg"):
    print("[!] Need a \"config.cfg\" file !")
    print("[!] See README.md, and run \"setup.py\" !")
    full_exit()

USER = PASS = PATH = DIRECTORY = None

with open("config.cfg", 'r') as f:
    for line in f.read().split('\n'):
        if cleared(line).startswith("USER="):
            USER = '='.join(cleared(line).split('=')[1:])
        elif cleared(line).startswith("PASS="):
            PASS = '='.join(cleared(line).split('=')[1:])
        elif cleared(line).startswith("PATH="):
            PATH = cleared(line).split('=')[1]
            if not PATH.startswith('/'):
                PATH = '/' + PATH
        elif cleared(line).startswith("DIRECTORY="):
            DIRECTORY = '='.join(cleared(line).split('=')[1:])

if USER is None or PASS is None or PATH is None or DIRECTORY is None:
    print("[!] Wrong \"config.cfg\" file found !")
    print("[!] Please see README.md, and run \"setup.py\" to create config file !")
    full_exit()