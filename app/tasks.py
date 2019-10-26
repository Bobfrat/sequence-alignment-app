#!/usr/bin/env python
'''
app/tasks.py
'''
from app import celery
from random import random
import time

# List will be much larger, proably need to hit a database for full list later
PROTEIN_LIST = [
    'NC_000852',
    'NC_007346',
    'NC_008724',
    'NC_009899',
    'NC_014637',
    'NC_020104',
    'NC_023423',
    'NC_023640',
    'NC_023719',
    'NC_027867'
]

def search_protein(dna_sequence):
    '''
    Return a Protein that contains the input DNA sequence.
    Randomly searches the list of Proteins (PROTEIN_LIST) until one is found

    :param str dna_sequence: The input dna_sequence to search
    '''
    for protein in PROTEIN_LIST:
        if dna_sequence in protein:
            break
    else:
        protein = None
    return protein

@celery.task(name='search_protein')
def search_protein_task(dna_sequence):
    '''
    Celery task to perform long running job of finding a Protein that contains
    the submitted input DNA sequence

    :param str dna_sequence: The input dna_sequence to search
    '''    

    return search_protein(dna_sequence)
