# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlightCrew(Document):
	def before_save(self):
		self._set_full_name()

	def _set_full_name(self):
		self.full_name = f"{self.first_name} {self.last_name if self.last_name else None}".strip()
