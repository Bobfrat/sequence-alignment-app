#!/usr/bin/env python
'''
app/api/__init__.py
'''
from flask import Blueprint

api = Blueprint('api', __name__)

from app.api import views
