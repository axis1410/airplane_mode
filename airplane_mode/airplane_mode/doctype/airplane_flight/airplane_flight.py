# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.update_flight_status()

	def update_flight_status(self):
		self.status = "Completed"

	def fetch_airline_name(self):
		if self.airplane:
			airplane = frappe.get_doc("Airplane", self.airplane)
			if airplane and airplane.airline:
				return airplane.airline
		return "N/A"
