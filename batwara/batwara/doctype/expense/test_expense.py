# Copyright (c) 2026, Build with Ei Ei San and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestExpense(IntegrationTestCase):
	"""
	Integration tests for Expense.
	Use this class for testing interactions between multiple components.
	"""

	def test_equal_split_calculation(self):
		test_expense = frappe.get_doc({
			"doctype": "Expense",
			"description":"test expense",
			"paid_by": "friend1@email.com",
			"amount": 2000,
			"splits": [
				{
					"user":"friend1@email.com",
				},
				{
					"user":"friend2@email.com",
				}
			]
		}).insert()

		self.assertEqual(test_expense.splits[0].amount, 1000)
		self.assertEqual(test_expense.splits[1].amount, 1000)
