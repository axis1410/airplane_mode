# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):
		self.update_flight_status()

	def update_flight_status(self):
		self.status = "Completed"
