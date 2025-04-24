import frappe


def execute():
	try:
		tickets_without_seats = frappe.get_all("Airplane Ticket", filters={"seat": ""}, fields=["name"])

		for ticket in tickets_without_seats:
			ticket_doc = frappe.get_doc("Airplane Ticket", ticket.name)

			ticket_doc.assign_seat()
			ticket_doc.save()

		frappe.db.commit()
	except Exception:
		frappe.log_error("Error in populate_seats.py", "populate_seats.py")
		frappe.db.rollback()
