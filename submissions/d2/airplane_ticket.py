# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

import random

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_save(self):
		self.assign_seat()

	def on_submit(self):
		self.validate_submit()

	def validate(self):
		self.remove_duplicate_add_ons()
		self.calculate_total_amount()

	def calculate_total_amount(self):
		total = self.flight_price or 0
		for add_on in self.add_ons:
			total += add_on.amount or 0
		self.total_amount = total

	def remove_duplicate_add_ons(self):
		seen_items = set()
		i = 0

		while i < len(self.add_ons):
			if self.add_ons[i].item in seen_items:
				self.add_ons.pop(i)
			else:
				seen_items.add(self.add_ons[i].item)
				i += 1

	def validate_submit(self):
		if self.status != "Boarded":
			frappe.throw("You can only submit the ticket if the status is 'Boarded'.")

	def assign_seat(self):
		if not self.seat:
			self.seat = f"{random.randint(1, 100)}{random.choice(['A', 'B', 'C', 'D'])}"
