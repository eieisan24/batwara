# Copyright (c) 2026, Build with Ei Ei San and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Expense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from batwara.batwara.doctype.expense_split.expense_split import ExpenseSplit
		from frappe.types import DF

		amended_from: DF.Link | None
		amount: DF.Currency
		currency: DF.Link
		date: DF.Date | None
		description: DF.Data
		notes: DF.SmallText | None
		paid_by: DF.Link
		splits: DF.Table[ExpenseSplit]
		splits_methods: DF.Literal["Equally", "Mantual"]
	# end: auto-generated types

	def before_save(self):
		self.apply_split()

	def apply_split(self):
		if self.splits_methods == "Equally":
			self.calculate_equal_splits()
		else:
			pass

	def calculate_equal_splits(self):
		num_splits = len(self.splits)
		split_amount = self.amount / num_splits

		for s in self.splits:
			s.amount = split_amount
