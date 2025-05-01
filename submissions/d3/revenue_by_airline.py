# Copyright (c) 2025, Aditya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_cols()
	data = get_data()
	chart = get_chart_data(data)
	total_revenue = sum(row[1] for row in data)
	summary = [
		{
			"label": "Total Revenue",
			"value": total_revenue,
		}
	]

	return columns, data, None, chart, summary


def get_cols():
	columns = [
		{
			"fieldname": "airline",
			"label": "Airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": "200",
		},
		{
			"fieldname": "revenue",
			"label": "Revenue",
			"fieldtype": "Currency",
			"width": "120",
		},
	]

	return columns


def get_data():
	data = []

	airlines = frappe.get_all("Airline", fields=["name"])

	for airline in airlines:
		revenue = (
			frappe.db.sql(
				"""
			SELECT
				SUM(t.flight_price + IFNULL(ai.total_addon_amount, 0)) AS total_revenue
				FROM `tabAirplane Ticket` t
				JOIN `tabAirplane Flight` f on t.flight = f.name
				JOIN `tabAirplane` a on f.airplane = a.name
				LEFT JOIN (
					SELECT parent, SUM(amount) as total_addon_amount
					FROM `tabAirplane Ticket Add-on Item`
					GROUP BY parent
				) ai on t.name = ai.parent
				WHERE a.airline = %s

			""",
				(airline.name),
				as_list=True,
			)[0][0]
			or 0.0
		)
		data.append([airline.name, revenue])
	return data


def get_chart_data(data):
	labels = [row[0] for row in data]
	values = [row[1] for row in data]

	chart = {
		"data": {
			"labels": labels,
			"datasets": [
				{
					"name": "Revenue",
					"values": values,
				}
			],
		},
		"type": "donut",
	}

	return chart
