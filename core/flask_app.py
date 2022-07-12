from . import *

from flask import Flask, request, abort, send_file
from werkzeug.utils import secure_filename

APP = Flask(__name__)

@APP.route('/')
def home():
    with open("templates/main.html", 'r') as f:
        data = f.read()
    return data

@APP.route(PATH, methods=['GET', 'POST'])
def file_sharing():
    if request.method == "GET":
        auth = request.headers.get("Authorization")
        if auth is None:
            print("No auth !")
            abort(401)
        if not do_header_match(auth):
            print("Wrong auth !")
            print(auth)
            abort(401)
        return send_file(os.path.join(DIRECTORY, "output.zip"), attachment_filename='output.zip')
    elif request.method == "POST":
        auth = request.headers.get("Authorization")
        if auth is None:
            print("No auth post !")
            abort(401)
        if not  do_header_match(auth):
            print("Wrong auth post !")
            abort(401)
        if 'file' not in request.files:
            print("No file !")
            abort(400)
        file = request.files['file']
        if file.filename == '':
            abort(400)
        if file:
            file.save(os.path.join(DIRECTORY, "output.zip"))
            return "Uploaded sucess !"
        return "No file to upload !"
