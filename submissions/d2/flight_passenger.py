# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.set_full_name()

	def set_full_name(self):
		# Handle None values for last_name by using empty string instead
		last_name = self.last_name or ""
		self.full_name = (
			f"{self.first_name}".strip() if not last_name else f"{self.first_name} {last_name}".strip()
		)
