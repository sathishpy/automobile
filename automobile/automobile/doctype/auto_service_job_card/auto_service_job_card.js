// Copyright (c) 2017, Sathisha Poojary and contributors
// For license information, please see license.txt

frappe.ui.form.on('Auto Service Job Card', {
	refresh: function(frm) {
		if (frm.doc.docstatus == 1) {
			frm.add_custom_button(__('Generate Invoice'), function() {
					frm.events.make_sales_invoice(frm)
			});
		}

	},
	invoke_function(frm, method) {
		frappe.call({
			doc: frm.doc,
			method: method,
			callback: function(r) {
				if(!r.exe) {
					frm.refresh_fields()
				}
			}
		});
	},
	service_type: function(frm) {
		frm.events.invoke_function(frm, "populate_service_items")
	},
	vehicle: function(frm) {
		if (frm.doc.docstatus != 1) {
			frm.set_value("service_date", frappe.datetime.nowdate())
		}
		frm.add_fetch("vehicle", "chassis_number", "chassis_number")
		frm.add_fetch("vehicle", "vehicle_model", "vehicle_model")
		frm.add_fetch("vehicle", "odometer", "odometer")
		frm.add_fetch("vehicle", "owner", "customer")
		frm.add_fetch("vehicle", "service_center", "service_center")
		frm.events.invoke_function(frm, "populate_service_type")
	},
	make_sales_invoice: function(frm) {
		frappe.model.open_mapped_doc({
			method: "automobile.automobile.doctype.auto_service_job_card.auto_service_job_card.make_sales_invoice",
			frm: frm,
		})
	},
});
frappe.ui.form.on("Auto Service Job Item", "item", function(frm, cdt, cdn) {
	frm.add_fetch("item", "standard_rate", "rate")
});
