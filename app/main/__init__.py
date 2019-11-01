#!/usr/bin/env python
'''
app/main/__init__.py
'''
from flask import Blueprint

main = Blueprint('main', __name__, static_folder="../ui/build")

from app.main import views
