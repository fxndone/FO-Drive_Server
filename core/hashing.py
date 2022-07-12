from . import *

from hashlib import sha256
from base64 import b64decode


def make_password(password):
    return sha256(password.encode()).hexdigest()

def do_passwords_match(password):
    return make_password(password) == PASS

def do_header_match(b64encoded):
    if not b64encoded.startswith("Basic "):
        return False
    data = b64decode(b64encoded.split(' ')[1].encode()).decode()
    if len(data.split(':')) != 2:
        return False
    id, password = data.split(':')
    return id == USER and do_passwords_match(password)