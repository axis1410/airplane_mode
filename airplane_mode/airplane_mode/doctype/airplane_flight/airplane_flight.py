# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import format_date, format_duration
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.update_flight_status()

	def update_flight_status(self):
		self.status = "Completed"

	def fetch_airline_name(self):
		try:
			if self.airplane:
				airplane = frappe.get_doc("Airplane", self.airplane)
				if airplane and hasattr(airplane, "airline") and airplane.airline:
					return airplane.airline
		except Exception:
			pass
		return "N/A"

	def get_context(self, context):
		try:
			context.title = self.name
			context.doc = self

			# Format duration properly using frappe utils
			if hasattr(self, "duration") and self.duration:
				context.formatted_duration = format_duration(self.duration)
			else:
				context.formatted_duration = "N/A"

			# Format date properly
			if hasattr(self, "date_of_departure") and self.date_of_departure:
				context.formatted_date = format_date(self.date_of_departure, "d MMMM, YYYY")
			else:
				context.formatted_date = "N/A"

			# Get airline info - can be accessed via doc in template
			try:
				context.airline_name = self.fetch_airline_name()
			except Exception:
				context.airline_name = "N/A"
		except Exception as e:
			frappe.log_error(
				f"Error in AirplaneFlight.get_context: {str(e)}", "AirplaneFlight Template Error"
			)

		return context
