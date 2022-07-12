from hashlib import sha256

import getpass
import os


user = input("[?] Please enter the username : ")
passw = getpass.getpass("[?] Please enter the connection password : ")
path = input("[?] Please enter the path webserver will be using (for example if you want the url to be \"http://127.0.0.1:8080/my_drive\", enter \"my_drive\" : ")
while path == '':
    path = input("[?] Please enter the path webserver will be using (for example if you want the url to be \"http://127.0.0.1:8080/my_drive\", enter \"my_drive\" : ")
dirr = os.path.abspath("outputs/")

with open("config.cfg", 'w+') as f:
    f.write(f"""USER={user}
PASS={sha256(passw.encode()).hexdigest()}
PATH={path}
DIRECTORY={dirr}/""")