import frappe


def get_context(context):
	requested_color = frappe.form_dict.get("color")

	context.color = requested_color if requested_color else "black"

	context.title = "Color Display"
	context.description = "A dynamic color display using Jinja templating"
