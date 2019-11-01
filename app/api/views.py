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

@api.route('/search', methods=['POST'])
def search():
    '''
    API endpoint to find a protein that contains the submitted sequence

    :return: JSON response containing the matched protein
    '''
    current_search = request.json['dna_sequence']  # Template version
    task = search_protein_task.delay(current_search)
    current_app.logger.info('Task ID {} searching for: {}'.format(task.task_id, current_search))
    async_result = AsyncResult(id=task.task_id, app=celery)
    
    result = async_result.get()
    current_app.logger.info('Task ID {} Results: {}'.format(task.task_id, result))

    return jsonify([result])
