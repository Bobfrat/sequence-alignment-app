#!/usr/bin/env python
'''
app/main/views.py

View routes for the main application endpoints
'''
import os
from flask import send_from_directory
from app.main import main

@main.route('/', methods=['GET'])
def index():
    return send_from_directory(main.static_folder, 'index.html')


# serve whatever the client requested in the static folder
@main.route('/static/<string:folder>/<string:filename>', methods=['GET'])
def serve_static(folder=None, filename=None):
    if folder is None:
        send_from_directory(os.path.join(main.static_folder, folder), filename)
    return send_from_directory(os.path.join(main.static_folder, 'static', folder), filename)
