#!/usr/bin/env python
'''
app/main/views.py
'''
from flask import render_template, session
from app.main import main

@main.route('/', methods=['GET'])
def index():
    previous_search = session.get('previous_search')
    results = session.get('results')
    return render_template('index.html', results=results, previous_search=previous_search)
