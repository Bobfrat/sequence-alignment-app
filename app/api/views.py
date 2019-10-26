#!/usr/bin/env python
'''
app/api/views.py

View routes for the api endpoints
'''
import os
from app import celery
from app.api import api
from celery.result import AsyncResult
from flask import jsonify, session, request, redirect, url_for, current_app
from app.tasks import search_protein_task

@api.route('/search/<string:dna_sequence>', methods=['POST'])
def search(dna_sequence):
    '''
    API endpoint to find a protein that contains the submitted sequence

    :return: JSON response containing the matched protein
    '''
    current_search = request.form['dna_sequence']
    current_app.logger.info('Searching for: {}'.format(current_search))
    task = search_protein_task.delay(current_search)
    async_result = AsyncResult(id=task.task_id, app=celery)
    
    result = async_result.get()

    previous_search = session.get('previous_search', None)
    previous_results = session.get('results', None)
    print(previous_results)
    print(previous_search)

    if previous_results is not None:
        previous_results.insert(0, result)
    else:
        previous_results = [result]

    if previous_search is not None:
        previous_search.insert(0, current_search)
    else:
        previous_search = [result]

    session['results'] = previous_results
    session['previous_search'] = previous_search
    session.modified = True
    print(session)
    return redirect(url_for('main.index'))
