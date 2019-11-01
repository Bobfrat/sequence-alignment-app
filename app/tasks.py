#!/usr/bin/env python
'''
app/tasks.py
'''
import glob
import os
import re
from app import celery
from Bio import SeqIO
from Bio.Seq import Seq


def search_protein(dna_sequence):
    '''
    Return a Protein that contains the input DNA sequence.
    Randomly searches the list of Proteins (PROTEIN_LIST) until one is found

    :param str dna_sequence: The input dna_sequence to search
    '''    
    dna_seq = Seq(dna_sequence)
    results = {
        'dna': dna_sequence,
        'protein': None,
        'start_position': None,
        'end_position': None,
    }
    for filepath in glob.glob('app/sequence_data/*.fasta'):
        for rec in SeqIO.parse(filepath, "fasta"):
            # Look for a match
            ind = rec.seq.find(dna_seq)
            if ind > -1:
                results['protein'] = rec.id
                results['start_position'] = ind
                results['end_position'] = ind + len(dna_seq)
                return results

            # No match, let's try the reverse complement
            ind = rec.seq.find(dna_seq.reverse_complement())
            if ind > -1:
                results['protein'] = rec.id
                results['start_position'] = ind
                results['end_position'] = ind + len(dna_seq)
                return results

    return results


@celery.task(name='search_protein')
def search_protein_task(dna_sequence):
    '''
    Celery task to perform long running job of finding a Protein that contains
    the submitted input DNA sequence

    :param str dna_sequence: The input dna_sequence to search
    '''    
    return search_protein(dna_sequence)


if __name__ == "__main__":
    dna_sequence = 'ATGTTCGAAAACAGAGTCATATGTTGTATCG'
    print(search_protein(dna_sequence))