import sys


def cleared(string):
    output = string
    for e in (' ', '\n', '\t', '\r'):
        output = output.replace(e, '')
    return output

def full_exit():
    print("\n[+] Exiting...")
    sys.exit(0)