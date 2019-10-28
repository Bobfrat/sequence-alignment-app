#!/usr/bin/env python
'''
tests/test_tasks.py
'''
from unittest import TestCase
from app.tasks import search_protein


class TestTasks(TestCase):
	'''
	Test class to unit test all the celery tasks
	'''

	def test_search_protein_success(self):
		'''
		Test a successful search case returns expected results
		'''
		dna_sequence = 'ATGTTCGAAAACAGAGTCATATGTTGTATCG'
		expected_protein = 'NC_009899'
		expected_start = 911
		expected_start = 1117

		result = search_protein(dna_sequence)

		assert result['protein'] == expected_protein
		assert result['start_postion'] == expected_start
		assert result['end_position'] == expected_end

	def test_search_protein_fail(self):
		'''
		Test a failed search case returns expected results
		'''
		dna_sequence = 'blah'
		expected_result = None
		result = search_protein(dna_sequence)

		assert result['protein'] == expected_result