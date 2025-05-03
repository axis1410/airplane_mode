// Copyright (c) 2025, Aditya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		if (!frm.doc.seat) {
			frm.add_custom_button(
				__("Assign Seat"),
				function () {
					let seat_dialog = new frappe.ui.Dialog({
						title: "Enter Seat Number",
						fields: [
							{
								label: "Seat Number",
								fieldname: "seat",
								fieldtype: "Data",
								reqd: 1,
							},
						],
						primary_action_label: "Assign Seat",
						primary_action(values) {
							frm.set_value("seat", values.seat);
							seat_dialog.hide();
							frm.save();
						},
					});
					seat_dialog.show();
				},
				__("Actions"),
			);
		}
		if (!frm.doc.gate) {
			frm.add_custom_button(
				__("Assign Gate"),
				function () {
					let gate_dialog = new frappe.ui.Dialog({
						title: "Enter Gate Number",
						fields: [
							{
								label: "Gate Number",
								fieldname: "gate",
								fieldtype: "Data",
								reqd: 1,
							},
						],
						primary_action_label: "Assign Gate",
						primary_action(values) {
							frm.set_value("gate", values.gate);
							gate_dialog.hide();
							frm.save();
						},
					});
					gate_dialog.show();
				},
				__("Actions"),
			);
		}
	},
});
